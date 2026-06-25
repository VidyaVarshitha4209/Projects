
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Load Dataset
df = pd.read_csv("student_data.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Remove Duplicates
df = df.drop_duplicates()

# Features and Target
X = df[
    [
        "StudyHours",
        "Attendance",
        "PreviousMarks",
        "AssignmentsCompleted",
        "SleepHours"
    ]
]

y = df["FinalMarks"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Linear Regression
lr = LinearRegression()

lr.fit(X_train, y_train)

lr_predictions = lr.predict(X_test)

print("\nLINEAR REGRESSION RESULTS")

print("MAE:",
      mean_absolute_error(y_test, lr_predictions))

print("MSE:",
      mean_squared_error(y_test, lr_predictions))

print("R2 Score:",
      r2_score(y_test, lr_predictions))

# Random Forest
rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_predictions = rf.predict(X_test)

print("\nRANDOM FOREST RESULTS")

print("MAE:",
      mean_absolute_error(y_test, rf_predictions))

print("MSE:",
      mean_squared_error(y_test, rf_predictions))

print("R2 Score:",
      r2_score(y_test, rf_predictions))

# Feature Importance
importance = pd.DataFrame(
    {
        "Feature": X.columns,
        "Importance": rf.feature_importances_
    }
)

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance")
print(importance)

# Sample Prediction
new_student = [[
    5,
    85,
    70,
    7,
    7
]]

predicted_marks = rf.predict(new_student)

print(
    "\nPredicted Marks for New Student:",
    predicted_marks[0]
)

# Graph
plt.scatter(
    df["StudyHours"],
    df["FinalMarks"]
)

plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")

plt.show()