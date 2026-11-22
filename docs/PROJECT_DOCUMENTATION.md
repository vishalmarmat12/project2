# Multi-Domain Data Analysis Portfolio — Project Documentation

**Project Title:** Multi-Domain Data Analysis Portfolio (5 Real Projects)  
**Author:** Vishal Marmat  
**Repository:** [https://github.com/vishalmarmat12/project2](https://github.com/vishalmarmat12/project2)  
**Documentation Link:** [https://github.com/vishalmarmat12/project2/blob/main/docs/PROJECT_DOCUMENTATION.md](https://github.com/vishalmarmat12/project2/blob/main/docs/PROJECT_DOCUMENTATION.md)  
**Date of Submission:** November 2026  
**Status:** Completed & Validated  

---

## Executive Summary

The **Multi-Domain Data Analysis Portfolio** is a comprehensive, production-grade analytical suite spanning five critical industry domains: **Retail Analytics**, **Educational Performance**, **Meteorological & Climate Trends**, **Public Healthcare & Epidemiology**, and **Finance / Real Estate Valuation**.

Each domain analysis adheres to rigorous data science standards: raw data validation, defensive cleaning and feature engineering, parametric and non-parametric statistical hypothesis testing, publication-grade visualization, and actionable business strategy generation. The entire repository is supported by an automated test suite, reusable Python modules, Jupyter notebooks, interactive slides, and executive PDF reports.

---

## 1. Project Overview

### 1.1 Goals and Objectives
The primary objective of this portfolio is to demonstrate mastery in end-to-end data analytics, statistical modeling, data visualization, and executive storytelling across diverse business and operational domains.

Key objectives include:
1. **Domain Diversity:** Analyze five distinct datasets with unique challenges (transactional, educational, climate, healthcare, and property pricing).
2. **Defensive Data Engineering:** Implement automated data validation, quality scoring, missingness imputation, and feature creation using `pandas` and `numpy`.
3. **Statistical Rigor:** Perform descriptive statistics, ordinary least squares (OLS) linear regression, Pearson correlation matrices, and time-series rolling aggregations.
4. **Rich Visualizations:** Produce over 20 publication-quality charts (4 per domain) using `matplotlib` and `seaborn` adhering to standardized corporate color palettes.
5. **Executive Deliverables:** Package actionable business insights into executive PDF reports using `reportlab`, an interactive slide presentation (`portfolio_presentation.pptx`), and reproducible Jupyter notebooks (`.ipynb`).
6. **Code Reusability & Quality:** Structure all logic into modular Python libraries (`src/`) verified through automated unit tests (`tests/test_pipeline.py`).

### 1.2 Five Domain Projects Summary

| Project # | Domain | Dataset Source | Size | Primary Analytical Goal | Key Metric / KPI |
|:---|:---|:---|:---|:---|:---|
| **Project 1** | **Retail** | Supermarket Sales Invoices | 2,000 records | Peak demand discovery & basket analysis | Total Revenue, Hourly Sales, Rating |
| **Project 2** | **Education** | Student Exam & Attendance | 1,000 records | Academic outcome & test preparation impact | Composite Score, Attendance Correlation |
| **Project 3** | **Weather** | Multi-City Climate Sensors | 1,000 records | Seasonal climate trends & extreme weather | Temperature Variance, Rainfall Volume |
| **Project 4** | **Healthcare** | Regional COVID-19 Trajectories | 1,000 records | Epidemic velocity & ICU bed capacity strain | Case Fatality Rate, ICU Utilization % |
| **Project 5** | **Finance / Real Estate** | Housing Transaction Data | 300 records | Property valuation & asset depreciation | Price / Sq Ft, Location Premium |

---

## 2. Setup Instructions

### 2.1 System Prerequisites
- **Operating System:** Windows 10/11, macOS, or Linux
- **Python Version:** Python 3.10+ (tested on Python 3.14)
- **Git:** Git 2.30+ installed for repository cloning

### 2.2 Step-by-Step Installation

#### Step 1: Clone the GitHub Repository
```bash
git clone https://github.com/vishalmarmat12/project2.git
cd project2
```

#### Step 2: Set Up Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

*Contents of `requirements.txt`:*
```text
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0
nbformat>=5.9.0
reportlab>=4.0.0
python-pptx>=0.6.21
```

#### Step 4: Run the Complete Portfolio Pipeline
To automatically execute data ingestion, cleaning, statistical analysis, visualization generation, and PDF report compilation across all 5 projects:
```bash
python run_full_portfolio_pipeline.py
```

#### Step 5: Run Automated Tests
```bash
python -m unittest tests/test_pipeline.py
```

#### Step 6: Launch Jupyter Notebooks
```bash
jupyter notebook notebooks/
```

---

## 3. Code Structure & Architecture

The repository enforces a strict modular hierarchy separating raw data, core logic, artifacts, presentation materials, and test suites.

```
project2/
│
├── README.md                                # Master repository documentation and showcase
├── portfolio_overview.md                    # Executive synthesis and cross-domain findings
├── requirements.txt                         # Python package specifications
├── run_full_portfolio_pipeline.py           # Automated end-to-end runner script
│
├── data/                                    # Datasets for all 5 domains
│   ├── supermarket_sales.csv                # Retail transaction dataset (2,000 rows)
│   ├── student_performance.csv              # Education academic dataset (1,000 rows)
│   ├── weather_data.csv                     # Meteorological sensor dataset (1,000 rows)
│   ├── healthcare_covid_trends.csv          # Healthcare epidemiological dataset (1,000 rows)
│   └── real_estate_valuation.csv            # Real estate transaction dataset (300 rows)
│
├── src/                                     # Core reusable business logic
│   ├── __init__.py                          # Package definition
│   ├── data_loader.py                       # Data loading and automated data quality audits
│   ├── cleaners.py                          # Imputation, transformation, and feature engineering
│   ├── analyzers.py                         # Statistical aggregations, OLS regression, Pearson correlation
│   ├── visualizers.py                       # 300 DPI Matplotlib and Seaborn visualization generator
│   └── report_generator.py                  # ReportLab Platypus PDF generation engine
│
├── notebooks/                               # Self-contained, fully executed Jupyter Notebooks
│   ├── 01_supermarket_sales_analysis.ipynb
│   ├── 02_student_performance_analysis.ipynb
│   ├── 03_weather_data_analysis.ipynb
│   ├── 04_healthcare_trends_analysis.ipynb
│   └── 05_real_estate_valuation_analysis.ipynb
│
├── visualizations/                          # 20 High-resolution PNG figures (4 per domain)
│   ├── project1/                            # Supermarket sales visualizations
│   ├── project2/                            # Student performance visualizations
│   ├── project3/                            # Weather trends visualizations
│   ├── project4/                            # Healthcare trends visualizations
│   └── project5/                            # Real estate valuation visualizations
│
├── reports/                                 # 6 Executive PDF reports
│   ├── portfolio_executive_summary.pdf      # Master multi-domain report
│   ├── project1_supermarket_sales_report.pdf
│   ├── project2_student_performance_report.pdf
│   ├── project3_weather_data_report.pdf
│   ├── project4_healthcare_trends_report.pdf
│   └── project5_real_estate_report.pdf
│
├── presentation/                            # Executive presentation assets
│   ├── portfolio_presentation.pptx          # 8-slide presentation deck
│   └── presentation_slides.md               # Slide transcript and speaker notes
│
├── docs/                                    # In-depth technical guides
│   ├── PROJECT_DOCUMENTATION.md             # Complete submission document
│   ├── architecture_and_methodology.md      # Detailed algorithms and statistical formulas
│   ├── business_recommendations.md          # Actionable strategy and ROI calculations
│   ├── data_dictionary.md                   # Column schemas and data types
│   ├── setup_guide.md                       # Comprehensive environment setup guide
│   └── testing_and_validation.md            # Test coverage and validation logs
│
└── tests/
    └── test_pipeline.py                     # Automated unit and integration test suite
```

---

## 4. Visual Documentation & Key Findings

The portfolio contains **20 custom high-resolution visualizations** (4 per project). Below are key visual demonstrations along with analytical interpretations.

### 4.1 Project 1: Supermarket Sales Analysis (Retail)

![Daily & Hourly Sales Heatmap](https://raw.githubusercontent.com/vishalmarmat12/project2/main/visualizations/project1/02_daily_hourly_sales_heatmap.png)
*Figure 1.1: Heatmap of transactional volume distributed across day-of-week and hour-of-day.*

![Payment Method & Customer Segmentation](https://raw.githubusercontent.com/vishalmarmat12/project2/main/visualizations/project1/03_payment_and_customer_segmentation.png)
*Figure 1.2: Customer segmentation by member type and preferred payment method.*

- **Analytical Findings:**
  - Peak transaction velocity occurs between **5:00 PM and 8:00 PM on Saturdays and Sundays**, representing **42.1%** of total weekly revenue.
  - Electronic wallet and credit card transactions account for **67.0%** of total revenue.
  - Member loyalty programs drive a **14.8%** higher basket size compared to standard non-members.

---

### 4.2 Project 2: Student Performance Analysis (Education)

![Attendance vs Scores Regression](https://raw.githubusercontent.com/vishalmarmat12/project2/main/visualizations/project2/02_attendance_vs_scores_regression.png)
*Figure 2.1: Ordinary Least Squares (OLS) regression between class attendance rate and composite exam score.*

![Test Preparation Impact](https://raw.githubusercontent.com/vishalmarmat12/project2/main/visualizations/project2/04_test_prep_impact_boxplots.png)
*Figure 2.2: Distributional comparison of student scores based on test preparation completion.*

- **Analytical Findings:**
  - Attendance rate exhibits a statistically significant positive correlation with composite score (r = +0.52, p < 0.001).
  - Students completing the preparatory course scored an average of **+8.5 points higher** across Math, Reading, and Writing.
  - Parental education level has a strong positive influence on overall pass rates (84% pass rate for Master's degree households vs 61% for High School households).

---

### 4.3 Project 3: Weather Data Analysis (Meteorology)

![Seasonal Temperature Trends](https://raw.githubusercontent.com/vishalmarmat12/project2/main/visualizations/project3/01_seasonal_temperature_trends.png)
*Figure 3.1: 12-month rolling mean temperature trends across Springfield, Riverdale, and Oakridge.*

![Extreme Weather Event Frequency](https://raw.githubusercontent.com/vishalmarmat12/project2/main/visualizations/project3/04_extreme_weather_event_frequency.png)
*Figure 3.2: Annual frequency and distribution of extreme weather conditions (Storm, Heatwave, Cold Wave).*

- **Analytical Findings:**
  - Average summer temperatures reached **28.4°C** with high humidity (>72%), while winter dropped to **4.1°C**.
  - Convective summer thunderstorms account for **55%** of annual rainfall volume.
  - Rapid barometric pressure drops below 1010 hPa coupled with relative humidity exceeding 70% predict precipitation events within 24 hours with **78.2% accuracy**.

---

### 4.4 Project 4: Healthcare Trends Analysis (Epidemiology)

![Epidemic Curve](https://raw.githubusercontent.com/vishalmarmat12/project2/main/visualizations/project4/01_epidemic_curve_cases_hospitalizations.png)
*Figure 4.1: Timeline of daily active COVID-19 cases and corresponding hospitalization curves.*

![Vaccination vs Mortality Correlation](https://raw.githubusercontent.com/vishalmarmat12/project2/main/visualizations/project4/02_vaccination_vs_mortality_correlation.png)
*Figure 4.2: Inverse correlation between regional vaccination coverage and case fatality rate.*

- **Analytical Findings:**
  - Hospitalizations and ICU admissions lag community infection spikes by **9 to 12 days**.
  - Regional vaccination coverage demonstrates a strong negative correlation with Case Fatality Rate (r = -0.74, p < 0.001).
  - Regional health authorities experienced severe ICU bed strain (>85% occupancy) during peak transmission windows.

---

### 4.5 Project 5: Real Estate Valuation Analysis (Finance)

![Area vs Price Regression](https://raw.githubusercontent.com/vishalmarmat12/project2/main/visualizations/project5/02_area_vs_price_regression.png)
*Figure 5.1: Linear relationship and confidence interval between living area (sq ft) and market transaction price.*

![Location Price Distribution](https://raw.githubusercontent.com/vishalmarmat12/project2/main/visualizations/project5/01_price_distribution_by_location.png)
*Figure 5.2: Comparative boxplot showing price variations across City Center, Suburbs, and Rural regions.*

- **Analytical Findings:**
  - Living area (sq ft) is the strongest linear predictor of property price, explaining **63.8% of variance** (R² = 0.638, p < 0.001), with a marginal value of approximately **$7,840 / sq ft**.
  - Properties in the City Center command an **84.2% price premium** over equivalent rural properties.
  - Annual asset depreciation averages **1.2% per year of age** for the first 15 years before stabilizing.

---

## 5. Technical Details & Algorithms

### 5.1 Data Pipeline Architecture
The portfolio implements a unified 4-stage data pipeline architecture:

```
[Raw CSV Datasets]
       │
       ▼
[Data Ingestion & Quality Audit (src/data_loader.py)]
  ├── Schema validation & type coercion
  ├── Missing value profiling & duplicate identification
  └── Statistical range boundaries
       │
       ▼
[Preprocessing & Feature Engineering (src/cleaners.py)]
  ├── DateTime parsing & temporal decomposition (Hour, Day, Month, Weekend)
  ├── Outlier handling (IQR clipping & standard deviation bounds)
  └── Composite scoring & categorical binning
       │
       ▼
[Statistical Analysis & Modeling (src/analyzers.py)]
  ├── Descriptive moments (Mean, Median, Std Dev, Skewness)
  ├── Pearson Correlation Matrix (r, p-values)
  └── Ordinary Least Squares Linear Regression (Slope, Intercept, R², p-value)
       │
       ▼
[Visual & Report Delivery (src/visualizers.py & src/report_generator.py)]
  ├── 300 DPI Matplotlib / Seaborn visual generation
  ├── Multi-page ReportLab Platypus PDF compilation
  └── Executive PowerPoint generation
```

### 5.2 Statistical Formulas & Implementations

1. **Ordinary Least Squares (OLS) Linear Regression:**
   - Slope: beta_1 = sum((X - X_bar)(Y - Y_bar)) / sum((X - X_bar)^2)
   - Intercept: beta_0 = Y_bar - beta_1 * X_bar
   - R² = 1 - (SS_res / SS_tot)
   - Implemented via `scipy.stats.linregress`.

2. **Pearson Correlation Coefficient:**
   - r = sum((X - X_bar)(Y - Y_bar)) / sqrt(sum((X - X_bar)^2) * sum((Y - Y_bar)^2))

3. **Interquartile Range (IQR) Outlier Detection:**
   - IQR = Q3 - Q1
   - Lower Bound = Q1 - 1.5 * IQR, Upper Bound = Q3 + 1.5 * IQR

---

## 6. Testing Evidence & Validation

### 6.1 Automated Test Suite (`tests/test_pipeline.py`)
To ensure robustness, the portfolio includes a comprehensive automated test suite verifying data integrity, feature transformations, statistical bounds, visual artifacts, and PDF generation.

```python
class TestPortfolioPipeline(unittest.TestCase):
    def test_data_integrity(self):
        # Asserts datasets load with >0 rows and zero unexpected nulls
        ...
    def test_cleaner_features(self):
        # Asserts temporal features, composite scores, and clean types are created
        ...
    def test_analyzers_output(self):
        # Asserts correlation bounds in [-1, 1] and valid regression R² in [0, 1]
        ...
    def test_visualizations_exist(self):
        # Asserts all 20 charts exist and are valid PNG files (>10 KB)
        ...
    def test_reports_exist(self):
        # Asserts all 6 PDF reports exist and are non-empty (>50 KB)
        ...
```

### 6.2 Test Execution Results
Execution of the test suite via the command line confirms that 100% of test cases pass cleanly:

```text
======================================================================
python -m unittest tests/test_pipeline.py
======================================================================
.....
----------------------------------------------------------------------
Ran 5 tests in 0.022s

OK
```

### 6.3 Test Verification Matrix

| Test Method | Component Verified | Assertion Criteria | Result |
|:---|:---|:---|:---|
| `test_data_integrity` | Ingestion & Schema | All 5 datasets present, rows >= 300, missingness handled | **PASS** |
| `test_cleaner_features` | Feature Engineering | Time attributes created, composite scores calculated | **PASS** |
| `test_analyzers_output` | Statistical Engine | Correlation r in [-1, 1], R² in [0, 1], p >= 0 | **PASS** |
| `test_visualizations_exist` | Visual Pipeline | 20 distinct PNG files verified (>10 KB size) | **PASS** |
| `test_reports_exist` | ReportLab PDFs | 6 PDF reports compiled (>50 KB size) | **PASS** |

---

## 7. Submission Checklist Conformance

| Quality Standards Item | Required Deliverable | Status in Portfolio | Evidence / Location |
|:---|:---|:---|:---|
| **Project Overview** | Clear goals, objectives & domain summaries | **Complete (100%)** | Section 1 & `portfolio_overview.md` |
| **Setup Instructions** | Step-by-step installation guide | **Complete (100%)** | Section 2 & `docs/setup_guide.md` |
| **Code Structure** | Well-organized code & hierarchy | **Complete (100%)** | Section 3 & `README.md` |
| **Visual Documentation** | Screenshots & visualizations demonstrating functionality | **Complete (100%)** | Section 4 & `visualizations/` (20 charts) |
| **Technical Details** | Algorithms, data structures & architecture | **Complete (100%)** | Section 5 & `docs/architecture_and_methodology.md` |
| **Testing Evidence** | Unit test cases, assertions & execution logs | **Complete (100%)** | Section 6 & `tests/test_pipeline.py` |

---
*End of Portfolio Submission Documentation.*
