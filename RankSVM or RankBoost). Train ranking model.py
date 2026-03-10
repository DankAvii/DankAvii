Practical 9
pip install scikit-learn
pip install numpy
Aim: Learning to Rank
∙ Implement a learning to rank algorithm (e.g., RankSVM or
RankBoost).
∙ Train the ranking model using labelled data and evaluate its
effectiveness
 

a]
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
 
def train_ranksvm(X_train, y_train):
    svm = SVC(kernel='linear')
    svm.fit(X_train, y_train)
    return svm
 
def predict_ranksvm(model, X_test):
    rankings = model.decision_function(X_test)
    return rankings
 
 
if __name__ == "__main__":
 
    X, y = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=42)
 
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
 
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
 
    ranksvm_model = train_ranksvm(X_train_scaled, y_train)
 
    rankings = predict_ranksvm(ranksvm_model, X_test_scaled)
 
    y_pred = (rankings > 0).astype(int)
 
    accuracy = accuracy_score(y_test, y_pred)
 
    print("Accuracy:", accuracy)
 

 

b]
import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score
 
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)
 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
 
model = SVC(kernel='linear')
 
model.fit(X_train, y_train)
 
y_pred = model.predict(X_test)
 
map_score = average_precision_score(y_test, y_pred)
 
print("Mean Average Precision (MAP):", map_score)
