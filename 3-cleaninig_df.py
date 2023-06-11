# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:43:59 2021

@author: fmama
"""

import pandas as pd
import re
import numpy as np


#df = pd.read_csv('Customer_Churn_Reduced.csv')



#print(df.info())

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', False)
pd.set_option('display.expand_frame_repr', False)

# Getting information about rows with Null value in each column

#print(df.isnull().any())
#print(df.loc[df['gender'].isnull()])
#print(df['gender'].value_counts(dropna = False))

#print(df.loc[df['InternetService'].isnull()])

#print(df.loc[df['MonthlyCharges'].isnull()])

#print(df.loc[df['TotalCharges'].isnull()])
'''
# Part1: Deleting rows with missing value in 'gender' column
df = pd.read_csv('Customer_Churn_Reduced.csv')
print(df.loc[df['gender'].isnull()], '\n')
print(df['gender'].value_counts(dropna = False), '\n')

df.dropna(subset=['gender'], inplace = True)
df.to_csv('Customer_Churn_cleaning_part1.csv', index=False)

df = pd.read_csv('Customer_Churn_cleaning_part1.csv')
print(df.loc[df['gender'].isnull()], '\n')
print(df.shape)
'''
# Part2 : Replacing missing values in InternetService column with 'DSL'
'''
df = pd.read_csv('Customer_Churn_cleaning_part1.csv')
print(df.loc[df['InternetService'].isnull()], '\n')
print(df['InternetService'].value_counts(dropna = False))

df['InternetService'].fillna('DSL', inplace= True )
df.to_csv('Customer_Churn_cleaning_part2.csv', index=False)

df = pd.read_csv('Customer_Churn_cleaning_part2.csv')
print(df.loc[df['InternetService'].isnull()], '\n')
print(df['InternetService'].value_counts(dropna = False))
'''
# Part 3: Replacing missing value with the most frequent value in MonthlyCharges
'''
df = pd.read_csv('Customer_Churn_cleaning_part2.csv')
print(df.loc[df['MonthlyCharges'].isnull()], '\n')
print(df['MonthlyCharges'].mode(), '\n')
print(df['MonthlyCharges'].value_counts(dropna = False), '\n')

df['MonthlyCharges'].fillna(df['MonthlyCharges'].mode()[0], inplace= True)
df.to_csv('Customer_Churn_cleaning_part3.csv', index=False)

df = pd.read_csv('Customer_Churn_cleaning_part3.csv')
print(df.loc[df['MonthlyCharges'].isnull()], '\n')
print(df['MonthlyCharges'].value_counts(dropna = False))

'''
# Duplicates

#print(df.duplicated())


# Part 4: Replacing missing value with average value in TotalCharges column

df = pd.read_csv('Customer_Churn_cleaned_part6.csv')
print(df['TotalCharges'].value_counts(dropna = False), '\n')
print("Mean value before changes is: ", round(df['TotalCharges'].mean(),2), '\n')
print("Column type is: ", df['TotalCharges'].dtypes, '\n')

df['TotalCharges'].fillna(df['TotalCharges'].mean(), inplace= True)
df.to_csv('Customer_Churn_cleaned_part4.csv', index=False)

df = pd.read_csv('Customer_Churn_cleaned_part4.csv')
print("Mean value after changes is: ", round(df['TotalCharges'].mean(),2), '\n')
print(df.loc[df['TotalCharges'].isnull()], '\n')


# Part 5: Invalid data types cleaning
#   Finding the problematic cells
'''
df = pd.read_csv('Customer_Churn_cleaning_part3.csv')
df['NewTotalCharges'] = pd.to_numeric(df['TotalCharges'], errors = 'coerce')
print(df.loc[df['NewTotalCharges'].isnull()])
'''
'''
# Part6: Substituting blank for space

df = pd.read_csv('Customer_Churn_cleaning_part3.csv')
print(df['TotalCharges'].value_counts(dropna = False), '\n')

df['TotalCharges'].replace('\s+', np.nan, regex= DTrue, inplace= True)
df.to_csv('Customer_Churn_cleaned_part6.csv', index=False)

df = pd.read_csv('Customer_Churn_cleaned_part6.csv')
print(df['TotalCharges'].value_counts(dropna = False), '\n')
print(df.loc[df['TotalCharges'].isnull()], '\n')
print(df['TotalCharges'].dtypes, '\n')
'''

'''







#print(df.info())

'''










