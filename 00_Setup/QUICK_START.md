# Quick Start - 5 Minute Setup
## CPSC 4310 Housing Project

---

## 🚀 **Install Everything in 3 Steps**

### **Step 1: Install Python**
- Download: https://www.python.org/downloads/
- Get Python 3.9 or higher
- ✅ Check "Add to PATH" during install

### **Step 2: Install Packages**

Open Terminal/Command Prompt and run:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost jupyter
```

**Mac Users:** If XGBoost fails:
```bash
brew install libomp
pip install xgboost
```

**Still fails?** Skip XGBoost - Random Forest works great!

### **Step 3: Run Jupyter**

```bash
jupyter notebook
```

---

## ✅ **Verify Installation**

In Jupyter, create a new cell and run:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
print("✓ Everything works!")
```

No errors? **You're done!** 🎉

---

## 🆘 **Problems?**

### **"pip not found"**
```bash
python -m pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### **Import errors after install**
- Restart Jupyter: **Kernel → Restart**

### **Still stuck?**
- See `INSTALLATION_GUIDE.md` for detailed help
- Contact Chloe

---

**That's it!** Now open any `.ipynb` file and click **Cell → Run All**
