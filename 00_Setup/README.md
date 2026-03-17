# Canadian Housing Market Analysis

## CPSC 4310 - Data Analytics Project

**Team:** Project Group A (Chloe Lee, Jiwon Jeon, Ryan Back, Vergil Phan, James Gan)
**Semester:** Winter 2026  
**Instructor:** Brahimi, Samiha

---

## 📊 **Project Overview**

This project analyzes and predicts housing price trends across 5 major Canadian cities using machine learning models. We achieved **R² score of 0.925** using historical price data and interest rates.

The analysis covers:

- Exploratory Data Analysis (EDA)
- Feature engineering
- Baseline and advanced predictive models
- City-specific analysis & investment insights
- Visual storytelling for decision support

### **Objectives:**

1. Analyze 20 years of Canadian housing market data (2005-2025)
2. Identify key factors influencing price changes
3. Build predictive models for monthly price forecasting
4. Compare city-specific market dynamics and predictability
5. Provide short-term market direction forecasts per city
6. Create interactive dashboard for stakeholder use

### **Data Sources:**

- **Housing Prices**

  - MLS Home Price Index (via Statistics Canada)
  - Monthly data by city and house type
  - Cities: Vancouver, Toronto, Calgary, Ottawa, Montreal

- **Interest Rates**
  - Bank of Canada
  - Daily rates aggregated to monthly level
  - Mortgage (1Y / 3Y / 5Y), Prime Rate

---

## 👥 **Team Members & Roles**

| Name       | Role                       | Responsibilities                       |
| ---------- | -------------------------- | -------------------------------------- |
| **Jiwon**  | Data Collection & Cleaning | Sourced MLS and Bank of Canada data    |
| **James**  | Data Integration           | Merged datasets, quality assurance     |
| **Chloe**  | EDA & Modeling             | Feature engineering, model development |
| **Vergil** | Visualization              | Tableau dashboard creation             |
| **Ryan**   | Documentation              | Final report and presentation          |

---

## 📁 **Project Structure**

```
CANADIAN-HOUSING-MARKET-ANALYSIS/
│
├── 00_Setup/                           # Installation & Setup
│   ├── README.md                       # This file
│   ├── requirements.txt                # Python packages
│   ├── INSTALLATION_GUIDE.md           # Detailed setup guide
│   └── QUICK_START.md                  # 5-minute setup
│
├── 01_Data/                            # Raw datasets
│   ├── Daily Rates(in).csv             # Bank of Canada rates
│   └── Monthly Home Price and Index by type and city(in).csv  # Monthly home prices & price index by city and house type (Canada)
│
├── 02_Notebooks/                       # Jupyter notebooks
│   ├── 01_data_validation.ipynb        # Data validation & quality checks
│   ├── Housing_Analysis_EDA.ipynb      # Exploratory analysis
│   ├── Baseline_Model.ipynb            # Linear regression
│   └── Advanced_Models.ipynb           # RF, XGBoost, city analysis & forecasts
│
└── 03_Results/                         # Model outputs
    ├── final_predictions.csv           # Deployment-ready predictions
    ├── model_comparison.csv            # Performance metrics (all models)
    ├── city_performance.csv            # City-specific model performance
    ├── baseline_model_performance.csv
    ├── baseline_predictions.csv
    ├── baseline_feature_importance.csv
    ├── rf_feature_importance.csv
    ├── xgb_feature_importance.csv
    ├── housing_data_with_features.csv
    └── visualization/                  # Charts & graphs
        ├── 1_price_trends.png
        ├── 2_interest_rates.png
        ├── 3_dual_axis_vancouver.png
        ├── 4_correlation_heatmap.png
        ├── 5_boxplot_by_city.png
        ├── 6_yoy_trends.png
        ├── 7_actual_vs_predicted.png
        ├── 8_model_comparison.png
        ├── 9_rf_feature_importance.png
        ├── 10_xgb_feature_importance.png
        ├── 11_city_performance_heatmap.png
        ├── 12_price_trends_forecast.png
        └── 13_city_value_comparison.png
```

---

## 🚀 **Quick Start**

### **Prerequisites:**

- Python 3.9 or higher (64-bit)
- Jupyter Notebook
- 2GB free disk space

### **Installation (5 minutes):**

```bash
# 1. Clone or download project
cd CANADIAN-HOUSING-MARKET-ANALYSIS

# 2. Install packages
pip install -r 00_Setup/requirements.txt

# 3. Start Jupyter
jupyter notebook

# 4. Open any notebook in 02_Notebooks/
# 5. Run: Cell → Run All
```

