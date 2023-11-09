import pandas as pd
data = pd.read_excel(r"AdventureWorks Sales.xlsx")
SalesOrder_data = pd.read_excel(r"AdventureWorks Sales.xlsx",sheet_name="Sales Order_data")
SalesOrder_columns = pd.DataFrame(SalesOrder_data,columns=["CustomerKey","Sales Order"])
Sales_data = pd.read_excel(r"AdventureWorks Sales.xlsx",sheet_name="Sales_data")
Sales_columns = pd.DataFrame(Sales_data,columns=["CustomerKey","OrderDateKey","Sales Amount"])
Customer_data = pd.read_excel(r"AdventureWorks Sales.xlsx",sheet_name="Customer_data")
Customer_columns = pd.DataFrame(Customer_data,columns=["CustomerKey","Country-Region"])
print(Sales_columns)