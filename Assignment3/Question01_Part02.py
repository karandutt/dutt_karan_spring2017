
# coding: utf-8

# # Question 1
# - For each borough, find out distribution of each collision scale. (One car involved? Two? Three? or more?) (From 2015 to present)
# - Display a few rows of the output use df.head().

# In[15]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os


# In[14]:

#Read in data
#print(os.getcwd())
dataPath = os.getcwd()+'/Data/vehicle_collisions.csv'
df = pd.read_csv(dataPath)


# In[12]:

df1 = DataFrame(columns = ['ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED'])

df1['ONE_VEHICLE_INVOLVED'] = df.groupby(['BOROUGH'])['VEHICLE 1 TYPE'].count()
df1['TWO_VEHICLES_INVOLVED'] = df.groupby(['BOROUGH'])['VEHICLE 2 TYPE'].count() + df1['ONE_VEHICLE_INVOLVED']
df1['THREE_VEHICLES_INVOLVED'] = df.groupby(['BOROUGH'])['VEHICLE 3 TYPE'].count() + df1['TWO_VEHICLES_INVOLVED']
df1['MORE_VEHICLES_INVOLVED'] = df.groupby(['BOROUGH'])['VEHICLE 4 TYPE'].count() + df.groupby(['BOROUGH'])['VEHICLE 5 TYPE'].count()+df1['THREE_VEHICLES_INVOLVED']
df1


# In[13]:

#write to csv
df1.to_csv('Q1_Part2.csv')

