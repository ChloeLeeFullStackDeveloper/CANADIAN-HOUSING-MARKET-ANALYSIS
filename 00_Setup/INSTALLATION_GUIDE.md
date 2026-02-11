# Installation Guide - CPSC 4310 Housing Project
## For Team Members: Jiwon, James, Vergil, Ryan

---

## 📋 **What You Need**

Before running our notebooks, you need:
- Python 3.9 or higher (64-bit)
- Jupyter Notebook
- Required Python packages

---

## 🚀 **Quick Start (3 Methods)**

Choose the method that works best for you!

---

## **Method 1: Using requirements.txt** ⭐ **EASIEST!**

### **Step 1: Download Files**

Download these files from our shared folder:
- `requirements.txt`
- All `.ipynb` notebooks
- `01_Data/` folder with CSV files

### **Step 2: Open Terminal/Command Prompt**

Navigate to project folder:
```bash
cd path/to/CANADIAN-HOUSING-MARKET-ANALYSIS
```

### **Step 3: Install Everything**

```bash
# One command installs everything!
pip install -r requirements.txt
```

### **Step 4: Start Jupyter**

```bash
jupyter notebook
```

### **Step 5: Run Notebooks**

Open any notebook → **Cell → Run All**

---

## **Method 2: Manual Installation**

### **For Windows:**

```bash
# Open Command Prompt (cmd)
pip install pandas numpy matplotlib seaborn scikit-learn xgboost jupyter
```

### **For Mac:**

```bash
# Open Terminal
pip3 install pandas numpy matplotlib seaborn scikit-learn xgboost jupyter

# If you have Homebrew and get errors:
brew install libomp
pip3 install xgboost
```

### **For Linux:**

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost jupyter
```

---

## **Method 3: Using Anaconda** (If you have it)

### **Step 1: Open Anaconda Prompt**

### **Step 2: Create Environment (Optional but Recommended)**

```bash
conda create -n housing python=3.11
conda activate housing
```

### **Step 3: Install Packages**

```bash
conda install pandas numpy matplotlib seaborn scikit-learn jupyter
conda install -c conda-forge xgboost
```

### **Step 4: Start Jupyter**

```bash
jupyter notebook
```

---

## 🔧 **Troubleshooting**

### **Problem 1: "pip not found"**

**Solution:**
```bash
# Windows:
python -m pip install -r requirements.txt

# Mac/Linux:
python3 -m pip install -r requirements.txt
```

---

### **Problem 2: "ModuleNotFoundError: No module named 'matplotlib'"**

**Solution:**

Check which Python Jupyter is using:

```python
# In Jupyter notebook, run this cell:
import sys
print(sys.executable)
```

Then install to that Python:
```bash
/path/to/that/python -m pip install matplotlib seaborn scikit-learn xgboost
```

---

### **Problem 3: XGBoost Won't Install (Mac)**

**Error:** `XGBoost Library could not be loaded` or `Library not loaded: @rpath/libomp.dylib`

#### **Step 1: Check if you have 32-bit Python (common cause)**
```bash
python3 -c "import struct; print('64-bit' if struct.calcsize('P') == 8 else '32-bit')"
```

If it says **32-bit**, reinstall Python from https://www.python.org/downloads/ and make sure to download the **64-bit** version.

#### **Option A: Install OpenMP (try this first)**
```bash
brew install libomp
pip uninstall xgboost -y
pip install xgboost
```

#### **Option B: Use Conda**
```bash
conda install -c conda-forge xgboost
```

#### **Option C: Skip XGBoost**
Don't worry! Random Forest works great too. Just run the notebooks - they'll work with RF only.

---

### **Problem 4: "Permission Denied"**

**Solution:**

Add `--user` flag:
```bash
pip install --user -r requirements.txt
```

---

### **Problem 5: Import Errors After Installation**

**Solution:**

Restart Jupyter kernel:
- In Jupyter: **Kernel → Restart**
- Then re-run all cells

---

## 📁 **File Organization**

Make sure your folder looks like this:

```
CANADIAN-HOUSING-MARKET-ANALYSIS/
├── 00_Setup/
│   ├── README.md
│   ├── requirements.txt
│   ├── INSTALLATION_GUIDE.md
│   └── QUICK_START.md
├── 01_Data/
│   ├── Daily Rates(in).csv
│   └── Monthly Home Price and Index by type and city(in).csv
├── 02_Notebooks/
│   ├── 01_data_validation.ipynb
│   ├── Housing_Analysis_EDA.ipynb
│   ├── Baseline_Model.ipynb
│   └── Advanced_Models.ipynb
└── 03_Results/
    ├── final_predictions.csv
    ├── model_comparison.csv
    └── visualization/
