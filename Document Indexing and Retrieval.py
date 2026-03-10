p1=Document Indexing and Retrieval 
 Implement an inverted index construction algorithm. 
 Build a simple document retrieval system using the constructed index.

CMD:  pip install nltk       python -m pip install nltk

code

import nltk
from nltk.corpus import stopwords
 
 
nltk.download('stopwords')
nltk.download('punkt')
 
class InvertedIndex:
    def __init__(self):
        self.index = {}
 
    def add_document(self, doc_id, content):
        words = content.split()
        stop_words = set(stopwords.words('english'))
 
        
        filtered_words = [word for word in words if word.lower() not in stop_words]
 
        
        for word in set(filtered_words):
            if word not in self.index:
                self.index[word] = []
            self.index[word].append(doc_id)
 
    def search(self, query):
        return self.index.get(query, [])
 
 
if __name__ == "__main__":
 
    inverted_index = InvertedIndex()
 
 
    documents = {
        1: "Inverted index is a data structure",
        2: "This is an example of inverted index construction",
        3: "The algorithm constructs an inverted index from documents"
    }
 
    print("Documents:", documents)
 
    for doc_id, content in documents.items():
        inverted_index.add_document(doc_id, content)
 
    search_query = input("Please enter the word you want to search: ")
 
    result = inverted_index.search(search_query)
 
    if result:
        print(f"Documents containing '{search_query}': {result}")
    else:
        print(f"No documents found containing '{search_query}'")



        
