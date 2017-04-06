# coding: utf-8

# In[9]:

import csv
import pandas as pd
import numpy as np
from pandas import DataFrame
import datetime
import calendar


# In[10]:

#print(os.getcwd())
path = os.getcwd()+'/Data/movies_awards.csv'
df = pd.read_csv(path))


# In[26]:

df= DataFrame(file, columns = ['Awards'])
df = df.dropna() 
df['Awards_won']= df['Awards'].str.extract('(\d+) win',expand = True)
df['Awards_nominated']  = df['Awards'].str.extract('(\d+) nomination',expand = True)
df['Prime_Awards_won']  = df['Awards'].str.extract('Won (\d+) Primetime',expand = True)
df['Prime_Awards_nominated'] = df['Awards'].str.extract('Nominated for (\d+) PrimeTime',expand = True)
df['Bafta_Awards_won']  = df['Awards'].str.extract('Won (\d+) BAFTA',expand = True)
df['Bafta_Awards_nominated'] = df['Awards'].str.extract('Nominated for (\d+) BAFTA',expand = True)
df['Oscar_Awards_won']  = df['Awards'].str.extract('Won (\d+) Oscar',expand = True)
df['Oscar_Awards_nominated'] = df['Awards'].str.extract('Nominated for (\d+) Oscar',expand = True)
df['GoldenGlobe_Awards_won']  = df['Awards'].str.extract('Won (\d+) Golden Globe',expand = True)
df['GoldenGlobe_Awards_nominated'] = df['Awards'].str.extract('Nominated for (\d+) Golden Globe',expand = True)


# In[38]:

df = df.fillna(0)
df


# In[51]:

df['Awards_won'] = df['Awards_won'].astype(str).astype(int)
df['Awards_nominated'] =df['Awards_nominated'].astype(str).astype(int) 
df['Prime_Awards_won'] = df['Prime_Awards_won'].astype(str).astype(int)
df['Prime_Awards_nominated']=df['Prime_Awards_nominated'].astype(str).astype(int)
df['Bafta_Awards_won']=df['Bafta_Awards_won'].astype(str).astype(int) 
df['Bafta_Awards_nominated']=df['Bafta_Awards_nominated'].astype(str).astype(int)
df['Oscar_Awards_won']=df['Oscar_Awards_won'].astype(str).astype(int) 
df['Oscar_Awards_nominated']=df['Oscar_Awards_nominated'].astype(str).astype(int)
df['GoldenGlobe_Awards_won']=df['GoldenGlobe_Awards_won'].astype(str).astype(int)
df['GoldenGlobe_Awards_nominated']=df['GoldenGlobe_Awards_nominated'].astype(str).astype(int)


# In[62]:

df['Awards_won'] = df['Awards_won']+df['Prime_Awards_won']+df['Bafta_Awards_won']+df['Oscar_Awards_won']+df['GoldenGlobe_Awards_won']
df['Awards_nominated']=df['Awards_nominated']+df['Prime_Awards_nominated']+df['Bafta_Awards_nominated']+df['Oscar_Awards_nominated']+df['GoldenGlobe_Awards_nominated']


# In[83]:

print(df.head())


# In[124]:

df.to_csv('Question04_Part_1.csv')


# In[ ]: