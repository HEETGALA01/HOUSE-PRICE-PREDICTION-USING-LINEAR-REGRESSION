# HOUSE-PRICE-PREDICTION-USING-LINEAR-REGRESSION

## 1. Introduction
House price prediction is a popular problem in real estate, finance, and data science. Predicting house prices helps buyers, sellers, and real estate agents make informed decisions. One of the simplest and most interpretable machine learning models used for this task is **Linear Regression**.

---

## 2. What Is Linear Regression?
Linear Regression is a supervised machine learning algorithm that establishes a relationship between a dependent variable (target) and one or more independent variables (features). It assumes that the relationship between the variables is **linear**.

### **Equation of Linear Regression:**  
\[
y = \beta_0 + \beta_1x_1 + \beta_2x_2 + ... + \beta_nx_n + \epsilon
\]

Where:
- \( y \): Predicted house price (target variable).
- \( x_1, x_2, ..., x_n \): Features (e.g., number of rooms, crime rate, etc.).
- \( \beta_0 \): Intercept.
- \( \beta_1, \beta_2, ..., \beta_n \): Coefficients (weights) of the features.
- \( \epsilon \): Error term.

---

## 3. Dataset for House Price Prediction
The commonly used **Boston Housing Dataset** contains features like:

- **`crim`**: Per capita crime rate by town.
- **`rm`**: Average number of rooms per dwelling.
- **`dis`**: Weighted distance to Boston employment centers.
- **`nox`**: Nitric oxides concentration (pollution level).
- **`ptratio`**: Pupil-teacher ratio by town (education quality).

The target variable is **`medv`**, which represents the **median house price in $1000s**.

---

## 4. Steps for House Price Prediction Using Linear Regression

### **Step 1: Data Preprocessing**
- Load the dataset using `pandas`.
- Handle any missing values.
- Scale the features to bring them to the same scale.

### **Step 2: Splitting the Data**
Split the data into a training set and testing set (e.g., 80% train, 20% test).

### **Step 3: Model Training**
Train a `LinearRegression` model from `sklearn`.

### **Step 4: Prediction**
Use the trained model to predict house prices on the test set and new samples.

### **Step 5: Evaluation**
Evaluate the model using:
- **Mean Squared Error (MSE)**: Measures the average squared error of the predictions.
- **R-squared (R²)**: Represents how well the model explains the variance in house prices.
