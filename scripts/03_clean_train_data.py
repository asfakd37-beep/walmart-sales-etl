import pandas as pd
import numpy as np

# EXTRACT
path = r"C:\Users\ASFAK\OneDrive\文件\IBM data science notes\projects\walmart-sales-etl\data\raw\train.csv"

def extract_data(path):
    df = pd.read_csv(path)
    print(df.head(3))
    return df

# VALIDATE
def validate_data(df): 
    print("\nDATA VALIDATION")
    
    total_rows = len(df)
    missing_values = df.isnull().sum().sum()
    
    duplicate_count = df.duplicated(subset=["Store", "Dept", "Date"]).sum()
    
    negative_sales = (df["Weekly_Sales"] < 0).sum()
    negative_sales_pct = (negative_sales / total_rows) * 100
    
    print("Total rows:", total_rows)
    print("Missing values:", missing_values)
    
    print("Duplicate (Store+Dept+Date):", duplicate_count)
    
    print("Negative sales:", negative_sales)
    print("Negative sales %:", round(negative_sales_pct, 2), "%")
    
    # Business warning flags
    if negative_sales_pct > 5:
        print("⚠ WARNING: High return/negative sales ratio")
    
    return df

def check_grain_integrity(df):
    print("\nGRAIN INTEGRITY CHECK")
    
    duplicate_rows = df.duplicated(subset=["Store", "Dept", "Date"]).sum()
    
    total_keys = df.shape[0]
    unique_keys = df.drop_duplicates(subset=["Store", "Dept", "Date"]).shape[0]
    
    print("Total rows:", total_keys)
    print("Unique grain rows:", unique_keys)
    print("Duplicate grain rows:", duplicate_rows)
    
    if duplicate_rows > 0:
        print("⚠ WARNING: Grain violation detected!")
    else:
        print("✔ Grain integrity is clean")
    
    return df


# TRANSFORM
def transform_data(df):
    print("\nTRANSFORM")
    
    df["Date"] = pd.to_datetime(df["Date"])
    
    return df



#load
def load_data(df, output_path):
    df.to_csv(output_path, index=False)
    print("\nData saved to:", output_path)


# main pipeline
def run_pipeline():
    input_path = r"C:\Users\ASFAK\OneDrive\文件\IBM data science notes\projects\walmart-sales-etl\data\raw\train.csv"
    output_path = r"C:\Users\ASFAK\OneDrive\文件\IBM data science notes\projects\walmart-sales-etl\data\processed\fact_sales_clean.csv"
    
    df = extract_data(input_path)
    df = validate_data(df)
    df = transform_data(df)
    load_data(df, output_path)


if __name__ == "__main__":
    run_pipeline()