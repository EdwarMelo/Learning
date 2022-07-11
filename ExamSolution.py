#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 19:09:57 2022

@author: edwar_melo
"""

#%%

def findGolomb(n):
    # base case
    if (n == 1):
        return 1
    # Recursive Step
    return 1 + findGolomb(n -
    findGolomb(findGolomb(n - 1)))
# Print the first n term
# of Golomb Sequence
def printGolomb(n):
    # Finding first n terms of
    # Golomb Sequence.
    for i in range(1, n + 1):
        print(findGolomb(i))

printGolomb(1001)
 
sumDigit, extNum = 0, 0
# numEntero = 123
lista = [x for x in range(5000)]
nums = []
for numEntero in lista:
    sumDigit, extNum = 0, 0
    
    if numEntero != 0:
        extNum = numEntero % 10
        numEntero //= 10
        sumDigit += extNum
        nums.append(extNum)
        # if sumDigit == 16:
        # print("La suma de los digitos es: {}".format(sumDigit))

# %% 
# =============================================================================
# Examen
# =============================================================================

import os 
import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

# %%

data1 = pd.read_csv("https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/COVID19_clinical_trials.csv")

data1.head()
data1.columns
data1.loc[data1.Conditions == "covid19"].shape[0] #6
data1.loc[data1.Conditions == "Covid19"].shape[0] #657
data1.loc[data1.Conditions == "covid19"].shape[0] + data1.loc[data1.Conditions == "Covid19"].shape[0]
# Pregunta 3 : 663

data1.Gender.unique()
data1.loc[data1.Gender == "Female"].shape[0] #162
data1.loc[data1.Gender == "Male"].shape[0] #44
data1.loc[data1.Gender == "Female"].shape[0] + data1.loc[data1.Gender == "Male"].shape[0]
# Pregunta 5 : 206

# %%

data2 = pd.read_csv("https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/flights_Clase11_ML_EPC.csv")

data2.columns
data2.groupby("WEEKDAY").agg({"CANCELLED":"sum"})
# Pregunta 6 : 211,120,102,105,97,98,148

df1=data2.groupby(["ORG_AIR","DEST_AIR"]).agg({"DIVERTED":"count"}).reset_index()
df1.loc[df1.DEST_AIR=="KOA"]
# Pregunta 7 : 55

data2.DEST_AIR.unique().shape[0]
# Pregunta 8 : 271

data2.isna().sum().sum()
# Pregunta 9 : 2869

help(data1.Conditions.unique)
dir(lista)
type()
