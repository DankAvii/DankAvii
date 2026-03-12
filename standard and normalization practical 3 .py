#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


# In[2]:


# Define the data
data = {
    'Product': [
        'Apple_Juice', 'Banana_Smoothie', 'Orange_Jam', 'Grape_Jelly',
        'Kiwi_Parfait', 'Mango_Chutney', 'Pineapple_Sorbet',
        'Strawberry_Yogurt', 'Blueberry_Pie', 'Cherry_Salsa'
    ],

    'Category': [
        'Apple', 'Banana', 'Orange', 'Grape', 'Kiwi',
        'Mango', 'Pineapple', 'Strawberry', 'Blueberry', 'Cherry'
    ],

    'Sales': [1200, 1700, 2200, 1400, 2000, 1000, 1500, 1800, 1300, 1600],

    'Cost': [600, 850, 1100, 700, 1000, 500, 750, 900, 650, 800],

    'Profit': [600, 850, 1100, 700, 1000, 500, 750, 900, 650, 800]
}


# In[4]:


# Create a DataFrame
df = pd.DataFrame(data)
# Display the original dataset
print("Original Dataset:")
print(df)


# In[5]:


numeric_columns = ['Sales', 'Cost', 'Profit']
scaler_standardization = StandardScaler()
scaler_normalization = MinMaxScaler()


# In[9]:


# Standardization
df_scaled_standardized = pd.DataFrame(
    scaler_standardization.fit_transform(df[numeric_columns]),
    columns=numeric_columns
)

# Normalization
df_scaled_normalized = pd.DataFrame(
    scaler_normalization.fit_transform(df[numeric_columns]),
    columns=numeric_columns
)

# Combine the scaled numeric features with the categorical features
df_scaled = pd.concat([df_scaled_normalized, df.drop(numeric_columns, axis=1)], axis=1)

# Display the dataset after feature scaling
print("\nDataset after Feature Scaling:")
print(df_scaled)


# Step 2: Feature Dummification

# Identify categorical columns
categorical_columns = ['Product', 'Category']

# Create a column transformer for dummification
preprocessor = ColumnTransformer(
    transformers=[
        ('categorical', OneHotEncoder(), categorical_columns)
    ],
    remainder='passthrough'
)

# Apply the column transformer to the dataset
df_dummified = pd.DataFrame(preprocessor.fit_transform(df).toarray())

# Get column names after dummification
column_names = preprocessor.get_feature_names_out()

# Assign column names to the new dataframe
df_dummified.columns = column_names

# Display the dataset after feature dummification
print("\nDataset after Feature Dummification:")
print(df_dummified)


# In[ ]:




