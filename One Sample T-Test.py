#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats

scores = np.array([72,88,64,74,67,79,85,75,89,77])

t_stat, p_value = stats.ttest_1samp(scores, 70)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")


# In[ ]:




