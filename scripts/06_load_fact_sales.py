import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
import pandas as pd
from sqlalchemy import create_engine

# Load cleaned fact data
df = pd.read_csv(r"C:\Users\ASFAK\OneDrive\文件\IBM data science notes\projects\walmart-sales-etl\data\processed\fact_sales_clean.csv")

# Ensure correct data type for Date
df['Date'] = pd.to_datetime(df['Date'])

# Connect to PostgreSQL
engine = create_engine(f"postgresql+psycopg2://postgres:{DB_PASSWORD}@localhost:5432/walmart_etl")

try:
    with engine.begin() as conn:
        df.to_sql(
            "fact_sales",
            con=conn,
            if_exists="append",
            index=False,
            method="multi"
        )

    print("fact_sales loaded successfully")

except Exception as e:
    print(f"Load failed: {type(e).__name__}: {e}")
    raise

# Load into SQL
df.to_sql(
    "fact_sales",
    engine,
    if_exists="append",   # appends to table if exists
    index=False,
    chunksize=10000,   # important for large data
    method="multi"
)

print("fact_sales loaded successfully")
print("Rows loaded:", len(df))