```

---

## ✅ **Verification**

After installation, verify everything works:

### **Test 1: Check Packages**

```bash
python -c "import pandas, numpy, matplotlib, seaborn, sklearn; print('✓ All packages installed!')"
```

### **Test 2: Check XGBoost (Optional)**

```bash
python -c "import xgboost; print('✓ XGBoost works!')"
```

If XGBoost fails, that's okay - Random Forest will work fine!

### **Test 3: Check Jupyter**

```bash
jupyter notebook
```

Browser should open with Jupyter interface.

---

## 🎯 **Quick Reference**

### **Package Versions We're Using:**

| Package | Version | Purpose |
|---------|---------|---------|
| pandas | 2.0+ | Data manipulation |
| numpy | 1.24+ | Numerical operations |
| matplotlib | 3.7+ | Plotting |
| seaborn | 0.12+ | Beautiful plots |
| scikit-learn | 1.3+ | Machine learning |
| xgboost | 2.0+ | Advanced ML (optional) |
| jupyter | 1.0+ | Notebook interface |

---

## 🚦 **Step-by-Step for Complete Beginners**

### **Never used Python before? Start here:**

#### **1. Install Python**

- Go to: https://www.python.org/downloads/
- Download: Python 3.11 (or 3.10, 3.9) — **make sure it's 64-bit!**
- **IMPORTANT:** Check "Add Python to PATH" during installation!

#### **2. Verify Installation**

Open Terminal/Command Prompt:
```bash
python --version
```

Should show: `Python 3.11.x` or similar

#### **3. Install Packages**

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

#### **4. Try XGBoost (Optional)**

```bash
pip install xgboost
```

If this fails, don't worry! Skip it.

#### **5. Download Project Files**

Get from Google Drive or email

#### **6. Run Jupyter**

```bash
cd path/to/project
jupyter notebook
```

#### **7. Open Notebook**

Click on `Housing_Analysis_EDA.ipynb`

#### **8. Run All**

**Cell → Run All**

---

## 💡 **Tips**

### **For Windows Users:**
- Use Command Prompt (cmd) or PowerShell
- If pip doesn't work, use: `python -m pip install ...`

### **For Mac Users:**
- Use Terminal
- If pip doesn't work, use: `pip3 install ...`
- For XGBoost issues: `brew install libomp`
- Make sure Python is **64-bit**: `python3 -c "import struct; print(struct.calcsize('P') * 8, 'bit')"`

### **For Anaconda Users:**
- Always use `conda install` when possible
- Activate environment: `conda activate housing`

---

## 🆘 **Still Having Issues?**

### **Common Solutions:**

1. **Restart terminal/command prompt** after installing Python
2. **Restart computer** if PATH issues
3. **Use virtual environment:**
   ```bash
   python -m venv housing_env
   source housing_env/bin/activate  # Mac/Linux
   housing_env\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

### **Get Help:**

If you're stuck:
1. Take a screenshot of the error
2. Share in team group chat
3. Include: OS (Windows/Mac/Linux), Python version, exact error message

---

## 📞 **Contact**

**Chloe (EDA & Modeling):**
- Email: chloelee.lee@uleth.ca
- Best for: Python/Jupyter/ML questions

**James (Data Integration):**
- Best for: Data file questions

---

## 🎓 **For Presentation (Vergil/Ryan):**

You only need to install if you want to:
- Run notebooks yourself
- Regenerate visualizations
- Modify code

Otherwise:
- Use the CSV files we provide
- Use the PNG visualizations in `03_Results/visualization/`

---

## ⏱️ **Time Estimate**

- Method 1 (requirements.txt): **5 minutes**
- Method 2 (manual): **10 minutes**
- Method 3 (Anaconda): **15 minutes**
- Troubleshooting: **varies** (0-30 minutes)

**Most people finish in under 10 minutes!**

---

## 🎯 **Success Checklist**

- [ ] Python 3.9+ (64-bit) installed
- [ ] All packages installed (no import errors)
- [ ] Jupyter notebook opens in browser
- [ ] Can run cells in notebooks
- [ ] Visualizations appear
- [ ] CSV files load successfully

---

## 📚 **Additional Resources**

### **Learning Python:**
- Python.org: https://www.python.org/
- Jupyter docs: https://jupyter.org/

### **Package Documentation:**
- pandas: https://pandas.pydata.org/
- scikit-learn: https://scikit-learn.org/
- matplotlib: https://matplotlib.org/

---

**Good luck! If you have any issues, reach out to the team!** 🚀

---

**Last Updated:** February 10, 2026  
**Version:** 1.1  
**Created by:** Chloe Lee
