# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:01:43 2021

@author: fmama
"""

import pandas as pd



df = pd.read_csv('Customer_Churn_merged.csv')
#print(df.info(), '\n')


#print("The summary statistics of the column {0} is: ".format(df.columns[13]),'\n')
#print("{0}".format(df.iloc[:,[13]].describe()),'\n')

dfFilter = df.loc[:, 'TotalCall'] >= 1
print("The centrality Tendency for the column 'TotalCalls'")

print("The Average of the column {0} is: {1}".format(df.columns[13], round(df.loc[dfFilter,['TotalCall']].mean(), 2)),'\n')

print("The Median of the column {0} is: {1}".format(df.columns[13], round(df.loc[dfFilter,['TotalCall']].median(), 2)),'\n')

print("The Mode of the column {0} is: {1}".format(df.columns[13], round(df.loc[dfFilter,['TotalCall']].mode(), 2)),'\n')

'''
print("The Dispersion for the column 'TotalCalls'")

print("The Min of the column {0} is: {1}".format(df.columns[13], df.iloc[:,[13]].min()),'\n')

print("The Max of the column {0} is: {1}".format(df.columns[13], df.iloc[:,[13]].max()),'\n')

print("The Variance of the column {0} is: {1}".format(df.columns[13], round(df.iloc[:,[13]].var(), 2)),'\n')

print("The Standard Deviation of the column {0} is: {1}".format(df.columns[13], round(df.iloc[:,[13]].std(), 2)),'\n')

print("The Mean Absolute Deviation of the column {0} is: {1}".format(df.columns[13], round(df.iloc[:,[13]].mad(), 2)),'\n')

print("The Skewness of the column {0} is: {1}".format(df.columns[13], df.iloc[:,[13]].skew()),'\n')
'''





