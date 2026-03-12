#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from scipy.stats import chi2_contingency

aptitude = [85,65,50,68,87,74,65,96,68,94,73,84,85,87,91]
jobprof = [70,90,80,89,88,86,78,67,86,90,92,94,99,93,87]

data = pd.DataFrame({
    'Aptitude': aptitude,
    'JobProficiency': jobprof
})

data['Aptitude_cat'] = pd.cut(data['Aptitude'], bins=3, labels=["Low","Medium","High"])
data['Job_cat'] = pd.cut(data['JobProficiency'], bins=3, labels=["Low","Medium","High"])

table = pd.crosstab(data['Aptitude_cat'], data['Job_cat'])

chi2, p, dof, expected = chi2_contingency(table)

print("Contingency Table:\n", table)
print("\nChi-square value:", chi2)
print("p-value:", p)
print("Degrees of freedom:", dof)


# In[ ]:




