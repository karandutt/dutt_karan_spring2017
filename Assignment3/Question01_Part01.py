
# coding: utf-8

# # Question 1
# - For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City

# In[78]:

#do all the imports
import pandas as pd
from pandas import DataFrame
import sys, os, datetime


# In[79]:

#read in data
#print(os.getcwd())
dataPath = os.getcwd()+'/Data/vehicle_collisions.csv'
df = pd.read_csv(dataPath)


# In[80]:

#Converts the date column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])


# In[81]:

#Create new dataframe with only entries from 2016
zoo16 = df[(df['DATE'] >= '2016-01-01') & (df['DATE'] <= '2016-12-31')]


# In[82]:

#Create a new colum representing the month of the colision
zoo16['MONTH'] = zoo16['DATE'].apply(lambda x : x.strftime('%b'))


# In[83]:

#Create a list of all unique months in the collisions dataFrame from 2016
mon = zoo16['MONTH'].unique()


# In[84]:

#create dataframe with months, accidents in manhattan, accidents in NYC and number of accidents in Manhattan compared to nyc

data = {'MONTH':[],'MANHATTAN':[],'NYC':[],'PERCENTAGE':[]} #data holder
for each in mon:
    thisMonth = zoo16[zoo16['MONTH'] == each] #Create new dataFrame of only given month
    nyc = len(thisMonth) #count NYC collisions
    man = len(thisMonth[thisMonth['BOROUGH'] == 'MANHATTAN']) #count Manhattan collisions
    perc = man/nyc #calculate percentage
    
    #store data
    data['MONTH'].append(each)
    data['MANHATTAN'].append(man)
    data['NYC'].append(nyc)
    data['PERCENTAGE'].append(perc)
    
dframe = DataFrame(data, columns=['MONTH','MANHATTAN','NYC','PERCENTAGE'])
dframe.head()


# In[85]:

#write to csv file
dframe.to_csv('Q1_Part_1.csv',index=False,header=True)

