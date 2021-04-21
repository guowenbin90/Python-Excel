import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

#print(df)
#print(df.loc[(df['City']=='Riverside') & (df['First']=='John')])

df['Tax %'] = df['Income'].apply(lambda x: 0.15 if 10000< x < 40000 else 0.2 if 40000 < x < 80000 else .25)


df['Tax owned'] = df['Income']*df['Tax %']
#print(df)
to_drop = ['Area code', 'First', 'Address']
df.drop(columns = to_drop, inplace = True)
#print(df)

df['Test col'] = False
df.loc[df['Income']<60000, 'Test col'] = True
print(df.groupby(['Test col']).mean().sort_values('Income'))
