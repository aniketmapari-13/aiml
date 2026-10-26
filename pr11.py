import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
# 1. Load dataset
data = load_breast_cancer()
X, y = data.data, data.target
print("Dataset shape:", X.shape)
# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
# 3. Create models
models = {
    "SVM": make_pipeline(StandardScaler(), SVC()),
    "Random Forest": RandomForestClassifier(random_state=42),
    "AdaBoost": AdaBoostClassifier(random_state=42)
}
# 4. Train and evaluate models
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("\n", name)
    print("Accuracy:", accuracy_score(y_test, pred))
    print("Precision:", precision_score(y_test, pred))
    print("Recall:", recall_score(y_test, pred))
    print("F1 Score:", f1_score(y_test, pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
# 5. Cross-validation on SVM
svm = models["SVM"]
scores = cross_val_score(svm, X_train, y_train, cv=5)
print("\nCV Scores:", scores)
print("Mean CV Score:", scores.mean())
# 6. Find best SVM parameters
grid = GridSearchCV(svm, {
    "svc__C": [1, 10],
    "svc__kernel": ["linear", "rbf"]
}, cv=5)
grid.fit(X_train, y_train)
print("\nBest Parameters:", grid.best_params_)
# 7. Test optimized model
pred = grid.predict(X_test)
print("Best Accuracy:", accuracy_score(y_test, pred))
