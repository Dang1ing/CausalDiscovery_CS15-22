import pandas as pd
import numpy as np


df = pd.read_csv('jsj15-22_compulsory.csv')
df.fillna(0, inplace=True)
columns_to_convert = [col for col in df.columns if col != 'xh']
df[columns_to_convert] = df[columns_to_convert].astype(int)
# df = df.drop(columns=['xh'])
df.to_csv('jsj15-22_compulsory.csv', index=False)
