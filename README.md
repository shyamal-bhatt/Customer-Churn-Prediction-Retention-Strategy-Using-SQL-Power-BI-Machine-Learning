# End to End Churn Analysis and Predictive Model using Power BI


## Project Goals

Creating an entire ETL process using a database and Powe BI dashboard to utilize the customers data and achieve the following:

1. Analyze Customer Data at below levels::
   * Demographic
   * Geographic
   * Payment & Account Info
   * Service
2. Study Churn profile and identify areas for Implementing marketing campaings
3. Identify a method to predict future churners. 

## Metrics to be Calculated
1. Total customers
2. Total Churn & Churn Rate
3. New Joiners


## ETL FrameWork

The framework uses below components:
* **CSV file** - This is our source file
* **SQL Server Management Studio** - We will use its inbuilt import wizard to transform & load the data
* **SQL Server Database** - This is where our final data will be loaded and host our data warehouse, tables & views for final usage.

Power BI

Custom Column

Churn Status = if [Customer_Status] = "Churned" then 1 else 0
Monthly Charge Status = if [Monthly_Charge] < 20 then "<20"
                        else if [Monthly_Charge] < 50 then "20-50"
                        else if [Monthly_Charge] < 100 then "50-100"
                        else ">100"