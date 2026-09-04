import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
import pandas as pd
from sqlalchemy import create_engine

# Load features data
df = pd.read_csv(r"C:\Users\ASFAK\OneDrive\文件\IBM data science notes\projects\walmart-sales-etl\data\raw\features.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Optional cleanup (good practice)
df.columns = [col.lower() for col in df.columns]

# Connect to PostgreSQL
engine = create_engine(
    f"postgresql+psycopg2://postgres:{DB_PASSWORD}@localhost:5432/walmart_etl"
)

# Load into SQL
df.to_sql(
    "features_raw",
    engine,
    if_exists="append",   # appends to table if exists
    index=False,
    chunksize=5000,
    method="multi"
)

print("features_raw loaded successfully")
print("Rows loaded:", len(df))