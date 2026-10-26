import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Load dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

print("First five rows:")
print(df.head())

print("\nDataset shape:", df.shape)

# 2. Define features and target
X = df.drop(columns=["MedHouseVal"])
y = df["MedHouseVal"]

print("\nNumber of features:", X.shape[1])

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples :", len(X_test))

# 4. Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_pred_linear = linear_model.predict(X_test)

# 5. Polynomial Regression (Degree 2)
poly_model = Pipeline([
    ("poly", PolynomialFeatures(degree=2, include_bias=False)),
    ("linear", LinearRegression())
])

poly_model.fit(X_train, y_train)
y_pred_poly = poly_model.predict(X_test)

# 6. Evaluation function
def calculate_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return mse, mae, r2

mse_linear, mae_linear, r2_linear = calculate_metrics(
    y_test, y_pred_linear
)

mse_poly, mae_poly, r2_poly = calculate_metrics(
    y_test, y_pred_poly
)

# 7. Comparison table
results = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Polynomial Regression (Degree 2)"
    ],
    "MSE": [mse_linear, mse_poly],
    "MAE": [mae_linear, mae_poly],
    "R2 Score": [r2_linear, r2_poly]
})

print("\nModel Performance Comparison")
print(results.round(4).to_string(index=False))

# 8. Simple R2-based indication
if r2_poly > r2_linear:
    print("\nHigher R2 on test data: Polynomial Regression")
else:
    print("\nHigher R2 on test data: Linear Regression")

# 9. Select sample points for visualization
n_points = 50

if len(y_test) > n_points:
    indices = np.random.choice(len(y_test), n_points, replace=False)
else:
    indices = np.arange(len(y_test))

y_test_sample = y_test.iloc[indices]
y_pred_sample = y_pred_linear[indices]

# 10. Plot Actual vs Predicted Values
plt.figure(figsize=(7, 7))

plt.scatter(
    y_test_sample,
    y_pred_sample,
    alpha=0.6
)

# Ideal prediction line
min_value = min(y_test_sample.min(), y_pred_sample.min())
max_value = max(y_test_sample.max(), y_pred_sample.max())

plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    "r--",
    label="Ideal Prediction"
)

plt.xlabel("Actual Median House Value")
plt.ylabel("Predicted Median House Value")
plt.title("Linear Regression: Actual vs Predicted")
plt.legend()
plt.show()