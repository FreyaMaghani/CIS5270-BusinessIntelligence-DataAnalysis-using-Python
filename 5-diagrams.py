# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:14:39 2021

@author: fmama
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Customer_Churn_merged.csv')
print(df.info(), '\n')
'''
# Histogram

dfFilter = df.loc[:, 'TotalCharges'] >= 3800

plt.figure(figsize=(10,8))
plt.title('Frequency of Total Charges in 75th Percentile', color='Blue',
          weight='bold', fontsize='16')
df.loc[dfFilter, 'TotalCharges'].plot.hist(bins=10, edgecolor='black')


plt.show()
'''

#Box plot

#yTicks = [x for x in range (0, 9000, 400)]

plt.figure(figsize=(10,8))
plt.title('Distribution of Total Charges', color='Blue',
          weight='bold', fontsize='16')
dfFilter = df.loc[:, 'TotalCall'] >= 1
df.loc[dfFilter, 'TotalCall'].plot.box(fontsize=16)

plt.yticks(ticks=yTicks)
plt.xticks(fontsize=14, weight='bold')

plt.show()

'''
# Bar Chart

df2 = df.iloc[:, [ 8, 9, 10, 11, 12]]

plt.figure(figsize=(10,8))
plt.xticks(fontsize=13)
plt.title("Total Calls based on time of The Day", color='Blue', weight='bold', fontsize=16)
df2.sum().plot.bar() 

yLabel = df2.sum().values
#print(yLabel)
for i, v in enumerate(yLabel):
    plt.text(i - 0.18, v + 2000 , str(v), weight='bold')

plt.show()
'''
'''
# Pie Chart

plt.figure(figsize=(14,10))
df['InternetService'].value_counts().plot(kind='pie', fontsize=16, autopct='%.2f%%')
plt.title("Proportion of Type of Internet Access Service", color='Blue',
          fontweight="bold", fontsize=16)
plt.ylabel(None) 
                                   
plt.show()
'''

'''
# horizontal Bar Chart

df1 = df.groupby('InternetService').tenure.median()
print(df1) 

plt.figure(figsize=(10,6))
df1.plot.barh(title= "Average of Tenure based on Service")
plt.title('Average of Tenure based on Service', color='Blue',
          weight='bold', fontsize='16')
 
plt.xlabel('Tenure',fontsize=13, weight='bold')
plt.ylabel('InternetService', fontsize=13, weight='bold')

evens = [x for x in range (0, 35, 2)]
#print(evens)
plt.xticks(ticks=evens)
plt.yticks(fontsize=13)

plt.show()




'''


