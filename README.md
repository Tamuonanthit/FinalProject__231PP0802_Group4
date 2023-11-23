# PPNCLN
# Overview: 
- This folder contain file "Salesdata.csv" for calculating RFM values and file "Customerdata.csv" for calculating G value (Geography). These file are extracted from AdventureWorks-Sales.xlsx". 
# How to use:
- Download file data and then import to your code folder
# 1: Import libraries 
# 2: Read Salesdata
- Read it by command: df = pd.read_csv("Salesdata.csv")
- Drop unnescessary columns, just store nesscessary data for calculating RFM values: " CustomerKey"	"SALE ORDER"	"ORDER DATE"	"Sales Amount" columns.
- Change column name, the column name is already pretty good, but our team prefer use lowercase and use underscore instead of space, it's easier to read and code
# 3: Create RFM table
- Calculate R values and create R table with customer_key 
- Calculate F values and create F table with customer_key 
- Calculate M values and create M table with customer_key 
- Merge R, F, M Table into 1 DataFrame
- ![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/57bd74d5-7c25-4cb5-83a6-5353898b5936)
- Decribe it to know about count, mean, standard,min,max,quartiles.
# 4: RFM-G
- Drop unesscessary columns, groupby "country_region"	and calculate "sum_sales_of_country" from monetary 
- Add G table to RFM table
# 5: EDA RFMG
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/b8bac3a5-789d-4cee-a71f-60fc5c2fe6bb)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/b57e2453-6cd8-4fb5-8f24-93d9f9b5a13b)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/118fd735-fee5-452a-9b53-6b229c929b6b)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/4a391e02-fa3d-4f3d-b4e3-c4f73894924a)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/0da8c064-3faf-4068-9684-60f98d9b8688)
# 6: Calculate RFM score and Visualization Segment 
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/49b721b6-9235-423f-bdfc-a0a8557fc858)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/991c7cd5-1517-4344-bc31-ce2ce9495b98)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/eaa0d683-932b-4bda-8360-599c4b184356)
# 7: Transformation and Standardization (Z score) 
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/4bea4923-7a1a-4f04-b5b7-ebfa672f226b)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/9908d6ca-f730-403c-b18b-6e693a546edb)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/ec2895ea-d942-4b9d-955d-a7c7c79338ad)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/38960e57-fc72-43d6-a2d3-080f8ec308d0)
 - We chose boxcox transformation because it had lowest standard
 - Then,  StandardScaler boxcox values we had before
# 8: K-mean , Elbow, Silhouette
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/6e6270a4-e82d-446a-8db6-81dfdea0c494)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/e1d20df1-1867-4382-b5f1-782893e5b76d)
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/0032fb72-004a-4685-96b4-5c03ea86346d)
# Box plot to visualize Cluster Id vs Monetary
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/9ca9878a-d44e-4d73-b008-533b5152c810)
# Box plot to visualize cluster Id vs frequency
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/9ad69071-db0b-4a9b-acf2-c7fa5a867f7d)
# Box plot to visualize cluster Id vs recency
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/99fb4ae0-20f1-4822-bd49-4cd1bfea4e26)

# Calculate CLV 
- Import data from AHP and calculate CLV
![image](https://github.com/Tamuonanthit/PPNCLN/assets/118418261/33727993-ea8c-479e-9e76-856a83c3ab81)
