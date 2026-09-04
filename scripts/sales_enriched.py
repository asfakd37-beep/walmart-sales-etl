import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine(
    f"postgresql+psycopg2://postgres:{DB_PASSWORD}@localhost:5432/walmart_etl"
)
df = pd.read_sql("SELECT * FROM sales_enriched", engine)

output_path = os.path.join(os.getcwd(), "sales_enriched.csv")
df.to_csv(output_path, index=False)

print("File saved at:", output_path)