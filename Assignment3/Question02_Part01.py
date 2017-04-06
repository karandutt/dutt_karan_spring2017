
# coding: utf-8

# # Question 2
# - Find out the highest paid departments in each organization group by calculating mean of total compensation for every department.

# In[51]:

# do all the imports
import pandas as pd
from pandas import DataFrame
import sys, os


# In[44]:

#Read in data
#print(os.getcwd())
dataPath = os.getcwd()+'/Data/employee_compensation.csv'
df = pd.read_csv(dataPath)


# In[45]:

df.head()


# In[46]:

col = ['Organization Group'] + ['Department'] + ['Total Compensation']
comp = df[col]
comp.head()


# In[48]:

org = comp['Organization Group'].unique()
print(org)


# In[49]:

holder = []
for each in org:
    temp = comp[comp['Organization Group'] == each]
    deps = temp['Department'].unique()
    for x in deps:
        avg = temp[temp['Department'] == x].mean()
        holder.append((each, x, avg[0]))

avg_compensation = DataFrame(holder, columns=('Organization Group', 
                                            'Department', 
                                            'Avg Total Compensation')).sort_values(by=['Organization Group','Department','Avg Total Compensation'], ascending=False).reset_index(drop=True)
avg_compensation.head()


# In[50]:

#write to csv file
avg_compensation.to_csv('Q2_Part_1.csv',index=False,header=True)


# In[ ]:



