import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# ================================
# FACE 5 - Data Visualisation
# Black Granite Quarry Analytics
# ================================

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="quarry_analytics",
    user="postgres",
    password="Ajay@1256"
)

print("Connected to PostgreSQL successfully!")

# Load data
loads_df = pd.read_sql("SELECT * FROM loads", conn)
buyers_df = pd.read_sql("SELECT * FROM buyers", conn)
blocks_df = pd.read_sql("SELECT * FROM blocks", conn)

# Merge loads with buyers and blocks
loads_df = loads_df.merge(buyers_df[['buyer_id', 'buyer_name']], on='buyer_id')
loads_df = loads_df.merge(blocks_df[['block_id', 'block_type']], on='block_id')

# Convert dates
loads_df['dispatch_date'] = pd.to_datetime(loads_df['dispatch_date'])
loads_df['year'] = loads_df['dispatch_date'].dt.year
loads_df['month'] = loads_df['dispatch_date'].dt.month
loads_df['month_name'] = loads_df['dispatch_date'].dt.strftime('%B')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11

print("Data loaded successfully!")
print("Building charts now...")

# ================================
# CHART 1 - Revenue by Buyer
# ================================
plt.figure()
buyer_revenue = loads_df.groupby('buyer_name')['total_revenue'].sum().sort_values()
colors = sns.color_palette('Blues', len(buyer_revenue))
bars = plt.barh(buyer_revenue.index, buyer_revenue.values, color=colors)
plt.title('Total Revenue by Buyer - 2018 to 2021', fontsize=16, fontweight='bold')
plt.xlabel('Total Revenue in Rupees')
plt.ylabel('Buyer Name')
for bar, val in zip(bars, buyer_revenue.values):
    plt.text(bar.get_width() + 50000, bar.get_y() + bar.get_height()/2,
             f'{val/100000:.1f} Lakhs', va='center', fontsize=9)
plt.tight_layout()
plt.savefig('pg_chart1_revenue_by_buyer.png', dpi=150)
plt.show()
print("Chart 1 saved - Revenue by Buyer!")

# ================================
# CHART 2 - Yearly Performance with COVID
# ================================
plt.figure()
yearly = loads_df.groupby('year')['total_revenue'].sum()
colors = ['#2ecc71', '#2ecc71', '#e74c3c', '#2ecc71']
bars = plt.bar(yearly.index.astype(str), yearly.values, color=colors)
plt.title('Yearly Revenue Performance\nRed Bar Shows COVID-19 Impact in 2020',
          fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Revenue in Rupees')
for bar, val in zip(bars, yearly.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100000,
             f'{val/100000:.1f} Lakhs', ha='center', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('pg_chart2_yearly_performance.png', dpi=150)
plt.show()
print("Chart 2 saved - Yearly Performance!")

# ================================
# CHART 3 - Revenue by Destination
# ================================
plt.figure()
dest_revenue = loads_df.groupby('destination')['total_revenue'].sum().sort_values(ascending=False)
sns.barplot(x=dest_revenue.index, y=dest_revenue.values, palette='Oranges_r')
plt.title('Revenue by Export Destination', fontsize=16, fontweight='bold')
plt.xlabel('Destination Country')
plt.ylabel('Total Revenue in Rupees')
plt.tight_layout()
plt.savefig('pg_chart3_revenue_by_destination.png', dpi=150)
plt.show()
print("Chart 3 saved - Revenue by Destination!")

# ================================
# CHART 4 - Revenue by Block Type
# ================================
plt.figure()
block_revenue = loads_df.groupby('block_type')['total_revenue'].sum().sort_values(ascending=False)
sns.barplot(x=block_revenue.index, y=block_revenue.values, palette='Greens_r')
plt.title('Revenue by Block Type\nGangsaw Blocks Lead Performance',
          fontsize=14, fontweight='bold')
plt.xlabel('Block Type')
plt.ylabel('Total Revenue in Rupees')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('pg_chart4_revenue_by_block.png', dpi=150)
plt.show()
print("Chart 4 saved - Revenue by Block Type!")

# ================================
# CHART 5 - Monthly Revenue Trend
# ================================
plt.figure()
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
monthly = loads_df.groupby('month_name')['total_revenue'].sum()
monthly = monthly.reindex(month_order)
bar_colors = ['#e74c3c' if m in ['June', 'July', 'August']
              else '#3498db' for m in month_order]
bars = plt.bar(range(12), monthly.values, color=bar_colors)
plt.xticks(range(12), [m[:3] for m in month_order])
plt.title('Monthly Revenue Pattern\nRed Bars Show Rainy Season Slowdown',
          fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Total Revenue in Rupees')
plt.tight_layout()
plt.savefig('pg_chart5_monthly_trend.png', dpi=150)
plt.show()
print("Chart 5 saved - Monthly Trend!")

# ================================
# CHART 6 - Rainy vs Normal Season
# ================================
plt.figure()
seasonal = loads_df.groupby('is_rainy_season')['total_revenue'].sum()
seasonal.index = ['Normal Season\n9 Months', 'Rainy Season\n3 Months']
colors = ['#2ecc71', '#e74c3c']
wedges, texts, autotexts = plt.pie(
    seasonal.values,
    labels=seasonal.index,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 12}
)
plt.title('Revenue Split - Rainy vs Normal Season',
          fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('pg_chart6_seasonal_split.png', dpi=150)
plt.show()
print("Chart 6 saved - Seasonal Split!")

# ================================
# CHART 7 - COVID Impact Line Chart
# ================================
plt.figure()
yearly_data = loads_df.groupby('year').agg(
    Revenue=('total_revenue', 'sum'),
    Loads=('load_id', 'count')
).reset_index()
plt.plot(yearly_data['year'], yearly_data['Revenue'],
         marker='o', linewidth=2.5, color='#3498db', markersize=10)
plt.fill_between(yearly_data['year'], yearly_data['Revenue'],
                 alpha=0.3, color='#3498db')
plt.axvline(x=2020, color='red', linestyle='--', linewidth=1.5, label='COVID-19 Year')
plt.title('Revenue Trend 2018 to 2021\nCOVID-19 Impact Clearly Visible',
          fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Revenue in Rupees')
plt.legend()
plt.xticks([2018, 2019, 2020, 2021])
plt.tight_layout()
plt.savefig('pg_chart7_covid_impact.png', dpi=150)
plt.show()
print("Chart 7 saved - COVID Impact!")

# ================================
# CHART 8 - Buyer Load Distribution
# ================================
plt.figure()
buyer_loads = loads_df.groupby('buyer_name')['load_id'].count().sort_values()
colors = sns.color_palette('Purples', len(buyer_loads))
plt.barh(buyer_loads.index, buyer_loads.values, color=colors)
plt.title('Total Loads by Buyer', fontsize=16, fontweight='bold')
plt.xlabel('Number of Loads')
plt.ylabel('Buyer Name')
plt.tight_layout()
plt.savefig('pg_chart8_loads_by_buyer.png', dpi=150)
plt.show()
print("Chart 8 saved - Loads by Buyer!")

print("\nAll 8 charts created and saved successfully!")
print("Check your quarry_analytics folder for pg_chart files!")

conn.close()