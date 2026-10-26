import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# Load dataset
data = load_digits()
X, y = data.data, data.target
print("Original shape:", X.shape)
# Split and scale data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
# Apply PCA
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)
print("Reduced shape:", X_train_pca.shape)
# Train models before and after PCA
m1 = LogisticRegression(max_iter=2000)
m1.fit(X_train, y_train)
p1 = m1.predict(X_test)
m2 = LogisticRegression(max_iter=2000)
m2.fit(X_train_pca, y_train)
p2 = m2.predict(X_test_pca)
# Compare accuracy
print("Before PCA:", accuracy_score(y_test, p1))
print("After PCA:", accuracy_score(y_test, p2))
# Show graph
plt.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test)
plt.show()
#pCA