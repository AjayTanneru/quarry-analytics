import pandas as pd

# Load your real quarry data
df = pd.read_csv('quarry_exports.csv')

# =====================
# ANALYSIS 1
# Top Buyers by Revenue
# =====================
print("=== TOP BUYERS BY REVENUE ===")
buyer_revenue = df.groupby('buyer_name')[
    'total_revenue'].sum().sort_values(ascending=False)
for buyer, revenue in buyer_revenue.items():
    print(f"{buyer}: ₹{revenue:,.2f}")

# =====================
# ANALYSIS 2
# Revenue by Destination
# =====================
print("\n=== REVENUE BY DESTINATION ===")
dest_revenue = df.groupby('destination')[
    'total_revenue'].sum().sort_values(ascending=False)
for dest, revenue in dest_revenue.items():
    print(f"{dest}: ₹{revenue:,.2f}")

# =====================
# ANALYSIS 3
# Revenue by Block Type
# =====================
print("\n=== REVENUE BY BLOCK TYPE ===")
block_revenue = df.groupby('block_type')[
    'total_revenue'].sum().sort_values(ascending=False)
for block, revenue in block_revenue.items():
    print(f"{block}: ₹{revenue:,.2f}")

# =====================
# ANALYSIS 4
# Yearly Performance
# =====================
print("\n=== YEARLY PERFORMANCE ===")
yearly = df.groupby('year').agg(
    Loads=('load_id', 'count'),
    Cubic_Meters=('cubic_meters', 'sum'),
    Revenue=('total_revenue', 'sum')
).round(2)
for year, row in yearly.iterrows():
    print(
        f"{year}: {row['Loads']} loads | {row['Cubic_Meters']:.1f} m³ | ₹{row['Revenue']:,.2f}")

# =====================
# ANALYSIS 5
# Rainy Season Impact
# =====================
print("\n=== RAINY SEASON IMPACT ===")
seasonal = df.groupby('is_rainy_season').agg(
    Loads=('load_id', 'count'),
    Revenue=('total_revenue', 'sum')
).round(2)
seasonal.index = ['Normal Season', 'Rainy Season']
for season, row in seasonal.iterrows():
    print(f"{season}: {row['Loads']} loads | ₹{row['Revenue']:,.2f}")

# =====================
# ANALYSIS 6
# Best Month for Business
# =====================
print("\n=== BEST MONTHS FOR BUSINESS ===")
df['month_name'] = pd.to_datetime(df['dispatch_date']).dt.strftime('%B')
df['month_num'] = pd.to_datetime(df['dispatch_date']).dt.month
monthly = df.groupby(['month_num', 'month_name'])['total_revenue'].sum()
monthly = monthly.sort_values(ascending=False)
for (num, name), revenue in monthly.items():
    print(f"{name}: ₹{revenue:,.2f}")

# =====================
# ANALYSIS 7
# Dispatch Efficiency
# =====================
print("\n=== DISPATCH EFFICIENCY ===")
print(
    f"Average days from payment to dispatch: {df['dispatch_days'].mean():.1f} days")
print(f"Fastest dispatch: {df['dispatch_days'].min()} day")
print(f"Slowest dispatch: {df['dispatch_days'].max()} days")

# =====================
# ANALYSIS 8
# Overall Summary
# =====================
print("\n=== OVERALL BUSINESS SUMMARY ===")
print(f"Business Period:     2018 - 2021")
print(f"Location:            Narasimhulagudem, Mahabubabad")
print(f"Total Loads:         {len(df)}")
print(f"Total Cubic Meters:  {df['cubic_meters'].sum():.2f} m³")
print(f"Total Revenue:       ₹{df['total_revenue'].sum():,.2f}")
print(f"Avg Revenue/Load:    ₹{df['total_revenue'].mean():,.2f}")
print(f"Total Buyers:        {df['buyer_name'].nunique()}")
print(f"Total Markets:       {df['destination'].nunique()}")
