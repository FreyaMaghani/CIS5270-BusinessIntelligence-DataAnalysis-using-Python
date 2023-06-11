# -*- coding: utf-8 -*-
"""
Created on Sat May  8 15:08:40 2021

@author: fmama
"""

import pandas as pd
'''
Customer_voice_service = pd.read_excel('Customer_voice_service.xlsx')

columLabel = list(Customer_voice_service.columns)

print(columLabel)

df1 = Customer_voice_service.drop(['SeniorCitizen', 'MaritalStatus', 'Dependents',
                                    'PhoneService', 'MultipleLines', 'OnlineSecurity', 
                                    'OnlineBackup', 'DeviceProtection',
                                    'TechSupport', 'StreamingTV', 'StreamingMovies',
                                    'Contract', 'PaperlessBilling',
                                    'InternationalPlan', 'VoiceMailPlan', 
                                    'NumbervMailMessages', 'TotalDayMinutes', 
                                    'TotalEveMinutes', 'TotalNightMinutes', 'TotalIntlMinutes', 
                                    'Churn'], axis =1)


df1.to_excel('Customer_voice_service_Reduced.xlsx', index=False)

Customer_voice_service_Reduced = pd.read_excel('Customer_voice_service_Reduced.xlsx')
print(Customer_voice_service_Reduced.head())

'''

'''
Customer_Churn = pd.read_csv('Customer_Churn.csv')
#Retreiving the list of columns
colLabels = list(Customer_Churn.columns)

#print(colLabels)

df = Customer_Churn.drop(['SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 
                          'MultipleLines', 'OnlineSecurity',
                          'OnlineBackup', 'DeviceProtection', 
                          'TechSupport', 'StreamingTV', 'StreamingMovies',
                          'PaperlessBilling','Churn'], axis=1)

df.to_csv('Customer_Churn_Reduced.csv', index=False)
'''
Customer_Churn_Reduced = pd.read_csv('Customer_Churn_Reduced.csv')

print(Customer_Churn_Reduced.head())






