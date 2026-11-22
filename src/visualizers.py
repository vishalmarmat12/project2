"""
Visualization Engine Module
Generates publication-quality charts and plots for all 5 portfolio projects.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set cohesive theme
sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['figure.titlesize'] = 14
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 11


def generate_supermarket_visualizations(df: pd.DataFrame, output_dir: str):
    """Generates all visualizations for Project 1."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Chart 1: Product Line Revenue
    plt.figure(figsize=(10, 5))
    prod_rev = df.groupby('Product_Line')['Total'].sum().sort_values(ascending=True)
    colors = sns.color_palette("Blues_r", len(prod_rev))
    ax = prod_rev.plot(kind='barh', color=colors, edgecolor='black', alpha=0.85)
    plt.title('Total Revenue by Product Line (Supermarket Sales)', weight='bold', pad=15)
    plt.xlabel('Total Revenue (USD)')
    plt.ylabel('Product Category')
    for i, v in enumerate(prod_rev):
        ax.text(v + 1000, i, f"${v:,.0f}", va='center', fontweight='bold', fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '01_sales_by_product_line.png'), dpi=300)
    plt.close()
    
    # Chart 2: Day of Week & Time Slot Heatmap
    plt.figure(figsize=(9, 5))
    dow_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pivot_table = df.pivot_table(index='Day_Name', columns='Time_Slot', values='Total', aggfunc='sum').reindex(dow_order)
    sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt=',.0f', cbar_kws={'label': 'Revenue ($)'}, linewidths=.5)
    plt.title('Sales Velocity Heatmap: Day of Week vs Time Slot', weight='bold', pad=15)
    plt.xlabel('Time of Day')
    plt.ylabel('Day of Week')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '02_daily_hourly_sales_heatmap.png'), dpi=300)
    plt.close()
    
    # Chart 3: Payment Method by Customer Type
    plt.figure(figsize=(9, 5))
    pay_cust = df.groupby(['Payment', 'Customer_Type'])['Total'].sum().unstack()
    pay_cust.plot(kind='bar', stacked=False, colormap='Spectral', edgecolor='black', alpha=0.9, figsize=(9, 5))
    plt.title('Revenue Contribution: Payment Method by Customer Segment', weight='bold', pad=15)
    plt.xlabel('Payment Method')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=0)
    plt.legend(title='Customer Type')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '03_payment_and_customer_segmentation.png'), dpi=300)
    plt.close()
    
    # Chart 4: Rating Distribution across Branches
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Branch', y='Rating', hue='City', data=df, palette='Set2')
    plt.title('Customer Rating Distribution by Branch & City', weight='bold', pad=15)
    plt.xlabel('Branch Location')
    plt.ylabel('Customer Satisfaction Rating (1-10)')
    plt.ylim(3.5, 10.5)
    plt.legend(title='City', loc='lower right')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '04_branch_rating_distribution.png'), dpi=300)
    plt.close()


