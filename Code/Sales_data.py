import pandas as pd

#Importing CSV File 
df = pd.read_csv("C:/Users/GUEST-1/Desktop/Project/sales_data_sample.csv",encoding="latin1")

# CHanging date to datetime
df['ORDERDATE'] = pd.to_datetime(df["ORDERDATE"], errors = 'coerce')

#Renaming Columns
df = df.rename(columns={'SALES': 'SALES_REVENUE'})
df = df.rename(columns={'ORDERNUMBER': 'ORDER_NUMBER'})
df = df.rename(columns={'QUANTITYORDERED': 'QUANTITY_ORDERED'})
df = df.rename(columns={'PRICEEACH': 'PRICE_EACH'})
df = df.rename(columns={'ORDERLINENUMBER': 'ORDER_LINE_NUMBER'})
df = df.rename(columns={'ORDERDATE': 'ORDER_DATE'})
df = df.rename(columns={'PRODUCTLINE': 'PRODUCT_LINE'})
df = df.rename(columns={'CUSTOMERNAME': 'COMPANY_NAME'})
df = df.rename(columns={'ADDRESSLINE1': 'ADDRESS_LINE_1'})
df = df.rename(columns={'ADDRESSLINE2': 'ADDRESS_LINE_2'})
df = df.rename(columns={'POSTALCODE': 'POSTAL_CODE'})
df = df.rename(columns={'CONTACTLASTNAME': 'CONTACT_LAST_NAME'})
df = df.rename(columns={'CONTACTFIRSTNAME': 'CONTACT_FIRST_NAME'})
df = df.rename(columns={'DEALSIZE': 'DEAL_SIZE'})

#Creating a column name monthly sales
month_sales = df.groupby('MONTH_ID')['SALES_REVENUE'].sum().rename('monthly_sales')
df = df.join(month_sales, on='MONTH_ID')

#Top Product Line by Sales Revenue
prod_sales = df.groupby('PRODUCT_LINE')['SALES_REVENUE'].sum().reset_index()
prod_sales = prod_sales.sort_values('SALES_REVENUE', ascending=False).head(10)

#Top Companys names by Sales Revenue
comp_sales = df.groupby('COMPANY_NAME')['SALES_REVENUE'].sum().reset_index()
comp_sales = comp_sales.sort_values('SALES_REVENUE', ascending=False).head(10)

#County Wise Sales Revenue
country_sales = df.groupby('COUNTRY')['SALES_REVENUE'].sum().reset_index()

#Order status wise Revenue
Orders_by_sales = df.groupby('STATUS')['SALES_REVENUE'].sum().reset_index()

# Save to CSV File
df.to_csv('Cleaned_sales_data.csv', index=False)
