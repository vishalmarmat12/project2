# ⚙️ Step-by-Step Installation & Setup Guide

This guide provides instructions to clone, configure, and execute the entire data analytics portfolio pipeline from scratch.

---

## 1. Prerequisites
- **Operating System**: Windows, macOS, or Linux
- **Python Version**: Python 3.10+ (tested on Python 3.14)
- **Git**: Installed and configured
- **RAM**: Minimum 4 GB recommended

---

## 2. Clone the Repository
```bash
git clone https://github.com/vishalmarmat12/project2.git
cd project2
```

---

## 3. Virtual Environment Setup
It is best practice to install dependencies inside an isolated virtual environment:

### On Windows (Command Prompt or PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### On macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies
Install all required analytical and reporting packages:
```bash
pip install -r requirements.txt
```

Verify that the core dependencies are successfully installed:
```bash
python -c "import pandas, matplotlib, seaborn, scipy, reportlab, pptx, nbformat; print('All dependencies verified successfully!')"
```

---

## 5. Running the Master Pipeline
To execute the complete end-to-end pipeline (data validation, cleaning, statistical analysis, generation of 20+ charts, 6 PDF reports, and presentation deck):
```bash
python run_full_portfolio_pipeline.py
```

### Output Directories Populated:
- `visualizations/`: High-resolution figures saved as PNGs across `project1` through `project5`.
- `reports/`: 5 Individual project PDF reports + 1 master portfolio summary PDF.
- `presentation/`: PowerPoint slide deck (`portfolio_presentation.pptx`).

---

## 6. Running Interactive Jupyter Notebooks
To interactively explore the notebooks:
```bash
jupyter notebook notebooks/
```
Or launch JupyterLab:
```bash
jupyter lab
```

---

## 7. Running the Automated Test Suite
To execute the automated validation tests:
```bash
python -m unittest tests/test_pipeline.py
```
All tests should pass with `OK`.
