"""
Statistical Analysis & Insights Engine Module
Provides statistical computations, correlations, trend assessments, and KPI summaries.
"""

import pandas as pd
import numpy as np
from scipy import stats
from typing import Dict, Any, Tuple


def analyze_supermarket_sales(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Computes key retail KPIs, product performance, and customer segmentation.
    """
    total_revenue = df['Total'].sum()
    total_transactions = len(df)
    avg_ticket = df['Total'].mean()
    median_ticket = df['Total'].median()
    total_tax = df['Tax'].sum()
    avg_rating = df['Rating'].mean()
    
    # By Product Line
    product_performance = df.groupby('Product_Line').agg(
        Revenue=('Total', 'sum'),
        Units_Sold=('Quantity', 'sum'),
        Transactions=('Invoice_ID', 'count'),
        Avg_Rating=('Rating', 'mean'),
        Avg_Unit_Price=('Unit_Price', 'mean')
    ).sort_values(by='Revenue', ascending=False)
    product_performance['Revenue_Share_Pct'] = (product_performance['Revenue'] / total_revenue * 100).round(2)
    
    # By City & Branch
    branch_performance = df.groupby(['City', 'Branch']).agg(
        Revenue=('Total', 'sum'),
        Transactions=('Invoice_ID', 'count'),
        Avg_Ticket=('Total', 'mean'),
        Avg_Rating=('Rating', 'mean')
    ).reset_index()
    
    # By Customer Type
    customer_segmentation = df.groupby('Customer_Type').agg(
        Revenue=('Total', 'sum'),
        Transactions=('Invoice_ID', 'count'),
        Avg_Spending=('Total', 'mean'),
        Avg_Rating=('Rating', 'mean')
    ).reset_index()
    
    # By Payment Method
    payment_stats = df.groupby('Payment').agg(
        Revenue=('Total', 'sum'),
        Transactions=('Invoice_ID', 'count'),
        Avg_Rating=('Rating', 'mean')
    ).reset_index()
    
    # Day & Time Analysis
    dow_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dow_sales = df.groupby('Day_Name')['Total'].agg(['sum', 'mean', 'count']).reindex(dow_order)
    
    time_slot_sales = df.groupby('Time_Slot')['Total'].agg(['sum', 'mean', 'count'])
    
    return {
        "total_revenue": round(total_revenue, 2),
        "total_transactions": total_transactions,
        "avg_ticket": round(avg_ticket, 2),
        "median_ticket": round(median_ticket, 2),
        "total_tax": round(total_tax, 2),
        "avg_rating": round(avg_rating, 2),
        "product_performance": product_performance,
        "branch_performance": branch_performance,
        "customer_segmentation": customer_segmentation,
        "payment_stats": payment_stats,
        "dow_sales": dow_sales,
        "time_slot_sales": time_slot_sales
    }


def analyze_student_performance(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Computes pass/fail statistics, subject distributions, and attendance impact.
    """
    total_students = len(df)
    pass_count = (df['Pass_Status'] == 'Pass').sum()
    pass_rate = round((pass_count / total_students) * 100, 2)
    
    subject_stats = {
        'Math': {
            'mean': round(df['Math_Score'].mean(), 2),
            'median': round(df['Math_Score'].median(), 2),
            'std': round(df['Math_Score'].std(), 2)
        },
        'Reading': {
            'mean': round(df['Reading_Score'].mean(), 2),
            'median': round(df['Reading_Score'].median(), 2),
            'std': round(df['Reading_Score'].std(), 2)
        },
        'Writing': {
            'mean': round(df['Writing_Score'].mean(), 2),
            'median': round(df['Writing_Score'].median(), 2),
            'std': round(df['Writing_Score'].std(), 2)
        },
        'Overall': {
            'mean': round(df['Average_Score'].mean(), 2),
            'median': round(df['Average_Score'].median(), 2),
            'std': round(df['Average_Score'].std(), 2)
        }
    }
    
    # Correlations
    corr_attendance_math, p_att_math = stats.pearsonr(df['Attendance_Rate'], df['Math_Score'])
    corr_attendance_avg, p_att_avg = stats.pearsonr(df['Attendance_Rate'], df['Average_Score'])
    corr_study_avg, p_study_avg = stats.pearsonr(df['Study_Hours_Weekly'], df['Average_Score'])
    
    # Impact of Parental Education
    parent_impact = df.groupby('Parental_Education').agg(
        Students=('Student_ID', 'count'),
        Avg_Score=('Average_Score', 'mean'),
        Pass_Rate=('Pass_Status', lambda s: round((s == 'Pass').mean() * 100, 2))
    ).sort_values(by='Avg_Score', ascending=False)
    
    # Impact of Test Preparation Course
    prep_impact = df.groupby('Test_Prep_Course').agg(
        Students=('Student_ID', 'count'),
        Avg_Math=('Math_Score', 'mean'),
        Avg_Reading=('Reading_Score', 'mean'),
        Avg_Writing=('Writing_Score', 'mean'),
        Overall_Avg=('Average_Score', 'mean'),
        Pass_Rate=('Pass_Status', lambda s: round((s == 'Pass').mean() * 100, 2))
    )
    
    # Attendance Tier Breakdown
    attendance_impact = df.groupby('Attendance_Tier', observed=False).agg(
        Students=('Student_ID', 'count'),
        Avg_Score=('Average_Score', 'mean'),
        Pass_Rate=('Pass_Status', lambda s: round((s == 'Pass').mean() * 100, 2))
    )
    
    return {
        "total_students": total_students,
        "pass_count": int(pass_count),
        "pass_rate": pass_rate,
        "subject_stats": subject_stats,
        "corr_attendance_math": round(corr_attendance_math, 3),
        "corr_attendance_avg": round(corr_attendance_avg, 3),
        "corr_study_avg": round(corr_study_avg, 3),
        "parent_impact": parent_impact,
        "prep_impact": prep_impact,
        "attendance_impact": attendance_impact
    }


def analyze_weather_data(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Computes meteorological trends, seasonal dynamics, rainfall totals, and extreme events.
    """
    total_observations = len(df)
    avg_min_temp = round(df['MinTemp'].mean(), 2)
    avg_max_temp = round(df['MaxTemp'].mean(), 2)
    total_rainfall = round(df['Rainfall'].sum(), 2)
    rainy_days_count = (df['RainToday'] == 'Yes').sum()
    rain_day_pct = round((rainy_days_count / total_observations) * 100, 2)
    
    # Seasonal Analysis
    season_stats = df.groupby('Season').agg(
        Avg_MinTemp=('MinTemp', 'mean'),
        Avg_MaxTemp=('MaxTemp', 'mean'),
        Total_Rainfall=('Rainfall', 'sum'),
        Avg_Rainfall=('Rainfall', 'mean'),
        Rain_Days=('RainToday', lambda s: (s == 'Yes').sum()),
        Avg_Humidity3pm=('Humidity3pm', 'mean'),
        Max_Wind_Gust=('WindGustSpeed', 'max')
    ).round(2)
    
    # Location comparison
    location_stats = df.groupby('Location').agg(
        Avg_MaxTemp=('MaxTemp', 'mean'),
        Total_Rainfall=('Rainfall', 'sum'),
        Rain_Frequency_Pct=('RainToday', lambda s: round((s == 'Yes').mean() * 100, 2)),
        Max_WindSpeed=('WindGustSpeed', 'max')
    ).round(2)
    
    # Extreme weather events
    extreme_events = df[df['Extreme_Event'] != 'Normal']['Extreme_Event'].value_counts()
    
    # Correlation between humidity/pressure and rainfall
    corr_humidity_rain, _ = stats.pearsonr(df['Humidity3pm'], df['Rainfall'])
    corr_pressure_rain, _ = stats.pearsonr(df['Pressure3pm'], df['Rainfall'])
    
    return {
        "total_observations": total_observations,
        "avg_min_temp": avg_min_temp,
        "avg_max_temp": avg_max_temp,
        "total_rainfall": total_rainfall,
        "rainy_days_count": int(rainy_days_count),
        "rain_day_pct": rain_day_pct,
        "season_stats": season_stats,
        "location_stats": location_stats,
        "extreme_events": extreme_events,
        "corr_humidity_rain": round(corr_humidity_rain, 3),
        "corr_pressure_rain": round(corr_pressure_rain, 3)
    }


def analyze_healthcare_trends(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Computes epidemiological metrics, vaccination impact, and hospital utilization.
    """
    total_records = len(df)
    total_confirmed = df.groupby('Region')['Confirmed_Cases'].max().sum()
    total_deaths = df.groupby('Region')['Deaths'].max().sum()
    total_recovered = df.groupby('Region')['Recovered'].max().sum()
    overall_cfr = round((total_deaths / total_confirmed) * 100, 2)
    
    # Regional Summary
    regional_summary = df.groupby('Region').agg(
        Peak_Confirmed=('Confirmed_Cases', 'max'),
        Peak_Hospitalized=('Hospitalized', 'max'),
        Peak_ICU=('ICU_Admissions', 'max'),
        Total_Deaths=('Deaths', 'max'),
        Final_Vaccination_Rate=('Vaccination_Rate_Pct', 'max'),
        Final_Mortality_Rate=('Mortality_Rate_Pct', 'last')
    )
    
    # Vaccination Tier Impact
    vax_impact = df.groupby('Vaccination_Tier', observed=False).agg(
        Avg_Hospitalization_Rate=('Hospitalization_Rate_Pct', 'mean'),
        Avg_Mortality_Rate=('Mortality_Rate_Pct', 'mean'),
        Avg_ICU_Burden=('ICU_Burden_Pct', 'mean')
    ).round(2)
    
    # Correlation between Vaccination Rate and Mortality Rate
    corr_vax_mortality, _ = stats.pearsonr(df['Vaccination_Rate_Pct'], df['Mortality_Rate_Pct'])
    corr_vax_hosp, _ = stats.pearsonr(df['Vaccination_Rate_Pct'], df['Hospitalization_Rate_Pct'])
    
    return {
        "total_records": total_records,
        "total_confirmed": int(total_confirmed),
        "total_deaths": int(total_deaths),
        "total_recovered": int(total_recovered),
        "overall_cfr": overall_cfr,
        "regional_summary": regional_summary,
        "vax_impact": vax_impact,
        "corr_vax_mortality": round(corr_vax_mortality, 3),
        "corr_vax_hosp": round(corr_vax_hosp, 3)
    }


def analyze_real_estate(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Computes valuation dynamics, location premiums, age depreciation, and feature pricing.
    """
    total_properties = len(df)
    avg_price = df['Price'].mean()
    median_price = df['Price'].median()
    avg_price_sqft = df['Price_per_SqFt'].mean()
    median_price_sqft = df['Price_per_SqFt'].median()
    
    # By Location
    location_summary = df.groupby('Location').agg(
        Count=('Property_ID', 'count'),
        Avg_Price=('Price', 'mean'),
        Median_Price=('Price', 'median'),
        Avg_Price_per_SqFt=('Price_per_SqFt', 'mean'),
        Avg_Area=('Area', 'mean')
    ).round(2).sort_values(by='Avg_Price', ascending=False)
    
    # By Property Type
    type_summary = df.groupby('Property_Type').agg(
        Count=('Property_ID', 'count'),
        Avg_Price=('Price', 'mean'),
        Avg_Price_per_SqFt=('Price_per_SqFt', 'mean'),
        Avg_Area=('Area', 'mean')
    ).round(2).sort_values(by='Avg_Price', ascending=False)
    
    # By Age Category
    age_summary = df.groupby('Age_Category', observed=False).agg(
        Count=('Property_ID', 'count'),
        Avg_Price=('Price', 'mean'),
        Avg_Price_per_SqFt=('Price_per_SqFt', 'mean')
    ).round(2)
    
    # Correlation with Price
    numeric_cols = ['Area', 'Bedrooms', 'Bathrooms', 'Age', 'Price_per_SqFt']
    price_correlations = {col: round(df[col].corr(df['Price']), 3) for col in numeric_cols}
    
    # Simple OLS regression for Area vs Price
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['Area'], df['Price'])
    
    return {
        "total_properties": total_properties,
        "avg_price": round(avg_price, 2),
        "median_price": round(median_price, 2),
        "avg_price_sqft": round(avg_price_sqft, 2),
        "median_price_sqft": round(median_price_sqft, 2),
        "location_summary": location_summary,
        "type_summary": type_summary,
        "age_summary": age_summary,
        "price_correlations": price_correlations,
        "area_regression": {
            "slope": round(slope, 2),
            "intercept": round(intercept, 2),
            "r_squared": round(r_value**2, 4),
            "p_value": p_value
        }
    }
