# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qIHlnLTEO71sK2qxSwqkbJUaqGvQlPGy
"""

#house price prediction using linear regression algorithm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("/content/BostonHousing.csv")
df.describe()

#checking for missing value
missing_value = df.isnull().sum()
print(missing_value)

#checking for dublicate value
dublicate_value = df.duplicated().sum()
print(dublicate_value)

#treating with missing values
df['rm'].fillna(df['rm'].mean(), inplace=True)

#standardization makes all features equal and important
# and faster for the algorithm to learn
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

#EDA
#Visualize correlation between features:

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

#Plot price distribution:
plt.figure(figsize=(9,3))
sns.histplot(df['medv'], kde=True)
plt.show()

#Splitting Data into Train and Test Sets

from sklearn.model_selection import train_test_split

# Define independent (X) and dependent (y) variables
X = df.drop(columns=['medv'])  # Features
y = df['medv']  # Target variable

# Split data into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train a Linear Regression Model

from sklearn.linear_model import LinearRegression

# Create a model and train it
model = LinearRegression()
model.fit(X_train, y_train)

#Evaluate model performance

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Make predictions
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae}, MSE: {mse}, R2 Score: {r2}")

# Testing the Model with New Data
# price predicting for new house

sample_house = [[0.1, 20, 5.0, 6.0, 30.0, 300, 18.0, 4.0, 1.0, 250.0, 12.0, 400.0, 5.0]]  # Example feature values
predicted_medv = model.predict(sample_house)
print(f"Predicted House Price: ${predicted_medv[0] * 1000:.2f}")  # Converting from $1000s to actual price

