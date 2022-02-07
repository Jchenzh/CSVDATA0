import os
import csv
import pandas as pd


path = 'Data/TPT-B30R3030A-SN0426500002-LatestData'
doclist = os.listdir(path)

dic = {}
for datacsv in doclist:
    print(datacsv)
    with open(f'Data/TPT-B30R3030A-SN0426500002-LatestData/{datacsv}', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dic[f"{datacsv}_{row['Index']}"] = row

print(dic)
df = pd.DataFrame(dic)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
print(df.T)

df.T.to_csv("midterm.csv")