**Detailed instructions:** See `00_Setup/INSTALLATION_GUIDE.md`

---

## 📊 **Key Results**

### **Model Performance:**

| Model                 | R²        | RMSE  | MAPE  | Status      |
| --------------------- | --------- | ----- | ----- | ----------- |
| **Linear Regression** | **0.925** | 0.252 | 51.9% | ✅ **Best** |
| Random Forest         | 0.906     | 0.282 | 89.2% | Good        |
| XGBoost               | 0.908     | 0.278 | 80.7% | Good        |

**Winner:** Linear Regression (92.5% accuracy)  
**Note:** MAPE is inflated due to low baseline prices in early years (2005–2007).

### **Key Findings:**

1. **Past prices are strongest predictors**

   - Previous month's index: 52% feature importance
   - 3-month moving average: 18% importance

2. **Interest rates have moderate impact**

   - 5-year mortgage rate: 8% importance
   - Lag effect of 3-6 months observed

3. **City-specific patterns:**

   - **Most predictable:** Calgary (lowest volatility)
   - **Most volatile:** Toronto (highest price swings)
   - **Highest growth:** Toronto (+305.9% since 2005)

4. **Major events impact:**
   - 2008 Financial Crisis: All cities declined
   - COVID-19 (2020-2021): Synchronized 20-30% growth
   - Rate Hikes (2022-2023): Sharp corrections

---

## 🏙️ **City-Specific Analysis**

Each city has unique market dynamics. We trained separate Random Forest models per city to measure individual predictability and volatility.

### **City Performance Heatmap** (`11_city_performance_heatmap.png`)

Compares R², RMSE, MAE, and volatility (σ) across all 5 cities side by side.

### **Key City Insights:**

| City      | Volatility (σ) | Characteristics                          |
| --------- | -------------- | ---------------------------------------- |
| Calgary   | Lowest         | Most stable, most predictable            |
| Montreal  | Low-Medium     | Steady growth, consistent                |
| Ottawa    | Medium         | Balanced market                          |
| Vancouver | Medium-High    | Strong fundamentals, high growth         |
| Toronto   | Highest        | Maximum growth (+305.9%) but most risky  |

---

## 📈 **Market Forecast & Investment Insights**

### **Short-Term Forecast** (`12_price_trends_forecast.png`)

Using the combined RF + XGBoost prediction on the most recent data point, we project the **3-month price direction** for each city. Green arrow = rising, Red arrow = falling.

> ⚠️ This is a short-term directional forecast only (3–6 months). It is based on historical patterns and should not be used as financial advice.

### **City Investment Score** (`13_city_value_comparison.png`)

We ranked cities using a composite score:
- **40%** — Average monthly growth rate
- **30%** — Stability (lower volatility = better)
- **30%** — Predictability (R² score)

The bubble chart shows Growth vs Volatility, where bubble size represents model predictability. Use this to understand the risk/reward tradeoff per city.

---

## 🔬 **Methodology**

### **Data Sources:**

- **MLS Home Price Index (via Statistics Canada):** Statistics Canada (2005-2025)
- **Interest Rates:** Bank of Canada (2005-2025)

### **Feature Engineering**

Time-series–specific features were engineered to capture housing market dynamics:

- Lag features (1, 3, 12 months) to model temporal dependency
- Month-over-Month (MoM) and Year-over-Year (YoY) percentage changes
- Rolling averages (3-month, 12-month) to smooth short- and long-term trends
- Derived momentum features measuring distance from moving averages

All features were generated after sorting the data by date to preserve temporal integrity.
The resulting dataset was saved as `housing_data_with_features.csv` for reproducibility.

### **Models Developed:**

1. **Linear Regression** (Baseline)
2. **Random Forest** (100 trees, depth 15)
3. **XGBoost** (100 estimators, lr 0.1)
4. **City-Specific Random Forest** (separate model per city)

### **Evaluation Metrics:**

- **R²** (variance explained)
- **RMSE** (root mean squared error)
- **MAE** (mean absolute error)
- **MAPE** (mean absolute percentage error)

---

## 📈 **Notebooks Guide**

### **1. 01_data_validation.ipynb**

**Purpose:** Data validation & quality checks  
**Runtime:** ~1 minute  
**Outputs:** Validation summary, coverage checks, sanity plots

**Key Sections:**
- Raw data loading (rates & housing)
- Date range & frequency validation
- Missing value analysis
- Column & data type verification
- Final validation overview chart

### **2. Housing_Analysis_EDA.ipynb**

