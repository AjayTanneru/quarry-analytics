# Black Granite Quarry Analytics Platform
### Narasimhulagudem, Mahabubabad, Telangana, India

## About This Repository
Complete end-to-end data analytics and business intelligence 
platform built for a real black granite quarry export business. 
This repository contains two projects showing progression from 
basic analytics to an enterprise-level BI platform.

## Business Questions This Project Answers
1. Which buyer generated the most revenue?
2. Which country is our most profitable export market?
3. How did COVID-19 impact our business operations?
4. Which granite block type is most profitable?
5. Which months are peak season vs slow season?
6. How efficient is our dispatch process?

## Business Background
- Business: Black Granite Quarry Export Operations
- Location: Narasimhulagudem, Mahabubabad, Telangana, India
- Period: 2018 to 2021
- Product: Black Granite Blocks
- Markets: USA, China, Poland, UK, India
- Buyers: 6 real granite export companies

## Block Types and Pricing
- Gangsaw Large Slab: 110000 per cubic meter
- Big Block High 240x140 Above: 100000 per cubic meter
- Big Block Low 240x140 Below: 90000 per cubic meter
- Small Block High 200x100 Above: 80000 per cubic meter
- Small Block Low 200x100 Below: 70000 per cubic meter

## Project 1 - Python Analytics Platform
Basic analytics project using Python and Power BI

### Tools Used
- Python for data generation and analysis
- Pandas for data manipulation
- Matplotlib and Seaborn for data visualisation
- Power BI for an interactive dashboard
- GitHub for version control

### Files
- project1/quarry_data.py - Generates quarry dataset
- project1/quarry_analysis.py - Business intelligence analysis
- project1/quarry_charts.py - 6 professional charts
- project1/quarry_exports.csv - 100 export records dataset
- project1/quarry_dashboard.pbix - Power BI dashboard
- project1/Quarry_Analytics_Executive_Summary.pptx - Presentation

### Key Insights
- The USA is the top market, generating 35 percent of total revenue
- Gangsaw blocks the highest revenue product at 1.02 Crores
- COVID caused a 67 percent revenue drop in 2020
- Rainy season, June to August, caused 90 percent fewer loads
- March peak month, generating 49 Lakhs
- Average dispatch turnaround 1.7 days

## Project 2 - Enterprise BI Platform
Advanced analytics platform using PostgreSQL, SQL and Python

### Tools Used
- PostgreSQL 16 for database management
- SQL for data querying and analysis
- Python for data pipeline
- Pandas for data processing
- Matplotlib and Seaborn for visualisation
- Power BI connected to live PostgreSQL database
- SQLAlchemy for database connection
- GitHub for version control

### Database Design
5 tables in the PostgreSQL quarry_analytics database
- buyers table - 6 buyer company records
- blocks table - 5 block type records with pricing
- loads table - 100 export load records
- payments table - 100 payment records
- market_performance table - 17 market summary records

### Files
- project2/quarry_database.sql - Database schema and setup
- project2/db_connection.py - PostgreSQL connection script
- project2/data_cleaning.py - Data validation and cleaning
- project2/eda_analysis.py - 6 SQL analytical queries
- project2/visualisation.py - 8 professional charts
- project2/quarry_postgresql_dashboard.pbix - Live Power BI dashboard
- project2/clean_quarry_data.csv - Validated clean dataset
- project2/analysis_buyers.csv - Buyer performance analysis
- project2/analysis_destinations.csv - Market analysis results
- project2/analysis_blocks.csv - Block type analysis results
- project2/analysis_monthly.csv - Monthly performance results

### Key Metrics Achieved
- Total Loads: 100 export loads tracked
- Total Revenue: 4.50 Crores across 4 years
- Data Quality Score: 100 percent
- Missing Values: Zero
- Duplicate Records: Zero
- Payment Compliance: 100 percent advance payment
- Dispatch Turnaround: 1 day average
- Top Buyer: Samantula Granites 86.46 Lakhs
- Top Market: USA 1.58 Crores 35 percent revenue share
- Top Product: Gangsaw blocks 2.13 Crores 47 percent revenue share
- COVID Impact: 83.5 percent revenue drop in 2020
- Full Recovery: 2021 highest revenue year at 1.46 Crores

## Business Insights and Decisions

| Business Question | Finding | Recommended Action |
|---|---|---|
| Best buyer | Samantula Granites 86.46 Lakhs | Prioritise this relationship |
| Best market | USA 1.58 Crores | Focus exports to USA |
| COVID impact | 83.5 percent revenue drop 2020 | Build emergency fund |
| Best block type | Gangsaw 2.13 Crores | Increase Gangsaw production |
| Peak month | March 69.31 Lakhs | Stock up before March |
| Worst season | June to August 90 percent fewer loads | Reduce costs in rainy season |

## Overall Business Summary
- Business Period: 2018 to 2021
- Total Export Loads: 100 shipments
- Total Revenue: 4.50 Crores
- Total Cubic Meters: 460.80 cubic meters
- Total Buyers: 6 companies
- Total Markets: 5 countries
- Average Revenue per Load: 4.50 Lakhs
- Dispatch Turnaround: 1 day average

## About
Built by Ajay Kumar Tanneru - Data Analyst with 4 years of 
hands-on quarry business experience and a Postgraduate Diploma 
in Data Analytics from the National College of Ireland, Dublin.

Portfolio: github.com/AjayTanneru/quarry-analytics
Email: ajaytanneru18@gmail.com
