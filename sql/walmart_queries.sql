

SELECT
    "Store",
    SUM("Weekly_Sales") AS total_sales
FROM fact_sales
GROUP BY "Store"
ORDER BY total_sales DESC;

SELECT
    "IsHoliday",
    AVG("Weekly_Sales") AS avg_sales
FROM fact_sales
GROUP BY "IsHoliday";

SELECT
    "Dept",
    SUM("Weekly_Sales") AS total_sales
FROM fact_sales
GROUP BY "Dept"
ORDER BY total_sales DESC;


SELECT
    DATE_TRUNC('month', "Date") AS month,
    SUM("Weekly_Sales") AS total_sales
FROM fact_sales
GROUP BY month
ORDER BY month;

SELECT
    "Store",
    DATE_TRUNC('month', "Date") AS month,
    SUM("Weekly_Sales") AS total_sales
FROM fact_sales
GROUP BY "Store", DATE_TRUNC('month', "Date")
ORDER BY "Store", month;

SELECT *
FROM features_raw
LIMIT 1; 

SELECT
    f."Store",
    f."Dept",
    f."Date",
    f."Weekly_Sales",
    f."IsHoliday",
    fe.temperature,
    fe.fuel_price,
    fe.markdown1,
    fe.markdown2,
    fe.markdown3,
    fe.markdown4,
    fe.markdown5,
    fe.cpi,
    fe.unemployment
FROM fact_sales f
JOIN features_raw fe
    ON f."Store" = fe.store
   AND f."Date" = fe.date;


SELECT *
FROM sales_enriched
LIMIT 1;
