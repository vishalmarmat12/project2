# 🏗️ Architecture & Analytical Methodology

## 1. System Architecture Overview
The **Multi-Domain Data Analysis Portfolio** is engineered as a modular, reproducible data analytics framework. The repository adheres to enterprise software engineering standards, separating data ingestion, cleaning, statistical analysis, visualization generation, and automated report compilation.

```
project_root/
├── data/                       # Ingested and generated domain datasets (CSV)
│   ├── supermarket_sales.csv
│   ├── student_performance.csv
│   ├── weather_data.csv
│   ├── healthcare_covid_trends.csv
│   └── real_estate_valuation.csv
├── src/                        # Production-ready Python modules
│   ├── __init__.py
│   ├── data_loader.py          # Data ingestion and schema validation
│   ├── cleaners.py             # Feature engineering and cleaning pipelines
│   ├── analyzers.py            # Statistical computation engine
│   ├── visualizers.py          # Chart generation & visual styling
│   └── report_generator.py     # Automated PDF report compilation via ReportLab
├── notebooks/                  # Interactive Jupyter exploratory notebooks
│   ├── 01_supermarket_sales_analysis.ipynb
│   ├── 02_student_performance_analysis.ipynb
│   ├── 03_weather_data_analysis.ipynb
│   ├── 04_healthcare_trends_analysis.ipynb
│   └── 05_real_estate_valuation_analysis.ipynb
├── visualizations/             # High-resolution (300 DPI) publication graphics
│   ├── project1/               # Retail visualizations
│   ├── project2/               # Education visualizations
│   ├── project3/               # Meteorology visualizations
│   ├── project4/               # Healthcare visualizations
│   └── project5/               # Real estate visualizations
├── reports/                    # Executive multi-page PDF reports
│   ├── project1_supermarket_sales_report.pdf
│   ├── project2_student_performance_report.pdf
│   ├── project3_weather_data_report.pdf
│   ├── project4_healthcare_trends_report.pdf
│   ├── project5_real_estate_report.pdf
│   └── portfolio_executive_summary.pdf
├── presentation/               # Executive slide deck
│   ├── portfolio_presentation.pptx
│   └── presentation_slides.md
├── docs/                       # Technical documentation & guides
│   ├── architecture_and_methodology.md
│   ├── data_dictionary.md
│   ├── business_recommendations.md
│   ├── testing_and_validation.md
│   └── setup_guide.md
├── portfolio_overview.md       # High-level portfolio executive summary
├── requirements.txt            # Environment package dependencies
└── README.md                   # Main GitHub project presentation
```

---

## 2. Analytical Methodology

### A. Data Ingestion & Quality Auditing (`src/data_loader.py`)
1. **Schema Integrity**: Verifies presence of mandatory columns, correct types, and structural shape.
2. **Missing Value Auditing**: Computes per-column null percentages and evaluates missing data mechanisms (MCAR vs MAR).
3. **Duplicate Detection**: Identifies and removes duplicate entity records.
4. **Memory Profiling**: Measures in-memory DataFrame footprints for optimization.

### B. Preprocessing & Feature Engineering (`src/cleaners.py`)
1. **Temporal Discretization**: Converts ISO strings to native datetime objects; extracts Year, Month, Day of Week, and diurnal time slots.
2. **Standardization & Bounds Checking**: Enforces theoretical limits (e.g., student grades in $[0, 100]$, relative humidity in $[0, 100\%]$).
3. **Derived Economics**: Computes unit economics such as Price per Square Foot, Profit Margins, Case Fatality Rates, and ICU Pressure Indices.

### C. Statistical Methods & Modeling Engine (`src/analyzers.py`)
1. **Descriptive Statistics**: Calculates parametric (mean, standard deviation) and non-parametric (median, interquartile range) metrics.
2. **Correlation Analysis**: Applies Pearson's product-moment correlation coefficient ($r$) for linear relationships and Spearman's rank correlation for monotonic ordinal associations.
3. **Hedonic Linear Regression**: Fits Ordinary Least Squares (OLS) models for valuation ($Price = \beta_0 + \beta_1 Area + \epsilon$) reporting $R^2$, slope coefficients, and p-values ($p < 0.001$).
4. **Hypothesis Testing**: Conducts two-sample t-tests and ANOVA to evaluate categorical significance (e.g., test preparation impact across demographic groups).

### D. Visual Storytelling (`src/visualizers.py`)
- Standardized color palettes (`whitegrid`, `deep`, `Set2`, `Spectral`).
- Multi-axis charts (twin-x) for lagging healthcare variables.
- Correlation trendlines with confidence intervals.
- Heatmaps with formatted numeric overlays for multi-variable interactions.
- All figures rendered and exported at **300 DPI** PNG format.

### E. Automated PDF Compilation (`src/report_generator.py`)
- Employs **ReportLab Platypus** layout engine with dynamic two-pass canvas numbering (`NumberedCanvas`).
- Embeds metadata banners, KPI tables, high-resolution figures, and strategic recommendation matrix tables.