def generate_student_visualizations(df: pd.DataFrame, output_dir: str):
    """Generates all visualizations for Project 2."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Chart 1: Subject Score Distributions
    plt.figure(figsize=(10, 5))
    sns.kdeplot(df['Math_Score'], label='Math', fill=True, alpha=0.3, color='#e74c3c')
    sns.kdeplot(df['Reading_Score'], label='Reading', fill=True, alpha=0.3, color='#2980b9')
    sns.kdeplot(df['Writing_Score'], label='Writing', fill=True, alpha=0.3, color='#27ae60')
    plt.title('Score Density Distributions Across Academic Subjects', weight='bold', pad=15)
    plt.xlabel('Standardized Score (0 - 100)')
    plt.ylabel('Probability Density')
    plt.axvline(40, color='gray', linestyle='--', label='Passing Threshold (40)')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '01_subject_score_distributions.png'), dpi=300)
    plt.close()
    
    # Chart 2: Attendance vs Overall Score Regression
    plt.figure(figsize=(9, 5))
    sns.regplot(
        x='Attendance_Rate', y='Average_Score', data=df,
        scatter_kws={'alpha': 0.45, 'color': '#34495e'},
        line_kws={'color': '#e74c3c', 'linewidth': 2.5}
    )
    plt.title('Correlation: Student Attendance Rate vs Overall Average Score', weight='bold', pad=15)
    plt.xlabel('Attendance Rate (%)')
    plt.ylabel('Average Academic Score')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '02_attendance_vs_scores_regression.png'), dpi=300)
    plt.close()
    
    # Chart 3: Parental Education & Pass Rates
    plt.figure(figsize=(10, 5))
    parent_stats = df.groupby('Parental_Education')['Pass_Status'].apply(lambda x: (x == 'Pass').mean() * 100).sort_values(ascending=True)
    ax = parent_stats.plot(kind='barh', color='#16a085', edgecolor='black', alpha=0.85)
    plt.title('Academic Pass Rate (%) by Parental Education Level', weight='bold', pad=15)
    plt.xlabel('Pass Rate (%)')
    plt.ylabel('Parental Education Level')
    for i, v in enumerate(parent_stats):
        ax.text(v + 1, i, f"{v:.1f}%", va='center', fontweight='bold', fontsize=9)
    plt.xlim(0, 105)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '03_parental_education_pass_rates.png'), dpi=300)
    plt.close()
    
    # Chart 4: Test Prep Course Impact
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Test_Prep_Course', y='Average_Score', hue='Lunch_Type', data=df, palette='Pastel1')
    plt.title('Test Preparation Course Impact Segmented by Socioeconomic Lunch Tier', weight='bold', pad=15)
    plt.xlabel('Test Preparation Course Status')
    plt.ylabel('Average Academic Score')
    plt.legend(title='Lunch Program')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '04_test_prep_impact_boxplots.png'), dpi=300)
    plt.close()


def generate_weather_visualizations(df: pd.DataFrame, output_dir: str):
    """Generates all visualizations for Project 3."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Chart 1: Monthly Temperature Trends
    plt.figure(figsize=(10, 5))
    monthly_temp = df.groupby('Month_Num').agg({'MinTemp': 'mean', 'MaxTemp': 'mean'}).sort_index()
    months_map = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
    months = [months_map.get(m, str(m)) for m in monthly_temp.index]
    plt.plot(months, monthly_temp['MaxTemp'], marker='o', color='#e67e22', linewidth=2.5, label='Avg Max Temp')
    plt.plot(months, monthly_temp['MinTemp'], marker='s', color='#2980b9', linewidth=2.5, label='Avg Min Temp')
    plt.fill_between(months, monthly_temp['MinTemp'], monthly_temp['MaxTemp'], color='#f39c12', alpha=0.2, label='Diurnal Range Band')
    plt.title('Annual Meteorological Temperature Profile (Mean Min & Max)', weight='bold', pad=15)
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '01_seasonal_temperature_trends.png'), dpi=300)
    plt.close()
    
    # Chart 2: Rainfall Distribution by Season
    plt.figure(figsize=(9, 5))
    sns.boxplot(x='Season', y='Rainfall', data=df[df['Rainfall'] > 0], palette='Blues', showmeans=True)
    plt.title('Seasonal Rainfall Intensity Distribution (Precipitation Days)', weight='bold', pad=15)
    plt.xlabel('Season')
    plt.ylabel('Rainfall (mm)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '02_rainfall_distribution_by_season.png'), dpi=300)
    plt.close()
    
    # Chart 3: Atmospheric Pressure vs Afternoon Humidity
    plt.figure(figsize=(9, 5))
    sns.scatterplot(
        x='Pressure3pm', y='Humidity3pm', hue='RainToday', style='RainTomorrow',
        data=df, alpha=0.7, palette={'Yes': '#2980b9', 'No': '#e74c3c'}, s=45
    )
    plt.title('Barometric Pressure vs Afternoon Humidity (Precipitation Predictor)', weight='bold', pad=15)
    plt.xlabel('Atmospheric Pressure at 3 PM (hPa)')
    plt.ylabel('Relative Humidity at 3 PM (%)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '03_humidity_vs_pressure_scatter.png'), dpi=300)
    plt.close()
    
    # Chart 4: Extreme Weather Events
    plt.figure(figsize=(8, 4.5))
    extreme_counts = df[df['Extreme_Event'] != 'Normal']['Extreme_Event'].value_counts()
    colors = ['#c0392b', '#2c3e50', '#2980b9', '#7f8c8d']
    ax = extreme_counts.plot(kind='bar', color=colors, edgecolor='black', alpha=0.85)
    plt.title('Frequency of Extreme Meteorological Events Logged', weight='bold', pad=15)
    plt.xlabel('Extreme Event Category')
    plt.ylabel('Total Observations')
    plt.xticks(rotation=15)
    for i, v in enumerate(extreme_counts):
        ax.text(i, v + 2, str(v), ha='center', fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '04_extreme_weather_event_frequency.png'), dpi=300)
    plt.close()


def generate_healthcare_visualizations(df: pd.DataFrame, output_dir: str):
    """Generates all visualizations for Project 4."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Chart 1: Epidemic Curve & Healthcare Strain
    plt.figure(figsize=(11, 5.5))
    daily_agg = df.groupby('Date').agg({'Active_Cases': 'sum', 'Hospitalized': 'sum', 'ICU_Admissions': 'sum'})
    
    fig, ax1 = plt.subplots(figsize=(11, 5))
    ax2 = ax1.twinx()
    
    ax1.plot(daily_agg.index, daily_agg['Active_Cases'], color='#e74c3c', label='Total Active Cases', linewidth=2.0)
    ax2.plot(daily_agg.index, daily_agg['Hospitalized'], color='#2980b9', label='Hospitalized', linewidth=2.0)
    ax2.plot(daily_agg.index, daily_agg['ICU_Admissions'], color='#8e44ad', linestyle='--', label='ICU Occupancy', linewidth=2.0)
    
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Active Cases', color='#e74c3c')
    ax2.set_ylabel('Hospitalized & ICU Load', color='#2980b9')
    plt.title('Epidemiological Wave Trajectory: Active Infections vs Clinical Bed Capacity', weight='bold', pad=15)
    
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '01_epidemic_curve_cases_hospitalizations.png'), dpi=300)
    plt.close()
    
    # Chart 2: Vaccination Rate vs Case Fatality Rate
    plt.figure(figsize=(9, 5))
    sns.regplot(
        x='Vaccination_Rate_Pct', y='Mortality_Rate_Pct', data=df,
        scatter_kws={'alpha': 0.35, 'color': '#27ae60'},
        line_kws={'color': '#c0392b', 'linewidth': 2.5}
    )
    plt.title('Clinical Impact: Vaccination Coverage Rate vs Case Mortality Rate (%)', weight='bold', pad=15)
    plt.xlabel('Population Vaccination Coverage (%)')
    plt.ylabel('Cumulative Mortality Rate (%)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '02_vaccination_vs_mortality_correlation.png'), dpi=300)
    plt.close()
    
    # Chart 3: Regional ICU Burden Heatmap
    plt.figure(figsize=(10, 5))
    df_sample = df.copy()
    df_sample['Month'] = df_sample['Date'].dt.to_period('M').astype(str)
    icu_pivot = df_sample.pivot_table(index='Region', columns='Month', values='ICU_Burden_Pct', aggfunc='mean')
    sns.heatmap(icu_pivot, cmap='Reds', annot=True, fmt='.1f', cbar_kws={'label': 'ICU / Hospitalized (%)'})
    plt.title('Healthcare System Vulnerability: Monthly ICU Strain by Health District', weight='bold', pad=15)
    plt.xlabel('Calendar Month')
    plt.ylabel('Health District')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '03_regional_icu_strain_heatmap.png'), dpi=300)
    plt.close()
    
    # Chart 4: Clinical Outcomes Trajectory
    plt.figure(figsize=(10, 5))
    latest_per_region = df.groupby('Region').last().reset_index()
    outcomes = latest_per_region.set_index('Region')[['Recovered', 'Deaths', 'Active_Cases']]
    outcomes.plot(kind='bar', stacked=True, color=['#2ecc71', '#e74c3c', '#f39c12'], edgecolor='black', figsize=(10, 5))
    plt.title('Cumulative Case Resolution Trajectory by Health District', weight='bold', pad=15)
    plt.xlabel('Health Region')
    plt.ylabel('Total Patient Count')
    plt.xticks(rotation=20)
    plt.legend(['Recovered', 'Deaths', 'Active'])
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '04_active_recovered_deaths_trajectories.png'), dpi=300)
    plt.close()


def generate_real_estate_visualizations(df: pd.DataFrame, output_dir: str):
    """Generates all visualizations for Project 5."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Chart 1: Price Distribution by Location
    plt.figure(figsize=(9, 5))
    sns.boxplot(x='Location', y='Price_in_Millions', data=df, palette='Set2')
    plt.title('Property Valuation Distribution by Prime Location', weight='bold', pad=15)
    plt.xlabel('Geographical Location')
    plt.ylabel('Property Price (Millions USD/INR)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '01_price_distribution_by_location.png'), dpi=300)
    plt.close()
    
    # Chart 2: Square Footage vs Price with OLS Regression
    plt.figure(figsize=(9, 5))
    sns.regplot(
        x='Area', y='Price_in_Millions', data=df,
        scatter_kws={'alpha': 0.5, 'color': '#2980b9'},
        line_kws={'color': '#e74c3c', 'linewidth': 2.5}
    )
    plt.title('Hedonic Pricing Model: Living Area (Sq Ft) vs Market Valuation', weight='bold', pad=15)
    plt.xlabel('Total Area (Square Feet)')
    plt.ylabel('Price (Millions)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '02_area_vs_price_regression.png'), dpi=300)
    plt.close()
    
    # Chart 3: Valuation per Sq Ft by Property Type
    plt.figure(figsize=(8, 5))
    type_sqft = df.groupby('Property_Type')['Price_per_SqFt'].mean().sort_values(ascending=False)
    colors = ['#8e44ad', '#27ae60', '#f39c12']
    ax = type_sqft.plot(kind='bar', color=colors, edgecolor='black', alpha=0.85)
    plt.title('Average Price per Square Foot Across Architectural Types', weight='bold', pad=15)
    plt.xlabel('Property Architectural Type')
    plt.ylabel('Avg Price / Sq Ft ($)')
    plt.xticks(rotation=0)
    for i, v in enumerate(type_sqft):
        ax.text(i, v + 150, f"${v:,.0f}", ha='center', fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '03_property_type_sqft_valuation.png'), dpi=300)
    plt.close()
    
    # Chart 4: Property Age Depreciation Curve
    plt.figure(figsize=(9, 5))
    sns.lineplot(x='Age', y='Price_per_SqFt', hue='Location', data=df, ci=None, marker='o', palette='Dark2')
    plt.title('Asset Depreciation Trajectory: Property Age vs Unit Valuation', weight='bold', pad=15)
    plt.xlabel('Building Age (Years)')
    plt.ylabel('Price per Sq Ft ($)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '04_age_depreciation_curve.png'), dpi=300)
    plt.close()
