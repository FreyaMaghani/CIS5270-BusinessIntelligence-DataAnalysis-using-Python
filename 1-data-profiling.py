# -*- coding: utf-8 -*-
"""
Created on Thu May  6 00:18:58 2021

@author: fmama
"""

import pandas as pd



Customer_Churn = pd.read_csv('Customer_Churn.csv')

print(Customer_Churn.head())

print(Customer_Churn.shape)

print(Customer_Churn.info())



Customer_voice_service = pd.read_excel('Customer_voice_service.xlsx')

print(Customer_voice_service.head())

print(Customer_voice_service.shape)

print(Customer_voice_service.info())


