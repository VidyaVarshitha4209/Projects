##Student Performance Prediction using Machine Learning

## Project Overview

This project predicts a student's final exam marks based on various academic and personal factors using Machine Learning Regression algorithms.

The objective of this project is to understand the complete Machine Learning workflow, including data preprocessing, model training, evaluation, and prediction.

---

## Problem Statement

Predict a student's final marks using the following features:

- Study Hours
- Attendance
- Previous Marks
- Assignments Completed
- Sleep Hours

Target Variable:

- Final Marks

---

## Machine Learning Type

This is a **Supervised Learning** problem because the dataset contains both:

- Input Features (X)
- Target Variable (Y)

The model learns the relationship between the inputs and outputs and predicts marks for new students.

---

## Regression

Since the output is a **continuous numerical value (Final Marks)**, this project uses **Regression** algorithms.

---

## Dataset Features

| Feature | Description |
|----------|-------------|
| StudyHours | Number of study hours |
| Attendance | Attendance percentage |
| PreviousMarks | Previous examination marks |
| AssignmentsCompleted | Number of assignments completed |
| SleepHours | Average sleep hours |
| FinalMarks | Target variable |

---

## Data Preprocessing

The following preprocessing steps were performed:

- Loaded the dataset using Pandas
- Checked for missing values
- Removed duplicate records
- Selected input and output features

---

## Train-Test Split

The dataset was divided into:

- Training Data – 80%
- Testing Data – 20%

The training data was used to train the model, while the testing data was used to evaluate its performance.

---

## Algorithms Used

### 1. Linear Regression

Linear Regression models the relationship between the input features and the target variable using a linear equation.

It works well when the relationship between the variables is approximately linear.

---

### 2. Random Forest Regression

Random Forest is an ensemble learning algorithm that combines multiple Decision Trees.

Each Decision Tree predicts the output independently, and the final prediction is obtained by averaging the predictions of all trees.

Random Forest performs well because it can learn complex patterns from the data.

---

## Feature Importance

Random Forest calculates Feature Importance to determine which input features contribute the most to prediction.

In this project, **Previous Marks** had the highest importance, indicating that it contributed the most towards predicting the final marks.

---

## Evaluation Metrics

The models were evaluated using:

### Mean Absolute Error (MAE)

Measures the average prediction error.

### Mean Squared Error (MSE)

Measures the average squared prediction error.

### R² Score

Measures how well the model explains the variance in the target variable.

---

## Prediction

The trained model predicts the final marks of a new student based on:

- Study Hours
- Attendance
- Previous Marks
- Assignments Completed
- Sleep Hours

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn

---

## Project Workflow

1. Load Dataset
2. Data Preprocessing
3. Feature Selection
4. Train-Test Split
5. Train Linear Regression Model
6. Train Random Forest Regression Model
7. Evaluate Models
8. Analyze Feature Importance
9. Predict Final Marks

---

## Results

- Successfully trained both Linear Regression and Random Forest Regression models.
- Random Forest achieved better prediction performance.
- The model successfully predicted the final marks for new student data.

---

## Future Improvements

- Use a larger real-world dataset.
- Perform feature engineering.
- Apply hyperparameter tuning.
- Build a web application using Flask or Streamlit.
