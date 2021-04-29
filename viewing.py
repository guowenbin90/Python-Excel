import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First','Last','Address','City','State','Area code','seven']
#print(df.columns)
#print(df['First'][0:3])
#print(df.iloc[2,1])
wanted_values = df[['First','Last','State']]
stored = wanted_values.to_excel('State_location.xlsx', index=None)