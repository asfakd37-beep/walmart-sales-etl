import pandas as pd

files = [
    r"C:\Users\ASFAK\OneDrive\文件\IBM data science notes\projects\walmart-sales-etl\data\raw\train.csv",
    r"C:\Users\ASFAK\OneDrive\文件\IBM data science notes\projects\walmart-sales-etl\data\raw\test.csv",
    r"C:\Users\ASFAK\OneDrive\文件\IBM data science notes\projects\walmart-sales-etl\data\raw\features.csv",
    r"C:\Users\ASFAK\OneDrive\文件\IBM data science notes\projects\walmart-sales-etl\data\raw\stores.csv"
]

for file in files:
    print(f"FILE: {file}")

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFirst 5 Rows:")
    print(df.head())