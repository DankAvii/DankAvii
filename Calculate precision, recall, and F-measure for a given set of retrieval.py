Practical 4 CMD -     pip install scikit-learn
Aim: Evaluation Metrics for IR Systems
 Calculate precision, recall, and F-measure for a given set of retrieval
results.
 Use an evaluation toolkit to measure average precision and other
evaluation metrics.

 

A]

def calculate_metrics(retrieved_set, relevant_set):
 
    true_positive = len(retrieved_set.intersection(relevant_set))
    false_positive = len(retrieved_set.difference(relevant_set))
    false_negative = len(relevant_set.difference(retrieved_set))
 
    print("True Positive:", true_positive)
    print("False Positive:", false_positive)
    print("False Negative:", false_negative)
    print()
 
    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)
 
    f_measure = 2 * precision * recall / (precision + recall)
 
    return precision, recall, f_measure
 
 
# Predicted / Retrieved documents
retrieved_set = set(["doc1", "doc2", "doc3"])
 
# Actually relevant documents
relevant_set = set(["doc1", "doc4"])
 
 
precision, recall, f_measure = calculate_metrics(retrieved_set, relevant_set)
 
print("Precision:", precision)
print("Recall:", recall)
print("F-measure:", f_measure)
 

 

 

==>

# Given values
TP = 20
FP = 10
FN = 30
 
# Calculate Precision
precision = TP / (TP + FP)
 
# Calculate Recall
recall = TP / (TP + FN)
 
# Calculate F-Measure
f_score = 2 * (precision * recall) / (precision + recall)
 
# Display results
print("True Positive:", TP)
print("False Positive:", FP)
print("False Negative:", FN)
 
print("\nPrecision =", precision)
print("Recall =", recall)
print("F-Measure =", f_score)
 

 

 

B]
from sklearn.metrics import average_precision_score
 
# Actual labels (0 = not relevant, 1 = relevant)
y_true = [0, 1, 1, 0, 1, 1]
 
# Model predicted scores
y_scores = [0.1, 0.4, 0.35, 0.8, 0.65, 0.9]
 
# Calculate Average Precision
average_precision = average_precision_score(y_true, y_scores)
 
# Display result
print("Average precision-recall score:", average_precision)