**Purpose:** Exploratory Data Analysis  
**Runtime:** ~5 minutes  
**Outputs:** 6 visualizations, feature-engineered dataset

**Key Sections:**
- Data loading & cleaning
- Trend analysis by city
- Correlation analysis
- Feature engineering
- Statistical summaries

### **3. Baseline_Model.ipynb**

**Purpose:** Linear Regression baseline  
**Runtime:** ~2 minutes  
**Outputs:** Baseline performance metrics

**Key Sections:**
- Train/test split (time-based)
- Linear regression training
- Performance evaluation
- Actual vs Predicted visualization

### **4. Advanced_Models.ipynb**

**Purpose:** RF, XGBoost, city-specific analysis & market forecasts  
**Runtime:** ~10 minutes  
**Outputs:** Final predictions, model comparison, city insights, forecast charts

**Key Sections:**
- Part 1–9: Random Forest & XGBoost training, comparison, feature importance
- Part 10: City-specific models & performance heatmap
- Part 11: Historical trends, 3-month forecast, city investment score ranking

---

## 📊 **Deliverables**

### **For Vergil (Tableau Dashboard):**

- ✅ `final_predictions.csv` - Deployment-ready predictions
- ✅ `model_comparison.csv` - Performance metrics
- ✅ `city_performance.csv` - City-specific results
- ✅ 13 visualization charts

### **For Ryan (Presentation):**

- ✅ Model performance comparison
- ✅ Key findings summary
- ✅ City investment score ranking
- ✅ 3-month forecast per city
- ✅ Feature importance rankings

### **For Professor:**

- ✅ All 4 Jupyter notebooks (with outputs)
- ✅ Final report (Milestone 3)
- ✅ Complete project package

---

## 🔧 **Technical Details**

### **System Requirements:**

- **OS:** Windows, Mac, or Linux
- **Python:** 3.9, 3.10, or 3.11 (64-bit)
- **RAM:** 4GB minimum, 8GB recommended
- **Disk:** 2GB free space

### **Dependencies:**

```
pandas >= 2.0.0
numpy >= 1.24.0
matplotlib >= 3.7.0
seaborn >= 0.12.0
scikit-learn >= 1.3.0
xgboost >= 2.0.0
jupyter >= 1.0.0
```

### **Tested On:**

- ✅ macOS 14 (Sonoma)
- ✅ Windows 11
- ✅ Ubuntu 22.04

---

## 📚 **How to Use**

### **For Team Members:**

**If you're setting up for the first time:**

1. Read `00_Setup/QUICK_START.md`
2. Install packages: `pip install -r requirements.txt`
3. Open notebooks in order (EDA → Baseline → Advanced)

### 🧠 Jupyter Kernel Selection (Recommended)

For consistency across the team, we recommend using the **"Python (Housing)"** kernel.

**If you see the kernel menu when opening a notebook:**
1. Choose **"Python (Housing)"** (if available)
2. Click **Select**
3. Run all cells from top to bottom

**If "Python (Housing)" is not available:**
- Select any available Python kernel (Python 3, ipykernel, etc.)
- As long as you installed packages (`pip install -r requirements.txt`), the code will run fine
- To register the "Python (Housing)" kernel, see `00_Setup/INSTALLATION_GUIDE.md` Method 4

⚠️ If you get import errors, the kernel may be using a different Python installation. See troubleshooting below.

**If you encounter issues:**

1. Check `00_Setup/INSTALLATION_GUIDE.md` for detailed kernel setup
2. Verify Python version: `python --version` (must be 3.9+, 64-bit)
3. Contact Chloe for technical help

### **For Replication:**

```bash
# 1. Navigate to project
cd CANADIAN-HOUSING-MARKET-ANALYSIS

# 2. Run EDA
jupyter notebook 02_Notebooks/Housing_Analysis_EDA.ipynb
# Cell → Run All

# 3. Run Baseline
jupyter notebook 02_Notebooks/Baseline_Model.ipynb
# Cell → Run All

# 4. Run Advanced Models (includes city analysis & forecasts)
jupyter notebook 02_Notebooks/Advanced_Models.ipynb
# Cell → Run All

# Results will be in 03_Results/
```

---

## 🎯 **Project Timeline**

