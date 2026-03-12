#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


csv_file = 'PlayTENNIS.csv' 
df_csv = pd.read_csv(csv_file)
json_file = 'sample_data.json' 
df_json = pd.read_json(json_file)
print("CSV Data:\n", df_csv.tail())
print("\nJSON Data:\n", df_json.head())


# In[3]:


# B) Identifiying Missing values and dropping
df_cleaned = df_csv.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_cleaned)
df_cleaned = df_csv.dropna(axis=1)
print("\nDataFrame after dropping columns with missing values:")
print(df_cleaned)
df.replace(["NA", ""], np.nan, inplace=True)--- if in the data set you have written NA *


# In[4]:


print("\nMissing Values in the Dataset:") # Printing the Count of missing terms)
print(df_csv.isnull().sum())


# In[5]:


# C) Handle missing value using mode and mean.
df_csv['temp'].fillna(df_csv['temp'].mode()[0], inplace=True) # Filling missing value with Mode)
print("\nDataset after filling missing categorical values with mode:")
print(df_csv)


# In[6]:


# Example with mean
df_csv['SNo'].fillna(df_csv['SNo'].mean(), inplace=True)
print("\nDataset after filling missing numerical values with mean:")
print(df_csv)


# In[7]:


# C) Outliers
import matplotlib.pyplot as plt
import seaborn as sns
sns.boxplot(data=df_csv['no_of_people'])
plt.show()


# In[10]:


# For Deleting the Outliers Method 1) Interquartile Range (IQR)
Q1 = df_csv['no_of_people'].quantile(0.25)
Q3 = df_csv['no_of_people'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 3 * IQR
upper_bound = Q3 + 3 * IQR
#print("print" , [(df_csv['no_of_people'] < lower_bound) | (df_csv['no_of_people'] > upper_bound)])
extreme_outliers = df_csv[(df_csv['no_of_people'] < lower_bound) | (df_csv['no_of_people'] > upper_bound)]


# In[12]:


df_cleaned = df_csv[(df_csv['no_of_people'] >= lower_bound) & (df_csv['no_of_people'] <= upper_bound)]


# In[13]:


import seaborn as sns
sns.boxplot(data=df_cleaned['no_of_people'])


# In[14]:


# D) manipulate and transform data using functions like filtering , sorting and grouping.
# Filtering
filtered_df = df_csv[df_csv['no_of_people'] > 2]
print(filtered_df)


# In[15]:


# sorting
sorted_df_desc = df_csv.sort_values(by='no_of_people', ascending=False)
print(sorted_df_desc)


# In[16]:


# Grouping
grouped_df = df_csv.groupby('outlook').size()
print(grouped_df)


# In[ ]:




