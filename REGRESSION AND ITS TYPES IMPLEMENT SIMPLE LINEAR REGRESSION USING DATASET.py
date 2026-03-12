#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
from sklearn import linear_model

# Load dataset
df = pd.read_csv(r'D:\Vandana_Mam\TYCS\Term-II\Pract\Pract_6\House_Pricing_Multivariables.csv')

# Display dataset
print(df)

# Find mean of Floors
mean_f = df['Floors'].mean()
mean_f1 = round(mean_f)

# Fill missing values in Floors
df['Floors'] = df['Floors'].fillna(mean_f1)
print("Mean Floors:", mean_f1)

print(df)

# Find mean of Grade
mean_g = df['Grade'].mean()
mean_g1 = round(mean_g)

# Fill missing values in Grade
df['Grade'] = df['Grade'].fillna(mean_g1)
print("Mean Grade:", mean_g1)

print(df)

# Create Linear Regression Model
reg = linear_model.LinearRegression()

# Train the model
reg.fit(
    df[['Bedrooms', 'Bathrooms', 'Sqft_living', 'Floors', 'Grade', 'Sqft_above', 'Sqft_basement']],
    df['Price']
)

# Display coefficients
print("Coefficients:", reg.coef_)

# Display intercept
print("Intercept:", reg.intercept_)


# In[ ]:




