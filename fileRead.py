import pandas as pd
import openpyxl.workbook as workbook

df_excel = pd.read_excel('regions.xlsx')
df_csv = pd.read_csv('Names.csv', header=None)
df_txt = pd.read_csv('data.txt', delimiter='\t')

#print(df_csv)
df_csv.columns = ['Frist','Last','Address','City','State','six','seven']
df_csv.to_excel('modified.xlsx')
