import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")

from sqlalchemy import create_engine

# Replace YOUR_PASSWORD with your PostgreSQL password
engine = create_engine(
    f"postgresql+psycopg2://postgres:{DB_PASSWORD}@localhost:5432/walmart_etl"
)

try:
    with engine.connect() as conn:
        print("Connection successful!")
except Exception as e:
    print("Connection failed!")
    print(e)