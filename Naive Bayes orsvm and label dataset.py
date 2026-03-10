Practical 5
cmd   pip install nltk
Aim: Text Categorization
A. Implement a text classification algorithm (e.g., Naive Bayes or
Support Vector Machines).
B. Train the classifier on a labelled dataset and evaluate its
performance.
 
 

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
 
 
class NaiveBayes:
 
    def __init__(self):
        self.class_probabilities = None
        self.word_probabilities = None
 
    def fit(self, X, y):
        num_samples, num_features = X.shape
        self.classes = np.unique(y)
        num_classes = len(self.classes)
 
        self.class_probabilities = np.zeros(num_classes)
 
        for i, c in enumerate(self.classes):
            self.class_probabilities[i] = np.sum(y == c) / num_samples
 
        self.word_probabilities = np.zeros((num_classes, num_features))
 
        for i, c in enumerate(self.classes):
            X_c = X[y == c]
            total_word_counts = np.sum(X_c, axis=0)
            self.word_probabilities[i] = (total_word_counts + 1) / (
                np.sum(total_word_counts) + num_features
            )
 
    def predict(self, X):
        num_samples, _ = X.shape
        predictions = np.zeros(num_samples, dtype=int)
 
        for i in range(num_samples):
            probabilities = np.zeros(len(self.classes))
 
            for j, c in enumerate(self.classes):
                probabilities[j] = np.log(self.class_probabilities[j]) + np.sum(
                    np.log(self.word_probabilities[j]) * X[i]
                )
 
            predictions[i] = np.argmax(probabilities)
 
        return predictions
 
 
# Dataset
corpus = [
    "This movie is great and enjoyable.",
    "I really liked this film!",
    "The acting was terrible.",
    "Such a waste of time.",
    "Not worth watching."
]
 
labels = [1, 1, 0, 0, 0]
 
 
# Split data
X_train, X_test, y_train, y_test = train_test_split(
    corpus, labels, test_size=0.2, random_state=42
)
 
# Convert text to vectors
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)
 
# Train classifier
classifier = MultinomialNB()
classifier.fit(X_train_vectorized, y_train)
 
# Predictions
predictions = classifier.predict(X_test_vectorized)
 
# Display predictions
for test, prediction in zip(X_test, predictions):
    print("Test Data:", test)
    print("Predicted Label:", prediction)
    print()
 
# Accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
 

 

 

 

 

 

A. Question Answering System
 

# Corpus
corpus = [
    "India has the second-largest population in the world.",
    "It is surrounded by oceans from three sides which are Bay of Bengal in the east, the Arabian Sea in the west and Indian Ocean in the south.",
    "Tiger is the national animal of India.",
    "Peacock is the national bird of India.",
    "Mango is the national fruit of India."
]
 
# Question
question = "Which is the national bird of India?"
 
# Simple Question Answering
answer = ""
 
for sentence in corpus:
    if "national bird" in sentence.lower():
        answer = sentence
        break
 
print("Question:", question)
print("Answer:", answer)
 

 

B. Text Summarization System
 

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
 
# Download required datasets
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
 
text = """
Natural language processing (NLP) is a field of computer science, artificial intelligence,
and computational linguistics concerned with the interactions between computers and human
(natural) languages. As such, NLP is related to the area of human-computer interaction.
Many challenges in NLP involve natural language understanding, natural language generation,
and machine learning.
 
Text summarization is the process of distilling the most important information from a source
(text) to produce an abridged version for a particular user or task. Automatic text
summarization methods are greatly needed to address the ever-growing amount of text data
available online to both better help discover relevant information and to consume the vast
amount of text data available more efficiently.
"""
 
# Sentence tokenization
sentences = sent_tokenize(text)
 
# Word frequency calculation
stop_words = set(stopwords.words("english"))
word_freq = defaultdict(int)
 
for word in word_tokenize(text.lower()):
    if word.isalnum() and word not in stop_words:
        word_freq[word] += 1
 
# Sentence scoring
sentence_scores = defaultdict(int)
 
for sentence in sentences:
    for word in word_tokenize(sentence.lower()):
        if word in word_freq:
            sentence_scores[sentence] += word_freq[word]
 
# Select top 2 sentences
summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]
 
print("Summary:\n")
for s in summary:
    print(s)
 

 

 

 

A. Question Answering System
# Corpus
corpus = [
"India has the second-largest population in the world.",
"It is surrounded by oceans from three sides which are Bay of Bengal in the east, the Arabian Sea in the west and Indian oceans in the south.",
"Tiger is the national animal of India.",
"Peacock is the national bird of India.",
"Mango is the national fruit of India."
]
 
# Question
question = "Which is the national bird of India?"
 
# Simple QA system
for sentence in corpus:
    if "national bird" in sentence.lower():
        answer = sentence
        break
 
print("Question:", question)
print("Answer:", answer)
 

 

 

B. Text Summarization System
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
 
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
 
text = """
Natural language processing (NLP) is a field of computer science, artificial intelligence,
and computational linguistics concerned with the interactions between computers and human languages.
As such, NLP is related to the area of human-computer interaction.
 
Many challenges in NLP involve natural language understanding, natural language generation,
and machine learning.
 
Text summarization is the process of distilling the most important information from a source text
to produce an abridged version for a particular user or task.
 
Automatic text summarization methods are greatly needed to address the ever-growing amount of text
data available online and to consume large text efficiently.
"""
 
sentences = sent_tokenize(text)
 
stop_words = set(stopwords.words("english"))
word_freq = defaultdict(int)
 
for word in word_tokenize(text.lower()):
    if word.isalnum() and word not in stop_words:
        word_freq[word] += 1
 
sentence_scores = defaultdict(int)
 
for sentence in sentences:
    for word in word_tokenize(sentence.lower()):
        if word in word_freq:
            sentence_scores[sentence] += word_freq[word]
 
summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]
 
print("Summary:")
for s in summary:
    print(s)
