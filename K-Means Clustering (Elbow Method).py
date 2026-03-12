#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans


# In[2]:


iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)

print(data.head())


# In[3]:


wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)


# In[4]:


wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)


# In[5]:


plt.plot(range(1,11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()


# In[6]:


kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(data)

data['Cluster'] = clusters


# In[7]:


kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(data)

data['Cluster'] = clusters


# In[ ]:




