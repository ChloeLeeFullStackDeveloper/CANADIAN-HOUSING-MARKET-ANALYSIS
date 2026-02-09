#!/usr/bin/env python3
"""
Canadian Housing Market Analysis - EDA Script
CPSC 4310 - Data Analytics Project

Author: Chloe Lee
Date: February 2025

This script performs:
1. Data loading and preprocessing
2. Feature engineering
3. Exploratory data analysis
4. Visualization generation
5. Data export for modeling

Usage:
    python housing_eda.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os
from datetime import datetime

warnings.filterwarnings('ignore')

# Configuration
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# File paths (update these to your file locations)
HOUSING_FILE = 'data/Monthly Home Price and Index by type and city(in).csv'
RATES_FILE = 'data/Daily Rates(in).csv'
OUTPUT_DIR = 'output'

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 80)
print("CANADIAN HOUSING MARKET ANALYSIS - EDA SCRIPT")
print("=" * 80)
print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# ============================================================================
# STEP 1: DATA LOADING
# ============================================================================
def load_data():
    """Load housing and interest rate data"""
    print("[STEP 1] Loading data...")
    
    housing = pd.read_csv(HOUSING_FILE)
    rates = pd.read_csv(RATES_FILE)
    
    print(f"  ✓ Housing data: {housing.shape[0]} rows, {housing.shape[1]} columns")
    print(f"  ✓ Rates data: {rates.shape[0]} rows, {rates.shape[1]} columns")
    
    return housing, rates


# ============================================================================
# STEP 2: DATA PREPROCESSING
# ============================================================================
def preprocess_data(housing, rates):
    """Preprocess and merge housing and rates data"""
    print("\n[STEP 2] Preprocessing data...")
    
    # Convert dates
    print("  [2.1] Converting dates...")
    housing['Date'] = pd.to_datetime(housing['Date'])
    rates['Date'] = pd.to_datetime(rates['Date'])
    
    # Filter for Composite house type
    print("  [2.2] Filtering for Composite house type...")
    housing_composite = housing[housing['House_Type'] == 'Composite'].copy()
    print(f"    → Filtered to {len(housing_composite)} rows")
    
    # Convert daily rates to monthly
    print("  [2.3] Converting rates to monthly...")
    rates['YearMonth'] = rates['Date'].dt.to_period('M')
    rates_monthly = rates.groupby('YearMonth').agg({
        'Mortgage_1Y': 'mean',
        'Mortgage_3Y': 'mean',
        'Mortgage_5Y': 'mean',
        'Prime_Rate': 'mean',
        'Policy_Rate': 'mean'
    }).reset_index()
    rates_monthly['Date'] = rates_monthly['YearMonth'].dt.to_timestamp()
    rates_monthly = rates_monthly.drop('YearMonth', axis=1)
    print(f"    → {len(rates_monthly)} monthly observations")
    
    # Merge datasets
    print("  [2.4] Merging datasets...")
    df = housing_composite.merge(rates_monthly, on='Date', how='left')
    
    # Sort by City and Date
    print("  [2.5] Sorting data...")
    df = df.sort_values(['City', 'Date']).reset_index(drop=True)
    
    print(f"  ✓ Merged dataset: {len(df)} rows, {len(df.columns)} columns")
    
    return df


# ============================================================================
# STEP 3: FEATURE ENGINEERING
# ============================================================================
def create_features(df):
    """Create lag, change, and rolling average features"""
    print("\n[STEP 3] Feature engineering...")
    
    # Lag features
    print("  [3.1] Creating lag features...")
    df['Index_Lag1'] = df.groupby('City')['Index'].shift(1)
    df['Index_Lag3'] = df.groupby('City')['Index'].shift(3)
    df['Index_Lag12'] = df.groupby('City')['Index'].shift(12)
    
    # Change features
    print("  [3.2] Creating change features...")
    df['Index_MoM_Change'] = df.groupby('City')['Index'].pct_change(1) * 100
    df['Index_YoY_Change'] = df.groupby('City')['Index'].pct_change(12) * 100
    df['Mortgage_5Y_Change'] = df.groupby('City')['Mortgage_5Y'].diff()
    
    # Rolling averages
    print("  [3.3] Creating rolling averages...")
    df['Index_MA3'] = df.groupby('City')['Index'].transform(
        lambda x: x.rolling(3, min_periods=1).mean()
    )
    df['Index_MA12'] = df.groupby('City')['Index'].transform(
        lambda x: x.rolling(12, min_periods=1).mean()
    )
    
    # Time features
    print("  [3.4] Creating time features...")
    df['Month'] = df['Date'].dt.month
    df['Quarter'] = df['Date'].dt.quarter
    df['Year'] = df['Date'].dt.year
    
    # Derived features
    print("  [3.5] Creating derived features...")
    df['Price_Above_MA3'] = df['Index'] - df['Index_MA3']
    df['MA3_MA12_Diff'] = df['Index_MA3'] - df['Index_MA12']
    
    new_features = [
        'Index_Lag1', 'Index_Lag3', 'Index_Lag12',
        'Index_MoM_Change', 'Index_YoY_Change', 'Mortgage_5Y_Change',
        'Index_MA3', 'Index_MA12',
        'Month', 'Quarter', 'Year',
        'Price_Above_MA3', 'MA3_MA12_Diff'
    ]
    
    print(f"  ✓ Created {len(new_features)} new features")
    
    return df


# ============================================================================
# STEP 4: EXPLORATORY DATA ANALYSIS
# ============================================================================
def create_visualizations(df):
    """Create all EDA visualizations"""
    print("\n[STEP 4] Creating visualizations...")
    
    # Viz 1: Price Trends by City
    print("  [4.1] Price trends by city...")
    fig, ax = plt.subplots(figsize=(14, 7))
    cities = df['City'].unique()
    colors = plt.cm.Set3(np.linspace(0, 1, len(cities)))
    
    for city, color in zip(cities, colors):
        city_data = df[df['City'] == city].sort_values('Date')
        ax.plot(city_data['Date'], city_data['Index'], 
                label=city, linewidth=2.5, color=color, alpha=0.8)
    
    # Event markers
    ax.axvline(pd.to_datetime('2008-09-01'), color='red', linestyle='--', alpha=0.5, linewidth=1)
    ax.text(pd.to_datetime('2008-09-01'), ax.get_ylim()[1]*0.95, 
            '2008 Crisis', rotation=90, va='top', ha='right', fontsize=9, color='red')
    
    ax.axvline(pd.to_datetime('2020-03-01'), color='orange', linestyle='--', alpha=0.5, linewidth=1)
    ax.text(pd.to_datetime('2020-03-01'), ax.get_ylim()[1]*0.95, 
            'COVID-19', rotation=90, va='top', ha='right', fontsize=9, color='orange')
    
    ax.axvline(pd.to_datetime('2022-03-01'), color='purple', linestyle='--', alpha=0.5, linewidth=1)
    ax.text(pd.to_datetime('2022-03-01'), ax.get_ylim()[1]*0.95, 
            'Rate Hikes', rotation=90, va='top', ha='right', fontsize=9, color='purple')
    
    ax.set_title('Housing Price Index by City (2005-2025)', fontsize=16, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price Index (2005-01 = 100)', fontsize=12)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/1_price_trends.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Viz 2: Interest Rate Trends
    print("  [4.2] Interest rate trends...")
    rates_df = df[['Date', 'Mortgage_1Y', 'Mortgage_3Y', 'Mortgage_5Y', 'Prime_Rate']].drop_duplicates('Date').sort_values('Date')
    
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(rates_df['Date'], rates_df['Mortgage_5Y'], label='5-Year Mortgage', 
            linewidth=2.5, color='#e74c3c')
    ax.plot(rates_df['Date'], rates_df['Mortgage_3Y'], label='3-Year Mortgage', 
            linewidth=2, color='#3498db', alpha=0.7)
    ax.plot(rates_df['Date'], rates_df['Mortgage_1Y'], label='1-Year Mortgage', 
            linewidth=2, color='#2ecc71', alpha=0.7)
    ax.plot(rates_df['Date'], rates_df['Prime_Rate'], label='Prime Rate', 
            linewidth=2, color='#f39c12', linestyle='--', alpha=0.7)
    
    ax.set_title('Interest Rate Trends (2005-2025)', fontsize=16, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Interest Rate (%)', fontsize=12)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/2_interest_rates.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Viz 3: Dual-Axis Chart
    print("  [4.3] Dual-axis chart (Vancouver)...")
    van_data = df[df['City'] == 'Greater Vancouver'].sort_values('Date')
    
    fig, ax1 = plt.subplots(figsize=(14, 7))
    color = 'tab:blue'
    ax1.set_xlabel('Date', fontsize=12)
    ax1.set_ylabel('Price Index', color=color, fontsize=12, fontweight='bold')
    ax1.plot(van_data['Date'], van_data['Index'], color=color, linewidth=3)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, alpha=0.3)
    
    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('5-Year Mortgage Rate (%)', color=color, fontsize=12, fontweight='bold')
    ax2.plot(van_data['Date'], van_data['Mortgage_5Y'], color=color, linewidth=2.5, 
             linestyle='--', alpha=0.8)
    ax2.tick_params(axis='y', labelcolor=color)
    
    plt.title('Greater Vancouver: Price vs Mortgage Rate', fontsize=16, fontweight='bold', pad=20)
    fig.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/3_dual_axis_vancouver.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Viz 4: Correlation Heatmap
    print("  [4.4] Correlation heatmap...")
    numeric_features = [
        'Index', 'Mortgage_1Y', 'Mortgage_3Y', 'Mortgage_5Y', 'Prime_Rate',
        'Index_Lag1', 'Index_Lag3', 'Index_Lag12',
        'Index_MoM_Change', 'Index_YoY_Change',
        'Index_MA3', 'Index_MA12'
    ]
    
    corr_data = df[numeric_features].dropna()
    correlation_matrix = corr_data.corr()
    
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8},
                vmin=-1, vmax=1)
    plt.title('Feature Correlation Heatmap', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/4_correlation_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Viz 5: Box Plot
    print("  [4.5] Box plot by city...")
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.boxplot(data=df, x='City', y='Index', palette='Set3', ax=ax)
    ax.set_title('Price Index Distribution by City', fontsize=16, fontweight='bold')
    ax.set_xlabel('City', fontsize=12)
    ax.set_ylabel('Price Index', fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/5_boxplot_by_city.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Viz 6: YoY Change Trends
    print("  [4.6] YoY change trends...")
    fig, ax = plt.subplots(figsize=(14, 7))
    
    for city, color in zip(cities, colors):
        city_data = df[df['City'] == city].sort_values('Date')
        ax.plot(city_data['Date'], city_data['Index_YoY_Change'], 
                label=city, linewidth=2, color=color, alpha=0.8)
    
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5, alpha=0.5)
    ax.set_title('Year-over-Year Price Change', fontsize=16, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('YoY Change (%)', fontsize=12)
    ax.legend(loc='best', fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/6_yoy_trends.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("  ✓ All visualizations saved to 'output/' directory")


# ============================================================================
# STEP 5: SUMMARY STATISTICS
# ============================================================================
def generate_summary(df):
    """Generate and save summary statistics"""
    print("\n[STEP 5] Generating summary statistics...")
    
    # City statistics
    stats = df.groupby('City')['Index'].agg(['min', 'max', 'mean', 'std'])
    stats['growth'] = ((stats['max'] - stats['min']) / stats['min'] * 100)
    stats = stats.round(2)
    
    print("\nPrice Index Statistics by City:")
    print("=" * 80)
    print(stats.to_string())
    
    # Correlation with Index
    numeric_features = [
        'Index', 'Mortgage_5Y', 'Index_Lag1', 'Index_Lag3', 'Index_Lag12',
        'Index_YoY_Change', 'Index_MA3', 'Index_MA12'
    ]
    
    corr_data = df[numeric_features].dropna()
    correlation_matrix = corr_data.corr()
    index_corr = correlation_matrix['Index'].sort_values(ascending=False)
    
    print("\nTop Correlations with Housing Price Index:")
    print("=" * 60)
    for feature, corr in index_corr.items():
        if feature != 'Index':
            print(f"  {feature:25} : {corr:6.3f}")
    
    # Save summary to file
    with open(f'{OUTPUT_DIR}/summary_statistics.txt', 'w') as f:
        f.write("HOUSING PRICE STATISTICS BY CITY\n")
        f.write("=" * 80 + "\n\n")
        f.write(stats.to_string())
        f.write("\n\n\nCORRELATION WITH HOUSING PRICE INDEX\n")
        f.write("=" * 60 + "\n\n")
        for feature, corr in index_corr.items():
            if feature != 'Index':
                f.write(f"{feature:30} : {corr:6.3f}\n")
    
    print("\n  ✓ Summary statistics saved to 'output/summary_statistics.txt'")


# ============================================================================
# STEP 6: SAVE PROCESSED DATA
# ============================================================================
def save_data(df):
    """Save processed dataset"""
    print("\n[STEP 6] Saving processed data...")
    
    output_file = f'{OUTPUT_DIR}/housing_data_with_features.csv'
    df.to_csv(output_file, index=False)
    
    print(f"  ✓ Saved to: {output_file}")
    print(f"    Rows: {len(df)}")
    print(f"    Columns: {len(df.columns)}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================
def main():
    """Main execution function"""
    try:
        # Step 1: Load data
        housing, rates = load_data()
        
        # Step 2: Preprocess
        df = preprocess_data(housing, rates)
        
        # Step 3: Feature engineering
        df = create_features(df)
        
        # Step 4: Create visualizations
        create_visualizations(df)
        
        # Step 5: Generate summary
        generate_summary(df)
        
        # Step 6: Save processed data
        save_data(df)
        
        # Final summary
        print("\n" + "=" * 80)
        print("✅ EDA COMPLETE!")
        print("=" * 80)
        print(f"\nOutputs saved to '{OUTPUT_DIR}/' directory:")
        print("  - 6 visualization PNG files")
        print("  - housing_data_with_features.csv")
        print("  - summary_statistics.txt")
        print(f"\nEnd time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\nNext step: Build baseline model!")
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
