# 📖 Data Dictionary & Schema Documentation

This document describes the schema, data types, definitions, and valid constraints across all 5 domain datasets.

---

## 1. Project 1: Supermarket Sales Dataset (`data/supermarket_sales.csv`)
- **Total Records**: 2,000 transactions
- **Timeframe**: Full Year 2023
- **Coverage**: 3 Branches (A, B, C) across Yangon, Mandalay, and Naypyitaw

| Column Name | Data Type | Description | Allowed Values / Range |
|---|---|---|---|
| `Invoice_ID` | String | Unique transaction alphanumeric identifier | e.g., `INV000001` - `INV002000` |
| `Branch` | String | Retail store branch code | `A`, `B`, `C` |
| `City` | String | Geographical metropolitan location | `Yangon`, `Mandalay`, `Naypyitaw` |
| `Customer_Type` | String | Customer loyalty membership tier | `Member`, `Normal` |
| `Gender` | String | Customer biological gender | `Female`, `Male` |
| `Product_Line` | String | Commercial product merchandise category | `Electronic Accessories`, `Fashion Accessories`, `Food & Beverages`, `Health & Beauty`, `Home & Lifestyle`, `Sports & Travel` |
| `Unit_Price` | Float | Price per single item unit (USD) | $10.00 - $100.00 |
| `Quantity` | Integer | Number of units purchased | 1 - 10 |
| `Tax` | Float | 5% Value Added Tax (VAT) | $1.00 - $50.00 |
| `Total` | Float | Gross bill total including tax (USD) | $10.00 - $1,050.00 |
| `Date` | String | Date of transaction | `YYYY-MM-DD` |
| `Time` | String | Time of transaction (24-hour clock) | `HH:MM` |
| `Payment` | String | Payment settlement method | `Cash`, `Credit card`, `Ewallet` |
| `Rating` | Float | Customer checkout satisfaction score | 4.0 - 10.0 |

---

## 2. Project 2: Student Academic Performance (`data/student_performance.csv`)
- **Total Records**: 1,000 students
- **Timeframe**: Academic Year Cycle

| Column Name | Data Type | Description | Allowed Values / Range |
|---|---|---|---|
| `Student_ID` | String | Unique student tracking identifier | `STU0001` - `STU1000` |
| `Gender` | String | Student gender identity | `Female`, `Male` |
| `Ethnicity` | String | Anonymized demographic cohort | `Group A`, `Group B`, `Group C`, `Group D`, `Group E` |
| `Parental_Education` | String | Highest education level completed by parent | `Some High School`, `High School`, `Some College`, `Associate's Degree`, `Bachelor's Degree`, `Master's Degree` |
| `Lunch_Type` | String | Socioeconomic school meal subsidy tier | `Standard`, `Free/Reduced` |
| `Test_Prep_Course` | String | Formal exam preparation completion | `None`, `Completed` |
| `Attendance_Rate` | Float | Percentage of enrolled classes attended | 55.0% - 100.0% |
| `Study_Hours_Weekly` | Integer | Self-reported weekly study hours | 2 - 35 hours |
| `Math_Score` | Integer | Standardized Mathematics exam score | 0 - 100 points |
| `Reading_Score` | Integer | Standardized Reading exam score | 0 - 100 points |
| `Writing_Score` | Integer | Standardized Composition exam score | 0 - 100 points |
| `Total_Score` | Integer | Sum of all three subject scores | 0 - 300 points |
| `Average_Score` | Float | Mean academic score across subjects | 0.0 - 100.0 points |
| `Pass_Status` | String | Overall academic pass/fail determination | `Pass`, `Fail` |

---

## 3. Project 3: Meteorological Weather Dataset (`data/weather_data.csv`)
- **Total Records**: 1,000 daily observations
- **Coverage**: 3 Meteorological Stations (Springfield, Riverdale, Oakridge)

