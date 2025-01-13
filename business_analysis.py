# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Generate synthetic transaction data
np.random.seed(42)
num_records = 10000

# Dummy transaction data
data = {
    "TransactionID": range(1, num_records + 1),
    "MerchantID": np.random.randint(1000, 1050, size=num_records),
    "TransactionAmount": np.random.uniform(50, 1000, size=num_records),
    "TransactionType": np.random.choice(["Online", "POS"], size=num_records),
    "FraudDetected": np.random.choice([0, 1], size=num_records, p=[0.98, 0.02]),
    "State": np.random.choice(["Maharashtra", "Delhi", "Karnataka", "Tamil Nadu", "Gujarat"], size=num_records),
    "UserAge": np.random.randint(18, 65, size=num_records),
    "UserIncome": np.random.uniform(20000, 150000, size=num_records),
    "Churn": np.random.choice([0, 1], size=num_records, p=[0.85, 0.15])
}

df = pd.DataFrame(data)

# Display the first few rows of the dataset
print(df.head())

# Save data for visualization/analysis
df.to_csv("synthetic_business_data.csv", index=False)


# Features and target for risk detection
features = ["TransactionAmount", "UserAge", "UserIncome"]
target = "FraudDetected"

X = df[features]
y = df[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Random Forest Classifier
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Predictions and evaluation
y_pred = rf_model.predict(X_test)
print("Risk Detection Model Evaluation:\n", classification_report(y_test, y_pred))

# State-wise transaction analysis
state_sales = df.groupby("State")["TransactionAmount"].sum().reset_index()
state_sales = state_sales.sort_values(by="TransactionAmount", ascending=False)

# Visualize sales
plt.figure(figsize=(10, 6))
sns.barplot(x="TransactionAmount", y="State", data=state_sales, palette="viridis")
plt.title("State-wise Transaction Volumes")
plt.xlabel("Total Transaction Volume")
plt.ylabel("State")
plt.show()

# Features and target for churn analysis
features = ["UserAge", "UserIncome", "TransactionAmount"]
target = "Churn"

X = df[features]
y = df[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Logistic Regression for churn prediction
log_model = LogisticRegression(random_state=42, max_iter=200)
log_model.fit(X_train, y_train)

# Predictions and evaluation
y_pred = log_model.predict(X_test)
print("Churn Prediction Model Evaluation:\n", classification_report(y_test, y_pred))


# Summary report visualization
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x="TransactionType", y="TransactionAmount", hue="FraudDetected")
plt.title("Transaction Amount by Type and Fraud Detection")
plt.xlabel("Transaction Type")
plt.ylabel("Transaction Amount")
plt.legend(title="Fraud Detected", loc="upper right")
plt.show()

# Analyze demographics for untapped opportunities
age_income_analysis = df.groupby("UserAge")["UserIncome"].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=age_income_analysis, x="UserAge", y="UserIncome", marker="o", color="blue")
plt.title("Average Income by User Age")
plt.xlabel("Age")
plt.ylabel("Average Income")
plt.grid(True)
plt.show()
















