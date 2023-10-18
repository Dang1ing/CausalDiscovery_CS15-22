import pandas as pd
import networkx as nx
import os
# import warnings
# warnings.filterwarnings('ignore')
data = pd.read_csv('t_cj_jsj15_22.csv')
# data.drop(['credit'], axis=1, inplace=True)
data.dropna(subset=['zcj'], inplace=True)
data.drop_duplicates(inplace=True)
# co = data[data['kch'].str.contains('COMP')]
comp_courses = data
comp_courses['kcm'] = data['kcm'].str.strip()

comp_courses.sort_values(by=['xh', 'zcj'], ascending=[
                         True, False], inplace=True)
comp_courses = comp_courses.groupby(['xh', 'kcm']).first().reset_index()

# 透视表，将数据重新排列
pivot_table = pd.pivot_table(comp_courses, values='zcj',
                             index='xh', columns='kcm', aggfunc='sum', fill_value=0)

# 保存结果到文件
pivot_table.to_csv('cs15-22.csv')

# dz = comp.groupby(['xh', 'kcm'], as_index=False).sum()
# da = pd.pivot(dz, index='xh', columns=['kcm'], values='zcj')
# da.fillna(0, inplace=True)
# da.to_csv('jsj15-22_comp.csv')
