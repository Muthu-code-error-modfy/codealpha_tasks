# -*- coding: utf-8 -*-
"""disease prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1P9KLMPjJw7dv8iyHW7RyeDnU_VAnBgPh
"""

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report  # ✅ Import accuracy_score

# ✅ Load dataset
data = load_breast_cancer()
X, y = data.data, data.target

# ✅ Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train model
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# ✅ Make predictions
y_pred = model.predict(X_test)

# ✅ Evaluate model
print("Disease Prediction Model Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

