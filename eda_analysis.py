import psycopg2
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# ================================
# FACE 4 - Exploratory Data Analysis
# Black Granite Quarry Analytics
# ================================

# Connect using SQLAlchemy - fixes the warning!
engine = create_engine(
    "postgresql+psycopg2://",
    creator=lambda: psycopg2.connect(
        host="localhost",
        database="quarry_analytics",
        user="postgres",
        password="Ajay@1256"
    )
)

print("Connected to PostgreSQL successfully!")
print("=" * 60)

# ================================
# QUESTION 1 - Which buyer generated most revenue?
# ================================
print("\nQUESTION 1 - TOP BUYERS BY REVENUE")
print("=" * 60)

query1 = """
SELECT 
    b.buyer_name,
    COUNT(l.load_id) as total_loads,
    SUM(l.total_revenue) as total_revenue,
    ROUND(AVG(l.total_revenue)::numeric, 2) as avg_revenue_per_load,
    ROUND((SUM(l.total_revenue) / 
    (SELECT SUM(total_revenue) FROM loads) * 100)::numeric, 2) 
    as revenue_percentage
FROM loads l
JOIN buyers b ON l.buyer_id = b.buyer_id
GROUP BY b.buyer_name
ORDER BY total_revenue DESC;
"""

buyer_analysis = pd.read_sql(query1, engine)
print(buyer_analysis.to_string())

# ================================
# QUESTION 2 - Which country is most profitable?
# ================================
print("\nQUESTION 2 - REVENUE BY DESTINATION")
print("=" * 60)

query2 = """
SELECT 
    destination,
    COUNT(load_id) as total_loads,
    SUM(total_revenue) as total_revenue,
    ROUND(AVG(total_revenue)::numeric, 2) as avg_revenue_per_load,
    ROUND((SUM(total_revenue) / 
    (SELECT SUM(total_revenue) FROM loads) * 100)::numeric, 2) 
    as revenue_percentage
FROM loads
GROUP BY destination
ORDER BY total_revenue DESC;
"""

destination_analysis = pd.read_sql(query2, engine)
print(destination_analysis.to_string())

# ================================
# QUESTION 3 - How did COVID impact exports?
# ================================
print("\nQUESTION 3 - COVID IMPACT ANALYSIS")
print("=" * 60)

query3 = """
SELECT 
    EXTRACT(YEAR FROM dispatch_date)::INT as year,
    COUNT(load_id) as total_loads,
    SUM(total_revenue) as total_revenue,
    ROUND(AVG(cubic_meters)::numeric, 2) as avg_cubic_meters,
    CASE 
        WHEN EXTRACT(YEAR FROM dispatch_date) = 2020 
        THEN 'COVID Year'
        ELSE 'Normal Year'
    END as year_type
FROM loads
GROUP BY EXTRACT(YEAR FROM dispatch_date)
ORDER BY year;
"""

covid_analysis = pd.read_sql(query3, engine)
print(covid_analysis.to_string())

# Calculate COVID impact percentage
revenue_2019 = covid_analysis[covid_analysis['year']==2019]['total_revenue'].values[0]
revenue_2020 = covid_analysis[covid_analysis['year']==2020]['total_revenue'].values[0]
covid_drop = ((revenue_2019 - revenue_2020) / revenue_2019 * 100)
print(f"\nCOVID Revenue Drop: {covid_drop:.1f} percent")

# ================================
# QUESTION 4 - Which block type is most profitable?
# ================================
print("\nQUESTION 4 - REVENUE BY BLOCK TYPE")
print("=" * 60)

query4 = """
SELECT 
    bl.block_type,
    bl.block_size,
    bl.price_per_m3,
    COUNT(l.load_id) as total_loads,
    SUM(l.cubic_meters) as total_cubic_meters,
    SUM(l.total_revenue) as total_revenue,
    ROUND(AVG(l.total_revenue)::numeric, 2) as avg_revenue_per_load
FROM loads l
JOIN blocks bl ON l.block_id = bl.block_id
GROUP BY bl.block_type, bl.block_size, bl.price_per_m3
ORDER BY total_revenue DESC;
"""

block_analysis = pd.read_sql(query4, engine)
print(block_analysis.to_string())

# ================================
# QUESTION 5 - Which months are peak vs slow?
# ================================
print("\nQUESTION 5 - MONTHLY PERFORMANCE ANALYSIS")
print("=" * 60)

query5 = """
SELECT 
    TO_CHAR(dispatch_date, 'Month') as month_name,
    EXTRACT(MONTH FROM dispatch_date)::INT as month_num,
    COUNT(load_id) as total_loads,
    SUM(total_revenue) as total_revenue,
    CASE 
        WHEN EXTRACT(MONTH FROM dispatch_date) IN (6,7,8) 
        THEN 'Rainy Season'
        ELSE 'Normal Season'
    END as season
FROM loads
GROUP BY TO_CHAR(dispatch_date, 'Month'), 
         EXTRACT(MONTH FROM dispatch_date)
ORDER BY month_num;
"""

monthly_analysis = pd.read_sql(query5, engine)
print(monthly_analysis.to_string())

# ================================
# QUESTION 6 - How efficient is dispatch process?
# ================================
print("\nQUESTION 6 - DISPATCH EFFICIENCY ANALYSIS")
print("=" * 60)

query6 = """
SELECT 
    EXTRACT(YEAR FROM dispatch_date)::INT as year,
    COUNT(load_id) as total_loads,
    ROUND(AVG(dispatch_date - payment_date)::numeric, 2) 
    as avg_dispatch_days,
    MIN(dispatch_date - payment_date) as min_dispatch_days,
    MAX(dispatch_date - payment_date) as max_dispatch_days
FROM loads
GROUP BY EXTRACT(YEAR FROM dispatch_date)
ORDER BY year;
"""

dispatch_analysis = pd.read_sql(query6, engine)
print(dispatch_analysis.to_string())

# ================================
# OVERALL BUSINESS SUMMARY
# ================================
print("\nOVERALL BUSINESS SUMMARY")
print("=" * 60)

loads_df = pd.read_sql("SELECT * FROM loads", engine)
loads_df['dispatch_date'] = pd.to_datetime(loads_df['dispatch_date'])
loads_df['year'] = loads_df['dispatch_date'].dt.year

print(f"Business Period:        2018 to 2021")
print(f"Total Loads:            {len(loads_df)}")
print(f"Total Revenue:          {loads_df['total_revenue'].sum():,.0f} rupees")
print(f"Average Revenue/Load:   {loads_df['total_revenue'].mean():,.0f} rupees")
print(f"Total Cubic Meters:     {loads_df['cubic_meters'].sum():.2f} cubic meters")
print(f"Total Buyers:           6 companies")
print(f"Total Markets:          5 countries")
print("=" * 60)
print("EDA Analysis Complete!")

# Save results to CSV
buyer_analysis.to_csv('analysis_buyers.csv', index=False)
destination_analysis.to_csv('analysis_destinations.csv', index=False)
block_analysis.to_csv('analysis_blocks.csv', index=False)
monthly_analysis.to_csv('analysis_monthly.csv', index=False)
print("All analysis files saved!")