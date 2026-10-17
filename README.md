Walmart Sales ETL and Analytics Project

Project Overview

This project builds an end-to-end retail data pipeline using Walmart sales data.

The objective is to transform raw sales and store-level datasets into an analytics-ready structure, load the data into PostgreSQL, perform SQL-based business analysis, and visualize the results using Tableau.

The project focuses on understanding sales performance, seasonality, store and department behaviour, holiday effects, and the relationship between sales and external factors such as temperature, CPI, unemployment, and fuel prices.


Project Workflow:
Raw CSV Data
→ Python Data Exploration
→ Data Quality Checks
→ Data Cleaning and Transformation
→ PostgreSQL Loading
→ SQL Analysis and Data Enrichment
→ Tableau Dashboard



Dataset
The project uses four Walmart datasets:



`train.csv` historical weekly sales by store and department

`test.csv` - future periods without sales values

`features.csv` - economic, holiday, weather, and markdown information

`stores.csv` - store type and size information



The main training dataset contains approximately 421,000 weekly sales records.

Raw and processed CSV files are excluded from this GitHub repository through `.gitignore`.



Technologies Used:
1) Python
2) Pandas
3) PostgreSQL
4) SQLAlchemy
5) psycopg2
6) SQL
7) Tableau
8) Git
9) GitHub


Project Structure:
```text

walmart-sales-etl/

│

├── data/

│   ├── raw/

│   └── processed/

│

├── scripts/

│   ├── 01\_data\_exploration.py

│   ├── 02\_data\_quality\_checks.py

│   ├── 03\_clean\_train\_data.py

│   ├── 04\_test\_db\_connection.py

│   ├── 05\_load\_dim\_store.py

│   ├── 06\_load\_fact\_sales.py

│   ├── 07\_load\_features\_raw.py

│   └── sales\_enriched.py

│

├── sql/

│   └── walmart\_queries.sql

│

├── dashboard/

│   └── walmart\_sales\_dashboard.twb

│

├── screenshots/

├── docs/

├── .gitignore

└── README.md

```



ETL Process

Extract

The raw Walmart CSV files are loaded using Python and Pandas.

Initial exploration is performed to understand:



dataset size:

\* column structure

\* data types

\* missing values

\* sample records



\### Transform



The sales dataset is validated and cleaned before loading into the database.



Checks include:



\* missing values

\* duplicate records

\* date formatting

\* negative sales values

\* Store, Department and Date combinations



The cleaned sales data is stored as an intermediate processed dataset.



\### Load



Python and SQLAlchemy are used to load the cleaned datasets into PostgreSQL.



The database includes sales data, store information and external business features.



Sales data is enriched by joining sales records with features using:



`Store + Date`



\## SQL Analysis



SQL queries are used to investigate:



\* total sales by store

\* holiday vs non-holiday sales

\* department performance

\* monthly sales trends

\* store-level seasonality

\* feature data

\* enriched sales data



The SQL queries are available in:



`sql/walmart\_queries.sql`



\## Tableau Dashboard



The project includes a Tableau dashboard for visual analysis.



The dashboard contains views for:



\* sales trends over time

\* store performance

\* holiday sales comparison



The Tableau workbook is available at:



`dashboard/walmart\_sales\_dashboard.twb`



\## Key Findings



The analysis identified several important patterns.



\* Store performance varies significantly across the Walmart network.

\* Store 20 generated the highest total sales in the analysed dataset.

\* Holiday weeks recorded higher average weekly sales than non-holiday weeks.

\* Departments differ substantially in total sales performance.

\* Sales show clear seasonal patterns, including strong year-end peaks.

\* Temperature, CPI, unemployment and fuel prices show relationships with sales, although these relationships should be interpreted as associations rather than direct causal effects.



\## Data Privacy and Credentials



Database credentials are stored locally using environment variables and are not included in the repository.



The `.env` file and raw/processed CSV datasets are excluded through `.gitignore`.



\## Future Improvements



Future development could include:



\* additional Tableau visualizations

\* markdown promotion analysis

\* automated database table creation

\* stronger validation checks

\* forecasting models

\* cloud deployment

\* automated ETL scheduling



\## Purpose



This project was developed as a portfolio project to demonstrate practical skills in:



\* data cleaning

\* ETL pipeline development

\* relational data modelling

\* PostgreSQL

\* SQL analytics

\* business insight generation

\* Tableau dashboard development

\* Git and GitHub version control