| Column Name | Data Type | Description | Units / Range |
|---|---|---|---|
| `Date` | String | Observation date | `YYYY-MM-DD` |
| `Location` | String | Weather monitoring ground station | `Springfield`, `Riverdale`, `Oakridge` |
| `MinTemp` | Float | Minimum temperature logged in 24 hours | -2.0°C - 28.0°C |
| `MaxTemp` | Float | Maximum temperature logged in 24 hours | 10.0°C - 44.0°C |
| `Rainfall` | Float | 24-hour cumulative precipitation | 0.0 - 120.0 mm |
| `Evaporation` | Float | Class A pan evaporation | 0.5 - 18.0 mm |
| `Sunshine` | Float | Daily hours of bright sunshine | 0.0 - 14.0 hours |
| `WindGustDir` | String | Direction of strongest 24-hour wind gust | 16-point compass (e.g. `NW`, `SE`) |
| `WindGustSpeed` | Integer | Maximum instantaneous wind gust speed | 15 - 110 km/h |
| `WindSpeed9am` | Integer | Sustained wind speed at 9:00 AM | 0 - 55 km/h |
| `WindSpeed3pm` | Integer | Sustained wind speed at 3:00 PM | 0 - 65 km/h |
| `Humidity9am` | Integer | Relative air humidity at 9:00 AM | 20% - 100% |
| `Humidity3pm` | Integer | Relative air humidity at 3:00 PM | 10% - 98% |
| `Pressure9am` | Float | Mean sea level barometric pressure at 9 AM | 995.0 - 1035.0 hPa |
| `Pressure3pm` | Float | Mean sea level barometric pressure at 3 PM | 990.0 - 1032.0 hPa |
| `Cloud9am` | Integer | Cloud cover fraction at 9:00 AM | 0 - 8 oktas |
| `Cloud3pm` | Integer | Cloud cover fraction at 3:00 PM | 0 - 8 oktas |
| `Temp9am` | Float | Dry-bulb air temperature at 9:00 AM | 0.0°C - 35.0°C |
| `Temp3pm` | Float | Dry-bulb air temperature at 3:00 PM | 8.0°C - 42.0°C |
| `RainToday` | String | Rain recorded in previous 24 hours (>1mm) | `Yes`, `No` |
| `RainTomorrow` | String | Next-day precipitation occurrence | `Yes`, `No` |
| `Season` | String | Meteorological season | `Winter`, `Spring`, `Summer`, `Autumn` |
| `Extreme_Event` | String | Classified extreme weather hazard | `None`, `Heatwave`, `Cold Wave`, `Heavy Rain Storm`, `Severe Gale` |

---

## 4. Project 4: Healthcare & COVID-19 Trends (`data/healthcare_covid_trends.csv`)
- **Total Records**: 1,000 regional daily reports
- **Coverage**: 5 Regional Health Authorities

| Column Name | Data Type | Description | Units / Range |
|---|---|---|---|
| `Date` | String | Surveillance report date | `YYYY-MM-DD` |
| `Region` | String | Regional healthcare authority | `Metro Health District`, `Northern Region`, `Coastal Medical Zone`, `Valley Health Authority`, `Eastern Highlands` |
| `Confirmed_Cases` | Integer | Cumulative confirmed RT-PCR infections | 2,500 - 95,000 |
| `Active_Cases` | Integer | Current actively infected patient count | 50 - 4,500 |
| `Recovered` | Integer | Cumulative clinical recoveries | 2,100 - 88,000 |
| `Deaths` | Integer | Cumulative virus-attributed deaths | 65 - 1,800 |
| `Hospitalized` | Integer | Inpatients in medical/surgical ward beds | 5 - 650 patients |
| `ICU_Admissions` | Integer | Critical care patients on mechanical ventilation | 1 - 120 patients |
| `Testing_Count` | Integer | Total diagnostic PCR/antigen tests processed | 500 - 8,500 daily tests |
| `Vaccination_Rate_Pct`| Float | Percentage of population with primary series | 12.0% - 88.5% |
| `Mortality_Rate_Pct` | Float | Cumulative Case Fatality Rate (Deaths / Confirmed) | 0.8% - 3.5% |
| `Recovery_Rate_Pct` | Float | Cumulative Recovery Rate (Recovered / Confirmed) | 70.0% - 94.0% |

---

## 5. Project 5: Real Estate Valuation (`data/real_estate_valuation.csv`)
- **Total Records**: 300 property transactions
- **Timeframe**: Sales Transactions Register

| Column Name | Data Type | Description | Units / Range |
|---|---|---|---|
| `Property_ID` | String | Unique real estate parcel ID | `PROP0001` - `PROP0300` |
| `Area` | Integer | Total interior floor living area | 520 - 4,999 sq ft |
| `Bedrooms` | Integer | Total residential bedrooms | 1 - 5 |
| `Bathrooms` | Integer | Total fitted bathrooms | 1 - 3 |
| `Age` | Integer | Building age since construction | 0 - 49 years |
| `Location` | String | Geographical micro-location | `City Center`, `Suburb`, `Rural` |
| `Property_Type` | String | Architectural structural classification | `Villa`, `Apartment`, `House` |
| `Price` | Integer | Closing transaction market price (USD/INR) | $3,695,000 - $58,700,000 |
