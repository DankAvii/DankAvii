#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


# In[2]:


iris = load_iris()

X = iris.data
y = iris.target


# In[3]:


model = DecisionTreeClassifier()
model.fit(X, y)


# In[4]:


plt.figure(figsize=(10,6))
plot_tree(model,
          feature_names=iris.feature_names,
          class_names=iris.target_names,
          filled=True)
plt.show()


# In[5]:


from sklearn.tree import export_text

rules = export_text(model, feature_names=iris.feature_names)
print(rules)


# In[ ]:




