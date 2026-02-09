# Housing Market Analysis - Usage Guide
## CPSC 4310 Project - Chloe's EDA Work

---

## 📦 **What You Got:**

You now have **TWO ways** to run the analysis:

1. **Jupyter Notebook** (`Housing_Analysis_EDA.ipynb`) - **RECOMMENDED!**
2. **Python Script** (`housing_eda.py`) - Automated version

---

## 📓 **Option 1: Jupyter Notebook (RECOMMENDED)**

### **What is it?**
- Interactive notebook with code + explanations + visualizations
- You can run it cell-by-cell
- Perfect for Milestone 2 submission
- You can add your own notes

### **How to use:**

#### **Step 1: Install Jupyter (if you don't have it)**
```bash
pip install jupyter notebook pandas numpy matplotlib seaborn
```

#### **Step 2: Put files in the same folder**
```
your_folder/
├── Housing_Analysis_EDA.ipynb          ← The notebook
├── Monthly_Home_Price_and_Index_by_type_and_city_in_.csv   ← Housing data
└── Daily_Rates_in_.csv                 ← Interest rate data
```

#### **Step 3: Start Jupyter**
```bash
cd your_folder
jupyter notebook
```

This will open your browser!

#### **Step 4: Open the notebook**
- Click on `Housing_Analysis_EDA.ipynb`
- You'll see all the cells

#### **Step 5: Run the cells**
**Option A: Run all at once**
- Menu → Cell → Run All
- Wait 1-2 minutes
- All visualizations appear!

**Option B: Run one by one**
- Click on first cell
- Press `Shift + Enter` to run
- Keep pressing `Shift + Enter` to go through each cell
- This is better for learning!

#### **Step 6: Save your work**
- File → Save
- You can submit this notebook for Milestone 2!

---

## 🐍 **Option 2: Python Script (AUTOMATED)**

### **What is it?**
- Runs everything automatically
- Generates all visualizations + CSV
- No interaction needed
- Good for quick re-runs

### **How to use:**

#### **Step 1: Install packages**
```bash
pip install pandas numpy matplotlib seaborn
```

#### **Step 2: Put files in the same folder**
```
your_folder/
├── housing_eda.py                      ← The script
├── Monthly_Home_Price_and_Index_by_type_and_city_in_.csv   ← Housing data
└── Daily_Rates_in_.csv                 ← Interest rate data
```

#### **Step 3: Run the script**
```bash
cd your_folder
python housing_eda.py
```

#### **Step 4: Check the output folder**
After running, you'll get a new `output/` folder:
```
output/
├── 1_price_trends.png
├── 2_interest_rates.png
├── 3_dual_axis_vancouver.png
├── 4_correlation_heatmap.png
├── 5_boxplot_by_city.png
├── 6_yoy_trends.png
├── housing_data_with_features.csv      ← For modeling!
└── summary_statistics.txt
```

---

## 📊 **What You'll Get:**

### **6 Visualizations:**
1. **Price Trends by City** - All 5 cities over time
2. **Interest Rate Trends** - Mortgage rates 2005-2025
3. **Dual-Axis Chart** - Vancouver price vs mortgage rate
4. **Correlation Heatmap** - Feature relationships
5. **Box Plot** - Price distribution by city
6. **YoY Change Trends** - Year-over-year growth rates

### **1 Processed Dataset:**
- `housing_data_with_features.csv`
- 1,260 rows × 23 columns
- Ready for modeling!
- Includes all engineered features (lags, YoY, MA)

### **1 Summary File:**
- `summary_statistics.txt`
- Key statistics by city
- Feature correlations

---

## 🎯 **What to Do Next:**

### **For Milestone 2 (Week 7):**
✅ You already have:
- EDA complete (6 visualizations)
- Processed data with features
- Summary statistics

⏭️ Still need:
- Baseline model (Linear Regression)
- Model evaluation (RMSE, MAE, R², MAPE)
- Progress report (1-2 pages)

### **For Milestone 3 (Week 11):**
- Advanced models (Random Forest, XGBoost)
- Model comparison
- Feature importance analysis
- Predictions for Vergil's dashboard

---

## 🔧 **Troubleshooting:**

### **Problem: "Module not found" error**
```bash
# Install missing packages
pip install pandas numpy matplotlib seaborn
```

### **Problem: "File not found" error**
- Make sure CSV files are in the same folder as the notebook/script
- Check file names match exactly (case-sensitive!)

### **Problem: Jupyter won't start**
```bash
# Try this instead
pip install jupyterlab
jupyter lab
```

### **Problem: Visualizations don't show in Jupyter**
Add this at the top of the first cell:
```python
%matplotlib inline
```

### **Problem: Script runs but no output folder**
- Check for error messages
- Make sure you have write permissions in the folder

---

## 📧 **Sharing with Team:**

### **For Jiwon & James:**
- Show them the processed CSV file
- They can verify the data cleaning

### **For Vergil:**
- Give him:
  - `housing_data_with_features.csv` (he'll need this!)
  - The PNG visualizations (for reference)
- Wait until you have predictions (Milestone 3)

### **For Ryan:**
- Show the visualizations for presentation
- Share key findings from summary file

---

## 💡 **Tips:**

1. **Always run Jupyter cells in order** (top to bottom)
2. **Don't skip the data loading cells** or later cells will fail
3. **The notebook takes 1-2 minutes to run completely**
4. **Save your work often** in Jupyter (Cmd/Ctrl + S)
5. **You can add markdown cells** to write your own notes
6. **The script is faster** but notebook is better for learning

---

## ✅ **Quick Start (Choose One):**

### **For Interactive Exploration:**
```bash
jupyter notebook
# Open Housing_Analysis_EDA.ipynb
# Run all cells
```

### **For Quick Results:**
```bash
python housing_eda.py
# Check output/ folder
```

---

## 📚 **What Each Section Does:**

### **Jupyter Notebook Sections:**
1. **Part 1:** Setup - Import libraries
2. **Part 2:** Data Loading - Read CSV files
3. **Part 3:** Preprocessing - Clean and merge data
4. **Part 4:** Feature Engineering - Create lag, YoY, MA features
5. **Part 5:** EDA - All 6 visualizations
6. **Part 6:** Summary - Key findings
7. **Part 7:** Save - Export processed data

### **Python Script Flow:**
```
Load Data → Preprocess → Create Features → 
→ Generate Visualizations → Save Everything
```

---

## 🎓 **For Your Submission:**

### **Milestone 2 Package:**
Include:
- ✅ Jupyter Notebook (with outputs visible)
- ✅ All 6 visualization PNG files
- ✅ Processed CSV file
- ✅ 1-2 page progress report (you write this separately)

### **What to Write in Progress Report:**
- Brief intro to the project
- Data sources used
- Features created (lag, YoY, MA)
- Key findings from EDA
- Next steps (baseline model)

---

**Questions?** 
- Check the notebook markdown cells for explanations
- Look at the script comments for details
- Run small sections at a time to debug

**Good luck! 🚀**
