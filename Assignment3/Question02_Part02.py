
# coding: utf-8

# # Question 2 
# - Find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# - For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value.
# - Display the top 5 Job Families according to this percentage value using df.head().

# In[35]:

# do all the imports
import pandas as pd
from pandas import DataFrame
import sys, os


# In[61]:

#read in data
#print(os.getcwd())
path = os.getcwd()+'/Data/employee_compensation.csv'
df = pd.read_csv(path)


# In[54]:

df.head()


# In[62]:

df = df[df['Year Type'] == 'Calendar']
cols = ['Year'] + list(df.loc[:,'Salaries':'Total Compensation'])
sal = df[cols]


# In[63]:

elist = []
for each in df['Year'].unique():
    temp = sal[sal['Year'] == each]
    vals = temp.mean()
    elist.append((each, 
                   vals['Salaries'],
                   vals['Overtime'],
                   vals['Other Salaries'],
                   vals['Total Salary'],
                   vals['Retirement'],
                   vals['Health/Dental'],
                   vals['Other Benefits'],
                   vals['Total Benefits'],
                   vals['Total Compensation']))

avg_salary = DataFrame(elist, columns=('Year',
                                          'Avg Salaries',
                                          'Avg Overtime',
                                          'Avg Other Salary',
                                          'Avg Total Salary',
                                          'Avg Retirment',
                                          'Avg Health/Dental',
                                          'Avg Other Benefits',
                                          'Avg Total Benefits',
                                          'Avg Total Compensation')).sort_values(by='Year').reset_index(drop=True)
avg_salary.head()


# In[64]:

elist = []
for each in df['Job Family'].unique():
    tBen = df[df['Job Family'] == each]['Total Benefits'].mean()
    tComp = df[df['Job Family'] == each]['Total Compensation'].mean()
    percentage = (tBen/tComp)*100
    elist.append((each,tBen,tComp,percentage))
    
compensation = DataFrame(elist, columns=('Job Family',
                                          'Total Benefits',
                                          'Total Compensation',
                                          'Percentage Ben/Comp')).sort_values(by='Percentage Ben/Comp',ascending=False).reset_index(drop=True)
compensation.head()


# In[65]:

#write to csv file
compensation.to_csv('Q2_Part_2.csv',index=False,header=True)

