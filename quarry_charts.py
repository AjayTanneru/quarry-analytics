import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# Load real quarry data
df = pd.read_csv('quarry_exports.csv')
df['dispatch_date'] = pd.to_datetime(df['dispatch_date'])
df['month_name'] = df['dispatch_date'].dt.strftime('%B')
df['month_num'] = df['dispatch_date'].dt.month

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11

# =====================
# CHART 1
# Top Buyers by Revenue
# =====================
plt.figure()
buyer_revenue = df.groupby('buyer_name')['total_revenue'].sum().sort_values()
colors = sns.color_palette('Blues', len(buyer_revenue))
bars = plt.barh(buyer_revenue.index, buyer_revenue.values, color=colors)
plt.title('Top Buyers by Revenue\nNarasimhulagudem Black Granite Quarry 2018-2021',
          fontsize=14, fontweight='bold')
plt.xlabel('Total Revenue (₹)')
plt.tight_layout()
plt.savefig('chart1_top_buyers.png', dpi=150)
plt.show()
print("✅ Chart 1 saved — Top Buyers!")

# =====================
# CHART 2
# Yearly Performance
# =====================
plt.figure()
yearly = df.groupby('year')['total_revenue'].sum()
bar_colors = ['#2ecc71', '#2ecc71', '#e74c3c', '#2ecc71']
bars = plt.bar(yearly.index.astype(str), yearly.values, color=bar_colors)
plt.title('Yearly Revenue Performance\n2020 COVID Impact Clearly Visible',
          fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Revenue (₹)')
# Add value labels on bars
for bar, val in zip(bars, yearly.values):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 50000,
             f'₹{val/1000000:.2f}M',
             ha='center', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('chart2_yearly_performance.png', dpi=150)
plt.show()
print("✅ Chart 2 saved — Yearly Performance!")

# =====================
# CHART 3
# Revenue by Destination
# =====================
plt.figure()
dest_revenue = df.groupby('destination')[
    'total_revenue'].sum().sort_values(ascending=False)
sns.barplot(x=dest_revenue.index, y=dest_revenue.values, palette='Oranges_r')
plt.title('Revenue by Export Destination',
          fontsize=14, fontweight='bold')
plt.xlabel('Destination')
plt.ylabel('Total Revenue (₹)')
plt.tight_layout()
plt.savefig('chart3_revenue_by_destination.png', dpi=150)
plt.show()
print("✅ Chart 3 saved — Revenue by Destination!")

# =====================
# CHART 4
# Revenue by Block Type
# =====================
plt.figure()
block_revenue = df.groupby('block_type')[
    'total_revenue'].sum().sort_values(ascending=False)
sns.barplot(x=block_revenue.index, y=block_revenue.values, palette='Greens_r')
plt.title('Revenue by Block Type\nGangsaw Blocks Lead Performance',
          fontsize=14, fontweight='bold')
plt.xlabel('Block Type')
plt.ylabel('Total Revenue (₹)')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('chart4_revenue_by_block.png', dpi=150)
plt.show()
print("✅ Chart 4 saved — Revenue by Block Type!")

# =====================
# CHART 5
# Monthly Revenue Trend
# =====================
plt.figure()
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
monthly = df.groupby('month_name')['total_revenue'].sum()
monthly = monthly.reindex(month_order)
bar_colors = ['#e74c3c' if m in ['June', 'July', 'August']
              else '#3498db' for m in month_order]
bars = plt.bar(range(12), monthly.values, color=bar_colors)
plt.xticks(range(12), [m[:3] for m in month_order])
plt.title('Monthly Revenue Pattern\nRed = Rainy Season Slowdown',
          fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Total Revenue (₹)')
plt.tight_layout()
plt.savefig('chart5_monthly_trend.png', dpi=150)
plt.show()
print("✅ Chart 5 saved — Monthly Trend!")

# =====================
# CHART 6
# Rainy vs Normal Season
# =====================
plt.figure()
seasonal = df.groupby('is_rainy_season')['total_revenue'].sum()
seasonal.index = ['Normal Season\n(9 months)', 'Rainy Season\n(3 months)']
colors = ['#2ecc71', '#e74c3c']
wedges, texts, autotexts = plt.pie(
    seasonal.values,
    labels=seasonal.index,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 12}
)
plt.title('Revenue Split — Rainy vs Normal Season',
          fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('chart6_seasonal_split.png', dpi=150)
plt.show()
print("✅ Chart 6 saved — Seasonal Split!")

print("\n🎉 All 6 charts created and saved!")
print("📁 Check your quarry_analytics folder for PNG files!")
