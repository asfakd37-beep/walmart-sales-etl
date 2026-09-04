import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
import pandas as pd
from sqlalchemy import create_engine

# Load data
df = pd.read_csv(r"C:\Users\ASFAK\OneDrive\文件\IBM data science notes\projects\walmart-sales-etl\data\raw\stores.csv")

# Connect to PostgreSQL
engine = create_engine(
    f"postgresql+psycopg2://postgres:{DB_PASSWORD}@localhost:5432/walmart_etl"
)

# OPTIONAL: clean column names (good habit)
df.columns = [col.lower() for col in df.columns]

# Load into SQL
df.to_sql(
    "dim_store",
    engine,
    if_exists="append",   # appends to table if exists
    index=False
)

print("dim_store loaded successfully")