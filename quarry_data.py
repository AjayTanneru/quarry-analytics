import pandas as pd
import numpy as np

np.random.seed(42)

# ==============================
# YOUR REAL BUSINESS DATA
# Black Granite Quarry
# Narasimhulagudem, Mahabubabad
# Telangana, India
# ==============================

# YOUR REAL BUYERS
buyers = [
    'Sri Vishnu Granites Pvt Ltd',
    'Universal Stone Exports',
    'Samantula Granites and Marbles',
    'Sri Satya Surya Company',
    'R P Granites',
    'United Universal Granites'
]

# BUYER DESTINATIONS
# Your buyers exported to these countries
destinations = ['USA', 'China', 'Poland', 'UK', 'India']

# REAL BLOCK TYPES AND PRICES
block_types = {
    'Gangsaw': {
        'price_per_m3': 110000,
        'avg_m3_per_load': 5.0,
        'size': 'Large Slab'
    },
    'Big Block High': {
        'price_per_m3': 100000,
        'avg_m3_per_load': 4.5,
        'size': '240x140 Above'
    },
    'Big Block Low': {
        'price_per_m3': 90000,
        'avg_m3_per_load': 4.0,
        'size': '240x140 Below'
    },
    'Small Block High': {
        'price_per_m3': 80000,
        'avg_m3_per_load': 3.5,
        'size': '200x100 Above'
    },
    'Small Block Low': {
        'price_per_m3': 70000,
        'avg_m3_per_load': 3.0,
        'size': '200x100 Below'
    },
}

# REAL YEARLY DATA
# Normal years: 130-140 m3
# COVID 2020: only 40 m3
# 2021: 120 m3 (left Dec 28)
yearly_data = {
    2018: {'cubic_meters': 130, 'loads': 30},
    2019: {'cubic_meters': 140, 'loads': 30},
    2020: {'cubic_meters': 40,  'loads': 10},
    2021: {'cubic_meters': 120, 'loads': 28},
}

# ==============================
# GENERATE LOADS YEAR BY YEAR
# ==============================

records = []
load_counter = 1

for year, year_info in yearly_data.items():
    total_loads = year_info['loads']
    is_covid_year = (year == 2020)

    # Monthly load distribution
    # Rainy season Jun-Aug = fewer loads
    if is_covid_year:
        monthly_loads = {
            1: 1, 2: 1, 3: 1,
            4: 1, 5: 1,
            6: 0, 7: 0, 8: 0,
            9: 1, 10: 1,
            11: 2, 12: 1
        }
    else:
        monthly_loads = {
            1: 3, 2: 3, 3: 4,
            4: 3, 5: 3,
            6: 1, 7: 1, 8: 1,
            9: 3, 10: 3,
            11: 3, 12: 2
        }

    for month, load_count in monthly_loads.items():

        # 2021 — you left Dec 28, fewer loads in December
        if year == 2021 and month == 12:
            load_count = 2

        for _ in range(load_count):
            day = np.random.randint(1, 28)

            # Make sure no loads after Dec 28 2021
            if year == 2021 and month == 12 and day >= 28:
                day = np.random.randint(1, 27)

            dispatch_date = pd.Timestamp(
                year=year, month=month, day=day)

            # Payment received 1-3 days before dispatch
            payment_days_before = np.random.randint(1, 4)
            payment_date = dispatch_date - pd.Timedelta(
                days=payment_days_before)

            # Pick block type
            block_name = np.random.choice(list(block_types.keys()))
            block_info = block_types[block_name]

            # Cubic meters for this load
            cubic_meters = round(
                np.random.uniform(
                    block_info['avg_m3_per_load'] - 0.5,
                    block_info['avg_m3_per_load'] + 0.5
                ), 2)

            # Price with small negotiation variation
            price = round(
                block_info['price_per_m3'] * np.random.uniform(0.95, 1.05), 2)

            # Total revenue = pure profit
            # No shipping cost — buyer handles everything!
            total_revenue = round(cubic_meters * price, 2)

            # Destination
            # COVID year — mostly domestic India
            if is_covid_year:
                dest = np.random.choice(
                    destinations,
                    p=[0.10, 0.10, 0.10, 0.10, 0.60])
            else:
                dest = np.random.choice(
                    destinations,
                    p=[0.25, 0.25, 0.20, 0.15, 0.15])

            # Rainy season flag
            is_rainy = month in [6, 7, 8]

            records.append({
                'load_id':          'LOAD' + str(load_counter).zfill(4),
                'dispatch_date':    dispatch_date.date(),
                'payment_date':     payment_date.date(),
                'dispatch_days':    payment_days_before,
                'buyer_name':       np.random.choice(buyers),
                'destination':      dest,
                'block_type':       block_name,
                'block_size':       block_info['size'],
                'cubic_meters':     cubic_meters,
                'price_per_m3':     price,
                'total_revenue':    total_revenue,
                'profit':           total_revenue,
                'payment_status':   'Paid',
                'is_rainy_season':  is_rainy,
                'year':             year
            })

            load_counter += 1

df = pd.DataFrame(records)
df = df.sort_values('dispatch_date').reset_index(drop=True)

# Save to CSV
df.to_csv('quarry_exports.csv', index=False)

print("✅ Real Quarry Dataset Created!")
print(f"📍 Location: Narasimhulagudem, Mahabubabad, Telangana")
print(f"🪨 Product: Black Granite Blocks")
print(f"📦 Total Loads: {len(df)}")
print(
    f"📅 Date Range: {df['dispatch_date'].min()} to {df['dispatch_date'].max()}")
print(f"\n📊 Yearly Summary:")
yearly_summary = df.groupby('year').agg(
    Loads=('load_id', 'count'),
    Cubic_Meters=('cubic_meters', 'sum'),
    Revenue=('total_revenue', 'sum')
).round(2)
print(yearly_summary)
print(f"\n💰 Overall Business Summary:")
print(f"Total Revenue:    ₹{df['total_revenue'].sum():,.2f}")
print(f"Total Loads:      {len(df)}")
print(f"Total Buyers:     {df['buyer_name'].nunique()}")
print(f"Total Markets:    {df['destination'].nunique()}")
print(f"\n🏆 Top Buyers:")
print(df.groupby('buyer_name')['total_revenue'].sum().sort_values(
    ascending=False).apply(lambda x: f"₹{x:,.2f}"))
