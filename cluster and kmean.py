Practical 6
pip install scikit-learn
pip install numpy
 
Aim : Clustering for Information Retrieval
∙ Implement a clustering algorithm (e.g., K-means or hierarchical
clustering).
∙ Apply the clustering algorithm to a set of documents and evaluate the
clustering results.
 

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
 
# Sample documents
documents = [
"Machine learning is the study of computer algorithms that improve automatically through experience.",
"Deep learning is a subset of machine learning.",
"Natural language processing is a field of artificial intelligence.",
"Computer vision is a field of study that enables computers to interpret and understand the visual world.",
"Reinforcement learning is a type of machine learning algorithm that teaches an agent how to make decisions in an environment by rewarding desired behaviors.",
"Information retrieval is the process of obtaining information from a collection of documents.",
"Text mining is the process of deriving high-quality information from text.",
"Data clustering is the task of dividing a set of objects into groups.",
"Hierarchical clustering builds a tree of clusters.",
"K-means clustering is a method of vector quantization."
]
 
# Convert documents into TF-IDF vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
 
# Perform K-means clustering
k = 3  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)
 
# Evaluate clustering results
silhouette_avg = silhouette_score(X, kmeans.labels_)
print("Silhouette Score:", silhouette_avg)
 
# Print clusters
for i in range(k):
    cluster_docs_indices = np.where(kmeans.labels_ == i)[0]
    cluster_docs = [documents[idx] for idx in cluster_docs_indices]
 
    print("\nCluster", i+1)
    for doc in cluster_docs:
        print("-", doc)
 

 

A]
from sklearn.feature_extraction.text import TfidfVectorizer
 
# Documents
documents = [
"The sun is the star at the center of the solar system.",
"She wore a beautiful dress to the party last night.",
"The book on the table caught my attention immediately."
]
 
# Query
query = "solar system"
 
# Combine documents and query
all_text = documents + [query]
 
# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_text)
 
# Print TF-IDF matrix
print("TF-IDF Matrix:\n")
print(tfidf_matrix.toarray())
 
# Print feature names (terms)
print("\nTerms:")
print(vectorizer.get_feature_names_out())
 

B]
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
 
# Documents
documents = [
"The sun is the star at the center of the solar system.",
"She wore a beautiful dress to the party last night.",
"The book on the table caught my attention immediately."
]
 
# Query
query = "solar system"
 
# Combine documents and query
all_text = documents + [query]
 
# Convert to TF-IDF vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_text)
 
# Separate document vectors and query vector
doc_vectors = tfidf_matrix[:-1]
query_vector = tfidf_matrix[-1]
 
# Calculate cosine similarity
similarity = cosine_similarity(query_vector, doc_vectors)
 
# Display similarity scores
for i, score in enumerate(similarity[0]):
    print(f"Cosine Similarity between Query and Document {i+1}: {score}")
 

 

A} SPELLONG CORRECTION 
 

def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
 
    # Create matrix
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
 
    # Initialize matrix
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
 
    # Compute edit distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
 
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 1
 
            dp[i][j] = min(
                dp[i-1][j] + 1,      # Deletion
                dp[i][j-1] + 1,      # Insertion
                dp[i-1][j-1] + cost  # Substitution
            )
 
    return dp[m][n]
 
 
word1 = "write"
word2 = "right"
 
distance = edit_distance(word1, word2)
 
print("Word 1:", word1)
print("Word 2:", word2)
print("Edit Distance:", distance)
 

 

B}

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
 
# Sample documents
documents = [
"Machine learning improves computer algorithms.",
"Deep learning is a subset of machine learning.",
"Natural language processing works with text data.",
"Information retrieval finds relevant documents.",
"Text mining extracts useful information from text."
]
 
# Convert documents into TF-IDF vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
 
# Apply K-means clustering
k = 2
kmeans = KMeans(n_clusters=k, random_state=0)
kmeans.fit(X)
 
# Get cluster labels
labels = kmeans.labels_
 
# Evaluate clustering using Silhouette Score
score = silhouette_score(X, labels)
print("Silhouette Score:", score)
 
# Print clustered documents
for i in range(k):
    print("\nCluster", i+1)
    for j in range(len(documents)):
        if labels[j] == i:
            print("-", documents[j])
 
