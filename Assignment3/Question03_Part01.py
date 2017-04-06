
# coding: utf-8

# # Question 3
# - Calculate the average score for each team which host the game and win the game.

# In[16]:

import pandas as pd
import numpy as np
from pandas import DataFrame
import os


# In[20]:

#Read in data
#print(os.getcwd())
path = os.getcwd()+'/Data/cricket_matches.csv'
df = pd.read_csv(path)


# In[21]:

df.head()


# In[26]:

df1 = DataFrame(df, columns = ['home','winner','innings1_runs','innings2_runs','innings1','innings2','score','avg_score'])
df2 = DataFrame(columns = ['avg_score',])
df1 = df1[df1['home']==(df1['winner'])]
df1['score'] = df1['innings1_runs'].where(df1['home'] == df1['innings1'], df1['innings2_runs'])
df2['avg_score'] = df1.groupby('home')['score'].mean()
df2 #gives all the data with the avg_score


# In[27]:

#write to csv file
df2.to_csv('Q2_Part_2.csv',index=False,header=True)

