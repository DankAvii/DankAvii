Practical 10   pip install nltk
Aim: Advanced Topics in Information Retrieval
 Implement a text summarization algorithm (e.g., extractive or
abstractive).
 Build a question-answering system using techniques such as
information extraction

A]

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
 
# Download resources
nltk.download('punkt')
nltk.download('stopwords')
 
 
def sentence_similarity(sent1, sent2):
 
    stop_words = stopwords.words('english')
 
    sent1 = [w.lower() for w in sent1 if w.lower() not in stop_words]
    sent2 = [w.lower() for w in sent2 if w.lower() not in stop_words]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    for w in sent1:
        vector1[all_words.index(w)] += 1
 
    for w in sent2:
        vector2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(vector1, vector2)
 
 
def build_similarity_matrix(sentences):
 
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j])
 
    return similarity_matrix
 
 
def generate_summary(text, top_n=3):
 
    sentences = sent_tokenize(text)
    sentence_words = [word_tokenize(sentence) for sentence in sentences]
 
    similarity_matrix = build_similarity_matrix(sentence_words)
 
    scores = np.array([np.sum(similarity_matrix[i]) for i in range(len(sentences))])
    scores /= scores.sum()
 
    ranked_sentences = [
        sentence for _, sentence in sorted(zip(scores, sentences), reverse=True)
    ]
 
    summary = " ".join(ranked_sentences[:top_n])
    return summary
 
 
text = """
Natural language processing (NLP) is a subfield of computer science and artificial intelligence.
It focuses on interaction between computers and human language.
Text summarization extracts important information from text.
TextRank is a popular algorithm used for extractive summarization.
"""
 
summary = generate_summary(text, 2)
 
print("Summary:")
print(summary)
 

 

B]
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
 
nltk.download('punkt')
nltk.download('stopwords')
 
documents = [
"The cat is on the mat.",
"The dog is in the yard.",
"A bird is flying in the sky.",
"The sun is shining brightly."
]
 
stop_words = nltk.corpus.stopwords.words('english')
 
 
def tokenize(text):
 
    tokens = nltk.word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalnum()]
    return tokens
 
 
vectorizer = TfidfVectorizer(tokenizer=tokenize, stop_words=stop_words)
 
tfidf_matrix = vectorizer.fit_transform(documents)
 
 
def answer_question(query):
 
    query_vector = vectorizer.transform([query])
    similarity = cosine_similarity(query_vector, tfidf_matrix)
 
    index = similarity.argmax()
 
    return documents[index]
 
 
query = "Where is the cat?"
 
answer = answer_question(query)
 
print("Question:", query)
print("Answer:", answer)
 

 

26bc008a4f66fcbed8a85ff9fdebe0b0.png
 

A}}
# Corpus
documents = [
"India has the second-largest population in the world.",
"It is surrounded by oceans from three sides which are Bay of Bengal in the east, the Arabian Sea in the west and Indian oceans in the south.",
"Tiger is the national animal of India.",
"Peacock is the national bird of India.",
"Mango is the national fruit of India."
]
 
# Query
query = "Which is the national bird of India?"
 
# Simple Question Answering
answer = ""
 
for sentence in documents:
    if "national bird" in sentence.lower():
        answer = sentence
        break
 
print("Question:", query)
print("Answer:", answer)
 

 

B}}
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
 
nltk.download('punkt')
nltk.download('stopwords')
 
text = """
Natural language processing (NLP) is a field of computer science, artificial intelligence,
and computational linguistics concerned with the interactions between computers and human languages.
As such, NLP is related to the area of human-computer interaction.
Many challenges in NLP involve natural language understanding, natural language generation, and machine learning.
 
Text summarization is the process of distilling the most important information from a source text
to produce an abridged version for a particular user or task.
Automatic text summarization methods are greatly needed to address the ever-growing amount of text
data available online.
"""
 
# Sentence tokenization
sentences = sent_tokenize(text)
 
# Remove stopwords and calculate frequency
stop_words = set(stopwords.words("english"))
word_freq = defaultdict(int)
 
for word in word_tokenize(text.lower()):
    if word.isalnum() and word not in stop_words:
        word_freq[word] += 1
 
# Score sentences
sentence_scores = defaultdict(int)
 
for sentence in sentences:
    for word in word_tokenize(sentence.lower()):
        if word in word_freq:
            sentence_scores[sentence] += word_freq[word]
 
# Select top sentences
summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]
 
print("Summary:")
for s in summary_sentences:
    print(s)
 

2b700526dc511771d2eeeb5411405b1e.png
A}}
# Corpus
documents = [
"India has the second-largest population in the world.",
"It is surrounded by oceans from three sides which are Bay of Bengal in the east, the Arabian Sea in the west and Indian oceans in the south.",
"Tiger is the national animal of India.",
"Peacock is the national bird of India.",
"Mango is the national fruit of India."
]
 
# Query
query = "Which is the national bird of India?"
 
# Search for answer
for sentence in documents:
    if "national bird" in sentence.lower():
        answer = sentence
        break
 
print("Question:", query)
print("Answer:", answer)
 

B}}
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
 
nltk.download('punkt')
nltk.download('stopwords')
 
text = """
Natural language processing (NLP) is a field of computer science, artificial intelligence and computational linguistics concerned with the interactions between computers and human languages.
As such, NLP is related to the area of human-computer interaction.
Many challenges in NLP involve natural language understanding, natural language generation and machine learning.
 
Text summarization is the process of distilling the most important information from a source text to produce an abridged version.
Automatic text summarization methods are needed to handle large amounts of online text data.
"""
 
# Tokenize sentences
sentences = sent_tokenize(text)
 
# Remove stopwords
stop_words = set(stopwords.words("english"))
 
word_freq = defaultdict(int)
 
for word in word_tokenize(text.lower()):
    if word not in stop_words and word.isalnum():
        word_freq[word] += 1
 
# Score sentences
sentence_scores = defaultdict(int)
 
for sentence in sentences:
    for word in word_tokenize(sentence.lower()):
        if word in word_freq:
            sentence_scores[sentence] += word_freq[word]
 
# Get top 2 sentences
summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]
 
print("Summary:")
for s in summary:
    print(s)
 

163bd9026a8724a98f6adb1c0d552bb0.png
A}]]
# Documents
documents = {
1: "this is the first document",
2: "this document is the second document",
3: "and this is the third one",
4: "is this the first document"
}
 
# Build inverted index
def build_index(docs):
    index = {}
 
    for doc_id, text in docs.items():
        words = text.lower().split()
 
        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(doc_id)
 
    return index
 
 
index = build_index(documents)
 
# Boolean AND query
query = ["first", "third"]
 
result = index.get(query[0], set())
 
for term in query[1:]:
    result = result.intersection(index.get(term, set()))
 
print("Documents matching query:", result)
 

 

b]]
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
 
nltk.download('punkt')
nltk.download('stopwords')
 
text = """
Text summarization is the process of reducing a text document.
It helps in extracting important information.
Automatic summarization is useful for large datasets.
"""
 
sentences = sent_tokenize(text)
 
stop_words = set(stopwords.words("english"))
 
word_freq = defaultdict(int)
 
for word in word_tokenize(text.lower()):
    if word not in stop_words and word.isalnum():
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
