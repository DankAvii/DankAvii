#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import warnings
warnings.filterwarnings("ignore")

import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Load dataset
boston = fetch_openml(name="boston", version=1, as_frame=True)
data = boston.data

print(data.head())

# Standardization
scaler = StandardScaler()
standardized_data = scaler.fit_transform(data)

print("Standardized Data:")
print(standardized_data[:5])

# Normalization
normalizer = MinMaxScaler()
normalized_data = normalizer.fit_transform(data)

print("Normalized Data:")
print(normalized_data[:5])

