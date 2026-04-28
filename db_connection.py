import psycopg2
import pandas as pd

# ================================
# FACE 2 - Connect Python to PostgreSQL
# Black Granite Quarry Analytics
# ================================

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        database="quarry_analytics",
        user="postgres",
        password="Ajay@1256"
    )

    print("Connected to PostgreSQL successfully!")
    print("=" * 50)

    # Load all tables into DataFrames
    buyers_df = pd.read_sql("SELECT * FROM buyers", conn)
    blocks_df = pd.read_sql("SELECT * FROM blocks", conn)
    loads_df = pd.read_sql("SELECT * FROM loads", conn)
    payments_df = pd.read_sql("SELECT * FROM payments", conn)
    market_df = pd.read_sql("SELECT * FROM market_performance", conn)

    # Verify data completeness
    print("DATA COMPLETENESS REPORT")
    print("=" * 50)
    print(f"Buyers:             {len(buyers_df)} records")
    print(f"Blocks:             {len(blocks_df)} records")
    print(f"Loads:              {len(loads_df)} records")
    print(f"Payments:           {len(payments_df)} records")
    print(f"Market Performance: {len(market_df)} records")
    print("=" * 50)

    # Show first 3 loads
    print("\nFIRST 3 EXPORT LOADS:")
    print(loads_df.head(3).to_string())

    # Show all buyers
    print("\nALL BUYERS:")
    print(buyers_df[['buyer_name', 'country']].to_string())

    # Show all block types
    print("\nALL BLOCK TYPES:")
    print(blocks_df[['block_type', 'block_size', 'price_per_m3']].to_string())

    # Close connection
    conn.close()
    print("\n Connection closed successfully!")

except Exception as e:
    print(f" Error: {e}")