# 🌟 Multi-Domain Data Analysis Portfolio: Executive Portfolio Overview
**Author**: Vishal Parmar  
**Repository**: [github.com/vishalmarmat12/project2](https://github.com/vishalmarmat12/project2)  
**Domain Coverage**: Retail, Education, Meteorology, Healthcare, Real Estate Finance  
**Quality Standards Checklist**: 100% Complete & Verified

---

## 🎯 Executive Summary
The **Multi-Domain Data Analysis Portfolio** is a professional collection of five end-to-end data science and business analytics projects. Each project simulates a high-impact consulting engagement, translating raw operational data into statistical findings, publication-grade visualizations, and actionable executive recommendations.

The portfolio encompasses over **5,300 audited records**, **20 publication-quality visualizations (300 DPI)**, **5 dedicated multi-page PDF reports + 1 master summary PDF**, **5 complete interactive Jupyter notebooks**, an executive **PowerPoint presentation deck**, and a modular, production-grade Python package architecture.

---

## 📊 Summary of Projects

| # | Project Name | Domain | Dataset Scope | Key Statistical Findings | Primary Business / Operational Recommendation |
|:---:|---|---|---|---|---|
| **1** | **Supermarket Sales & Retail Analytics** | Retail & E-Commerce | 2,000 Invoices (Yangon, Mandalay, Naypyitaw) | • $645.8K Total Sales<br>• Weekend 5-8 PM generates 42% volume<br>• Digital channels (cards/wallets) = 67% | Reallocate 35% of cashier shifts to weekend evening slots; launch targeted e-wallet cashback campaigns to drive loyalty sign-ups. |
| **2** | **Student Academic Performance** | Education & Learning Sciences | 1,000 Student Records across 3 Subjects | • 82.4% Overall Pass Rate<br>• Attendance correlation $r = +0.52$<br>• Test prep provides +8.5 pt score boost | Deploy automated guardian SMS alerts at 3 absences; provide universal subsidized test prep for students on reduced lunch programs. |
| **3** | **Meteorological Climate Study** | Meteorology & Environmental Sciences | 1,000 Observation Days across 3 Stations | • 55% of precipitation arrives in summer storms<br>• Pressure <1010 hPa & Humidity >70% predicts rain (78.2%) | Establish pre-summer storm drain desilting schedules; connect barometric drop triggers to municipal transit rerouting advisories. |
| **4** | **Healthcare COVID-19 Epidemiology** | Healthcare & Public Health | 1,000 Regional Surveillance Records | • Hospitalizations lag case surges by 9-12 days<br>• Vaccine-mortality correlation $r = -0.74$<br>• 78.4% peak ICU bed burden | Implement surge clinical nurse staffing 7 days after community positivity increases; enact inter-hospital patient diversion protocols. |
| **5** | **Real Estate Econometric Valuation** | Finance & Real Estate Econometrics | 300 Property Transactions across 3 Locations | • Living area explains 63.8% of price ($R^2=0.638$)<br>• City Center +84.2% premium<br>• Depreciation floor at 25 yrs | Focus capital on City Center infill multi-unit apartments; re-engineer floorplans to eliminate unusable dead corridor square footage. |

---

## 🛠️ Technical Implementation & Architecture

```
                               ┌─────────────────────────────────┐
                               │   Domain CSV Datasets (data/)   │
                               └────────────────┬────────────────┘
                                                │
                                                ▼
                               ┌─────────────────────────────────┐
                               │  Data Loader & Quality Audits   │
                               │      (src/data_loader.py)       │
                               └────────────────┬────────────────┘
                                                │
                                                ▼
                               ┌─────────────────────────────────┐
                               │ Cleaners & Feature Engineering  │
                               │       (src/cleaners.py)         │
                               └────────────────┬────────────────┘
                                                │
                     ┌──────────────────────────┴──────────────────────────┐
                     ▼                                                     ▼
     ┌───────────────────────────────┐                     ┌───────────────────────────────┐
     │  Statistical Analysis Engine  │                     │     Visualization Engine      │
     │      (src/analyzers.py)       │                     │     (src/visualizers.py)      │
     └───────────────┬───────────────┘                     └───────────────┬───────────────┘
                     │                                                     │
                     └──────────────────────────┬──────────────────────────┘
                                                │
                                                ▼
                               ┌─────────────────────────────────┐
                               │  ReportLab Executive PDF Engine │
                               │   (src/report_generator.py)     │
                               └────────────────┬────────────────┘
                                                │
            ┌───────────────────────────────────┼───────────────────────────────────┐
            ▼                                   ▼                                   ▼
┌───────────────────────┐           ┌───────────────────────┐           ┌───────────────────────┐
│ 5 Interactive .ipynb  │           │  6 Executive PDF Docs │           │ PowerPoint Deck (.pptx│
│      Notebooks        │           │      in reports/      │           │    in presentation/   │
└───────────────────────┘           └───────────────────────┘           └───────────────────────┘
```

---

## 📈 Cross-Domain Key Analytical Insights

### 1. The Impact of Human Behavioral Dynamics
Across retail and education, human habit and discipline govern primary outcomes. In retail, consumer shopping velocity predictably concentrates into weekend twilight hours, making labor deployment efficiency the chief lever for revenue maximization. In education, student attendance demonstrates an almost irreversible impact on academic survival ($r = +0.52$), where failing to attend classes precipitates failure regardless of socioeconomic backing.

### 2. Time-Lagged Systemic Strains
Both meteorological and healthcare studies highlighted the critical nature of time-lagged variables. In healthcare, peak hospitalization and intensive care bed demand lagged active infection surges by 9 to 12 days. In meteorology, dropping barometric pressure and rising afternoon humidity reliably preceded precipitation events by 12 to 18 hours. Predictive early-warning systems built on these lead times eliminate operational surprises.

### 3. Hedonic Elasticity & Structural Depreciation
The real estate econometric analysis verified that space ($Area$) remains the dominant pricing driver ($R^2 = 0.638$), but location creates an insurmountable value multiplier (+84.2% for City Center). Asset depreciation operates along a non-linear decay curve that plateaus around year 25, establishing an empirical foundation for value-add renovation arbitrage.

---

## 📦 Directory Structure & Deliverable Navigation

- **`data/`**: Source CSV files (`supermarket_sales.csv`, `student_performance.csv`, `weather_data.csv`, `healthcare_covid_trends.csv`, `real_estate_valuation.csv`).
- **`src/`**: Modular Python functions for data loading, cleaning, analysis, visualization, and PDF generation.
- **`notebooks/`**: 5 complete Jupyter notebooks featuring rich markdown, exploratory code, and statistical charts.
- **`visualizations/`**: 20 high-resolution charts organized across `project1` to `project5`.
- **`reports/`**: 5 individual project PDF reports and 1 master portfolio summary PDF report.
- **`presentation/`**: PowerPoint presentation (`portfolio_presentation.pptx`) and speaker notes markdown.
- **`docs/`**: Comprehensive guides covering architecture, data dictionaries, business recommendations, test evidence, and installation instructions.
- **`tests/`**: Unit test suite (`test_pipeline.py`) verifying pipeline integrity.
