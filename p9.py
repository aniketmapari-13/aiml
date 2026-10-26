import pandas as pd#kmean pr 9
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage
# 1. Load data
df = pd.read_csv("Mall_Customers.csv")
X = df[["Annual Income (k$)", "Spending Score (1-100)"]]
# 2. Scale data
X = StandardScaler().fit_transform(X)
# 3. Elbow graph
inertia = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)
    inertia.append(model.inertia_)
plt.plot(range(1, 11), inertia, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.show()
# 4. K-Means clustering
km = KMeans(n_clusters=5, random_state=42, n_init=10)
labels = km.fit_predict(X)
# 5. Cluster graph
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.title("K-Means Clustering")
plt.xlabel("Annual Income (scaled)")
plt.ylabel("Spending Score (scaled)")
plt.show()
# 6. Dendrogram
Z = linkage(X, method="ward")
plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.title("Hierarchical Clustering")
plt.show()
# 7. Hierarchical clustering
hc = AgglomerativeClustering(n_clusters=5)
df["Cluster"] = hc.fit_predict(X)
print(df.groupby("Cluster").size())
print("Silhouette Score:", silhouette_score(X, labels))
