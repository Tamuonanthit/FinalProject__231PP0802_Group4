# PPNCLN
# Overview: 
- This folder contain file "Salesdata.csv" for calculating RFM values and file "Customerdata.csv" for calculating G value (Geography). These file are extracted from AdventureWorks-Sales.xlsx"
# How to use:
- Download file data and then import to your code folder
# 1: Import libraries 
# 2: Read Salesdata
- Read it by command: df = pd.read_csv("Salesdata.csv")
- Drop unnescessary columns, just store nesscessary data for calculating RFM values, we have " CustomerKey"	"SALE ORDER"	"ORDER DATE"	"Sales Amount" columns left.
- Change column name, the column name is already pretty good, but I prefer use lowercase and use underscore instead of space, for me, it's easier to read and code
# 3: Create RFM table
- Calculate R values and create R table with customer_key 
- Calculate F values and create F table with customer_key 
- Calculate M values and create M table with customer_key 
- Merge R, F, M Table into 1 DataFrame
- ![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/57bd74d5-7c25-4cb5-83a6-5353898b5936)
- Decribe it and we know about count, mean, standard,min,max,quartiles.
# 4: RFM-G
- Drop unesscessary columns, after that we have "country_region"	and calculate "sum_sales_of_country" from monetary 

# 5: EDA RFMG
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/b8bac3a5-789d-4cee-a71f-60fc5c2fe6bb)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/b57e2453-6cd8-4fb5-8f24-93d9f9b5a13b)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/118fd735-fee5-452a-9b53-6b229c929b6b)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/4a391e02-fa3d-4f3d-b4e3-c4f73894924a)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/0da8c064-3faf-4068-9684-60f98d9b8688)
# 6: Calculate RFM score 


