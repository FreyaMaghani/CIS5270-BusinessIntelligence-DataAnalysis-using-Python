# -*- coding: utf-8 -*-
"""
Created on Thu May 13 15:18:12 2021

@author: fmama
"""

import pandas as pd

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', False)
pd.set_option('display.expand_frame_repr', False)

df1 = pd.read_excel('Customer_voice_service_Reduced.xlsx')
print(df1.info())

rightdf = df1.iloc[:, [0, 5, 6, 7, 8, 9, 10]]
print(rightdf.info(), '\n')

leftdf = pd.read_csv('Customer_Churn_cleaned_part4.csv')
print(leftdf.info(), '\n')

df = pd.merge(leftdf, rightdf, how= 'left' , on= 'customerID')
print(df, '\n')
df.fillna(0 , inplace= True) 
df.to_csv('Customer_Churn_merged.csv', index=False)

dfmerged = pd.read_csv('Customer_Churn_merged.csv')
print(dfmerged.info(), '\n')
print(dfmerged, '\n')