| Week | Milestone                              | Status         |
| ---- | -------------------------------------- | -------------- |
| 1-2  | Topic Selection & Data Collection      | ✅ Complete    |
| 3-4  | Data Cleaning & Integration            | ✅ Complete    |
| 5-6  | Exploratory Data Analysis              | ✅ Complete    |
| 7    | Baseline Model (Milestone 2)           | ✅ Complete    |
| 8-10 | Advanced Modeling                      | ✅ Complete    |
| 11   | Dashboard & Final Report (Milestone 3) | ✅ Complete    |
| 12   | Final Presentation                     | 🔄 In Progress |

---

## 🔍 **Key Insights**

### **1. Market Dynamics:**

- Strong **autocorrelation** in housing prices (R² = 0.925)
- Short-term trends (3-month MA) more predictive than long-term
- Interest rate changes take 3-6 months to impact prices

### **2. City Comparisons:**

- **Toronto:** Highest growth (+305.9%) but most volatile — high risk, high reward
- **Vancouver:** Second highest (+258.4%), strong fundamentals
- **Calgary:** Most stable, lowest volatility — easiest to predict
- **Montreal & Ottawa:** Balanced markets with moderate growth

### **3. Predictive Power:**

- Past month's price explains 52% of next month's movement
- Moving averages capture trend momentum effectively
- Interest rates have moderate but consistent impact (8%)

### **4. Investment Perspective:**

- **Best stability:** Calgary
- **Best growth potential:** Toronto / Vancouver
- **Best balance (growth + stability):** See `13_city_value_comparison.png` for full ranking

---

## 📞 **Contact & Support**

### **Technical Issues:**

**Chloe Lee (EDA & Modeling)**

- Email: chloelee.lee@uleth.ca
- Best for: Python, Jupyter, model questions

### **Data Questions:**

**James (Data Integration)**

- Best for: Dataset structure, missing values

### **Dashboard:**

**Vergil (Visualization)**

- Best for: Tableau, dashboard features

---

## 📄 **License & Academic Integrity**

This project is submitted for CPSC 4310 - Data Analytics at University of Lethbridge.

**Academic Use Only:**

- This code is for educational purposes
- Do not use for commercial applications
- Cite appropriately if referencing

**Data Sources:**

- Statistics Canada (MLS Home Price Index)
- Bank of Canada (Interest Rates)

---

## 🙏 **Acknowledgments**

- **Professor Brahimi, Samiha** for guidance and feedback
- **Statistics Canada** for MLS data access
- **Bank of Canada** for public interest rate data
- **scikit-learn & XGBoost** communities for excellent documentation

---

## 📈 **Future Work**

### **Potential Improvements:**

1. **Real-time updates:** Monthly model retraining
2. **Additional features:** Immigration data, housing starts, unemployment
3. **City-specific models:** Already implemented — next step is hyperparameter tuning per city
4. **Prediction intervals:** Add confidence bounds to forecasts
5. **API deployment:** Real-time prediction service

### **Research Extensions:**

- Neighborhood-level predictions
- External factors integration (policy, immigration)
- Multi-step forecasting (3, 6, 12 months ahead)
- Ensemble methods combining multiple models

---

## 📊 **Project Metrics**

- **Lines of Code:** ~2,500+
- **Data Points Analyzed:** 7,560 (20 years × 5 cities × 6 house types)
- **Features Engineered:** 13
- **Models Tested:** 3 global + 5 city-specific
- **Visualizations Created:** 13
- **Model Performance:** R² = 0.925

---

## ✅ **Checklist for Users**

Before running notebooks:

- [ ] Python 3.9+ (64-bit) installed
- [ ] All packages installed (`pip install -r requirements.txt`)
- [ ] Jupyter notebook working
- [ ] CSV files in `01_Data/` folder
- [ ] Sufficient disk space (2GB+)

For successful execution:

- [ ] Run notebooks in order (EDA → Baseline → Advanced)
- [ ] Allow 10-15 minutes total runtime
- [ ] Check `03_Results/` for outputs
- [ ] Verify `final_predictions.csv` and `city_performance.csv` created

---

## 🎓 **Learning Outcomes**

Through this project, we gained experience in:

- **Data Wrangling:** Cleaning, merging, feature engineering
- **Statistical Analysis:** Correlation, trend analysis, visualization
- **Machine Learning:** Regression models, ensemble methods, city-specific modeling
- **Model Evaluation:** Cross-validation, performance metrics
- **Market Analysis:** Investment scoring, risk vs reward comparison
- **Collaboration:** Team workflow, version control
- **Communication:** Documentation, presentation, dashboards

---

**Last Updated:** February 11, 2026  
**Version:** 1.3  
**Status:** ✅ Complete

---

**For questions, issues, or feedback, contact the team!**

🚀 **Happy Analyzing!**