import pandas as pd# pr 5 data preprocessing and analysis
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
# 1. Load dataset
df = pd.read_csv("titanic.csv")
print(df.head())
# 2. Remove duplicates
df = df.drop_duplicates()
print("Shape:", df.shape)
# 3. Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
print(df.isnull().sum())
# 4. Encode text values
le = LabelEncoder()
df["Sex"] = le.fit_transform(df["Sex"])
df["Embarked"] = le.fit_transform(df["Embarked"])
# 5. Statistical analysis
print(df.describe())
# 6. Select features and target
X = df[["Pclass", "Sex", "Age", "SibSp",
        "Parch", "Fare", "Embarked"]]
y = df["Survived"]
# 7. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)
# 8. Scale features
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print("Scaling completed")
# 9. Histogram of Age
plt.hist(df["Age"], bins=20)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Histogram of Age")
plt.show()
# 10. Boxplot of Fare
sns.boxplot(x=df["Fare"])
plt.title("Boxplot of Fare")
plt.show()
print("Practical 5 Completed Successfully!")
