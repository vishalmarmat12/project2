"""
Data Cleaners & Transformation Pipeline Module
Provides domain-specific cleaning, feature engineering, and validation routines.
"""

import pandas as pd
import numpy as np


def clean_supermarket_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and enhances Supermarket Sales dataset.
    """
    data = df.copy()
    data['Date'] = pd.to_datetime(data['Date'])
    data['Time_dt'] = pd.to_datetime(data['Time'], format='%H:%M', errors='coerce').dt.time
    data['Hour'] = pd.to_datetime(data['Time'], format='%H:%M', errors='coerce').dt.hour
    
    data['Month'] = data['Date'].dt.month_name()
    data['Month_Num'] = data['Date'].dt.month
    data['Day_Name'] = data['Date'].dt.day_name()
    data['Is_Weekend'] = data['Day_Name'].isin(['Saturday', 'Sunday'])
    
    # Calculate Line_Subtotal, Tax_Check
    data['Calculated_Total'] = (data['Unit_Price'] * data['Quantity']) + data['Tax']
    
    # Time slot
    def get_time_slot(hour):
        if hour < 12:
            return 'Morning (8AM-12PM)'
        elif hour < 17:
            return 'Afternoon (12PM-5PM)'
        else:
            return 'Evening (5PM-9PM)'
            
    data['Time_Slot'] = data['Hour'].apply(get_time_slot)
    return data


def clean_student_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and enhances Student Performance dataset.
    """
    data = df.copy()
    data['Total_Score'] = data['Math_Score'] + data['Reading_Score'] + data['Writing_Score']
    data['Average_Score'] = (data['Total_Score'] / 3.0).round(2)
    
    def assign_grade(score):
        if score >= 85:
            return 'A (Distinction)'
        elif score >= 70:
            return 'B (Merit)'
        elif score >= 55:
            return 'C (Pass)'
        elif score >= 40:
            return 'D (Marginal Pass)'
        else:
            return 'F (Fail)'
            
    data['Grade'] = data['Average_Score'].apply(assign_grade)
    data['Pass_Status'] = np.where(
        (data['Math_Score'] >= 40) & 
        (data['Reading_Score'] >= 40) & 
        (data['Writing_Score'] >= 40) & 
        (data['Average_Score'] >= 50),
        'Pass', 'Fail'
    )
    
    data['Attendance_Tier'] = pd.cut(
        data['Attendance_Rate'],
        bins=[0, 70, 80, 90, 100],
        labels=['Critical (<70%)', 'Low (70-80%)', 'Good (80-90%)', 'Excellent (>90%)']
    )
    return data


def clean_weather_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and enhances Meteorological Weather dataset.
    """
    data = df.copy()
    data['Date'] = pd.to_datetime(data['Date'])
    data['Year'] = data['Date'].dt.year
    data['Month'] = data['Date'].dt.month_name()
    data['Month_Num'] = data['Date'].dt.month
    
    data['Diurnal_Temp_Range'] = (data['MaxTemp'] - data['MinTemp']).round(1)
    
    def categorize_rain(r):
        if r <= 0.2:
            return 'None (0mm)'
        elif r <= 5.0:
            return 'Light (0-5mm)'
        elif r <= 20.0:
            return 'Moderate (5-20mm)'
        elif r <= 50.0:
            return 'Heavy (20-50mm)'
        else:
            return 'Violent (>50mm)'
            
    data['Rain_Category'] = data['Rainfall'].apply(categorize_rain)
    return data


def clean_healthcare_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and enhances Healthcare & COVID-19 Trends dataset.
    """
    data = df.copy()
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values(by=['Region', 'Date']).reset_index(drop=True)
    
    # 7-day rolling statistics per region
    data['Hospitalization_Rate_Pct'] = (data['Hospitalized'] / data['Active_Cases'] * 100).round(2)
    data['ICU_Burden_Pct'] = (data['ICU_Admissions'] / data['Hospitalized'] * 100).round(2)
    data['Test_Positivity_Pct'] = (data['Confirmed_Cases'].diff().clip(lower=0) / data['Testing_Count'] * 100).round(2).fillna(0)
    
    # Vaccination status category
    data['Vaccination_Tier'] = pd.cut(
        data['Vaccination_Rate_Pct'],
        bins=[0, 30, 50, 70, 100],
        labels=['Early Stage (<30%)', 'Moderate (30-50%)', 'Advanced (50-70%)', 'Widespread (>70%)']
    )
    return data


def clean_real_estate_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and enhances Real Estate Valuation dataset.
    """
    data = df.copy()
    data['Price_per_SqFt'] = (data['Price'] / data['Area']).round(2)
    data['Price_in_Millions'] = (data['Price'] / 1_000_000.0).round(2)
    
    # Age Category
    data['Age_Category'] = pd.cut(
        data['Age'],
        bins=[-1, 5, 15, 30, 100],
        labels=['New (<5 yrs)', 'Modern (5-15 yrs)', 'Established (15-30 yrs)', 'Historic (>30 yrs)']
    )
    
    # Area Size Category
    data['Size_Category'] = pd.cut(
        data['Area'],
        bins=[0, 1500, 3000, 4500, 10000],
        labels=['Compact (<1500 sqft)', 'Mid-Size (1500-3000)', 'Spacious (3000-4500)', 'Grand (>4500 sqft)']
    )
    return data
