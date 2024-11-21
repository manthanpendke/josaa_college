# -*- coding: utf-8 -*-
"""finalproject.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iAYR9MywvaefU94kRtqfMyJq_bJvMHr6
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, mean_absolute_error
from sklearn.metrics import accuracy_score, classification_report

# Load the data
data = pd.read_csv('2022.csv')  # Adjust to your file path

# Select relevant columns
data = data[["Institute", "Academic Program Name", "Seat Type", "Opening Rank", "Closing Rank", "Round"]]

# Drop rows with missing values
data = data.dropna()

# Encode categorical features
label_encoders = {}
for col in ["Institute", "Academic Program Name", "Seat Type"]:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Convert "Opening Rank" and "Closing Rank" to numeric types
data["Opening Rank"] = pd.to_numeric(data["Opening Rank"], errors="coerce")
data["Closing Rank"] = pd.to_numeric(data["Closing Rank"], errors="coerce")

# Drop rows where ranks couldn't be converted
data = data.dropna(subset=["Opening Rank", "Closing Rank"])

# Features and targets
X = data[["Seat Type", "Opening Rank", "Closing Rank"]]
y_institute = data["Institute"]
y_program = data["Academic Program Name"]
y_round = data["Round"]

# Split into training and testing sets
X_train, X_test, y_train_institute, y_test_institute = train_test_split(X, y_institute, test_size=0.2, random_state=42)
_, _, y_train_program, y_test_program = train_test_split(X, y_program, test_size=0.2, random_state=42)
_, _, y_train_round, y_test_round = train_test_split(X, y_round, test_size=0.2, random_state=42)

# Standardize numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize models
logistic_model = LogisticRegression(max_iter=1000, multi_class='multinomial', solver='lbfgs')
knn_model = KNeighborsClassifier(n_neighbors=5)
svm_model = SVC(kernel='linear')
nb_model = GaussianNB()
linear_model = LinearRegression()


# Logistic Regression
logistic_model.fit(X_train, y_train_institute)
institute_predictions_log = logistic_model.predict(X_test)

logistic_model.fit(X_train, y_train_program)
program_predictions_log = logistic_model.predict(X_test)

logistic_model.fit(X_train, y_train_round)
round_predictions_log = logistic_model.predict(X_test)

# K-Nearest Neighbors
knn_model.fit(X_train, y_train_institute)
institute_predictions_knn = knn_model.predict(X_test)

knn_model.fit(X_train, y_train_program)
program_predictions_knn = knn_model.predict(X_test)

knn_model.fit(X_train, y_train_round)
round_predictions_knn = knn_model.predict(X_test)

# Support Vector Machine
svm_model.fit(X_train, y_train_institute)
institute_predictions_svm = svm_model.predict(X_test)

svm_model.fit(X_train, y_train_program)
program_predictions_svm = svm_model.predict(X_test)

svm_model.fit(X_train, y_train_round)
round_predictions_svm = svm_model.predict(X_test)

# Naive Bayes
nb_model.fit(X_train, y_train_institute)
institute_predictions_nb = nb_model.predict(X_test)

nb_model.fit(X_train, y_train_program)
program_predictions_nb = nb_model.predict(X_test)

nb_model.fit(X_train, y_train_round)
round_predictions_nb = nb_model.predict(X_test)

# Linear Regression
linear_model.fit(X_train, y_train_institute)
institute_predictions_linear = linear_model.predict(X_test).round().astype(int)

linear_model.fit(X_train, y_train_program)
program_predictions_linear = linear_model.predict(X_test).round().astype(int)

linear_model.fit(X_train, y_train_round)
round_predictions_linear = linear_model.predict(X_test).round().astype(int)


# Linear Regression Evaluation
print("\nLinear Regression (Institute Prediction):")
print("Accuracy: {:.2f}%".format(accuracy_score(y_test_institute, institute_predictions_linear) * 100))

print("\nLinear Regression (Program Prediction):")
print("Accuracy: {:.2f}%".format(accuracy_score(y_test_program, program_predictions_linear) * 100))

print("\nLinear Regression (Round Prediction):")
print("MAE (Round): {:.2f}".format(mean_absolute_error(y_test_round, round_predictions_linear)))

# Logistic Regression Evaluation
print("\nLogistic Regression (Institute Prediction):")
print("Accuracy: {:.2f}%".format(accuracy_score(y_test_institute, institute_predictions_log) * 100))

print("\nLogistic Regression (Program Prediction):")
print("Accuracy: {:.2f}%".format(accuracy_score(y_test_program, program_predictions_log) * 100))

print("\nLogistic Regression (Round Prediction):")
print("Accuracy: {:.2f}%".format(accuracy_score(y_test_round, round_predictions_log) * 100))

# KNN Evaluation
print("\nKNN (Institute Prediction):")
print("Accuracy: {:.2f}%".format(accuracy_score(y_test_institute, institute_predictions_knn) * 100))

print("\nKNN (Program Prediction):")
print("Accuracy: {:.2f}%".format(accuracy_score(y_test_program, program_predictions_knn) * 100))

print("\nKNN (Round Prediction):")
print("Accuracy: {:.2f}%".format(accuracy_score(y_test_round, round_predictions_knn) * 100))

# SVM Evaluation
print("\nSVM (Institute Prediction):")
print("Accuracy: {:.2f}%".format(accuracy_score(y_test_institute, institute_predictions_svm) * 100))

print("\nSVM (Program Prediction):")
print("Accuracy: {:.2f}%".format(accuracy_score(y_test_program, program_predictions_svm) * 100))

print("\nSVM (Round Prediction):")
print("Accuracy: {:.2f}%".format(accuracy_score(y_test_round, round_predictions_svm) * 100))

# Naive Bayes Evaluation
print("\nNaive Bayes (Institute Prediction):")
print("Accuracy: {:.2f}%".format(accuracy_score(y_test_institute, institute_predictions_nb) * 100))

print("\nNaive Bayes (Program Prediction):")
print("Accuracy: {:.2f}%".format(accuracy_score(y_test_program, program_predictions_nb) * 100))

print("\nNaive Bayes (Round Prediction):")
print("Accuracy: {:.2f}%".format(accuracy_score(y_test_round, round_predictions_nb) * 100))

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the data
data = pd.read_csv('2022.csv')  # Adjust to your file path

# Select relevant columns
data = data[["Institute", "Academic Program Name", "Seat Type", "Opening Rank", "Closing Rank", "Round"]]

# Drop rows with missing values
data = data.dropna()

# Encode categorical features
label_encoders = {}
for col in ["Institute", "Academic Program Name", "Seat Type"]:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Convert "Opening Rank" and "Closing Rank" to numeric types
data["Opening Rank"] = pd.to_numeric(data["Opening Rank"], errors="coerce")
data["Closing Rank"] = pd.to_numeric(data["Closing Rank"], errors="coerce")

# Drop rows where ranks couldn't be converted
data = data.dropna(subset=["Opening Rank", "Closing Rank"])

# Features and targets
X = data[["Seat Type", "Opening Rank", "Closing Rank"]]
y_institute = data["Institute"]
y_program = data["Academic Program Name"]
y_round = data["Round"]

# Split into training and testing sets
X_train, X_test, y_train_institute, y_test_institute = train_test_split(X, y_institute, test_size=0.2, random_state=42)
_, _, y_train_program, y_test_program = train_test_split(X, y_program, test_size=0.2, random_state=42)
_, _, y_train_round, y_test_round = train_test_split(X, y_round, test_size=0.2, random_state=42)

# Standardize numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define hyperparameter grid for KNN
param_grid = {
    'n_neighbors': [3, 5, 7, 9, 11],
    'weights': ['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan', 'minkowski']
}

# Fine-tune KNN for Institute Prediction
grid_search_institute = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, scoring='accuracy')
grid_search_institute.fit(X_train, y_train_institute)
best_knn_institute = grid_search_institute.best_estimator_
institute_predictions_knn = best_knn_institute.predict(X_test)
print("\nFine-tuned KNN (Institute Prediction):")
print("Best Parameters:", grid_search_institute.best_params_)
print("Accuracy:", accuracy_score(y_test_institute, institute_predictions_knn))


# Fine-tune KNN for Program Prediction
grid_search_program = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, scoring='accuracy')
grid_search_program.fit(X_train, y_train_program)
best_knn_program = grid_search_program.best_estimator_
program_predictions_knn = best_knn_program.predict(X_test)
print("\nFine-tuned KNN (Program Prediction):")
print("Best Parameters:", grid_search_program.best_params_)
print("Accuracy:", accuracy_score(y_test_program, program_predictions_knn))


# Fine-tune KNN for Round Prediction
grid_search_round = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, scoring='accuracy')
grid_search_round.fit(X_train, y_train_round)
best_knn_round = grid_search_round.best_estimator_
round_predictions_knn = best_knn_round.predict(X_test)
print("\nFine-tuned KNN (Round Prediction):")
print("Best Parameters:", grid_search_round.best_params_)
print("Accuracy:", accuracy_score(y_test_round, round_predictions_knn))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Load the dataset
data = pd.read_csv('2022.csv')

# Replace 'OPEN' with 0 in Opening and Closing Rank and convert to numeric
data["Opening Rank"] = pd.to_numeric(data["Opening Rank"].replace("OPEN", 0), errors="coerce")
data["Closing Rank"] = pd.to_numeric(data["Closing Rank"].replace("OPEN", 0), errors="coerce")

# Drop rows with missing values across relevant columns
data.dropna(subset=["Seat Type", "Opening Rank", "Closing Rank", "Institute", "Academic Program Name", "Round"], inplace=True)

# Define features and targets
X = data[["Seat Type", "Opening Rank", "Closing Rank"]]
y_institute = data["Institute"]
y_program = data["Academic Program Name"]
y_round = data["Round"]

# Encode 'Seat Type' into numeric values if it is categorical
X["Seat Type"] = X["Seat Type"].astype('category').cat.codes

# Train-test split for all three targets
X_train, X_test, y_train_institute, y_test_institute = train_test_split(X, y_institute, test_size=0.2, random_state=42)
_, _, y_train_program, y_test_program = train_test_split(X, y_program, test_size=0.2, random_state=42)
_, _, y_train_round, y_test_round = train_test_split(X, y_round, test_size=0.2, random_state=42)

# Initialize the KNN model
knn_model = KNeighborsClassifier(n_neighbors=5)

# ===== INSTITUTE PREDICTION =====
# Train and predict for Institute
knn_model.fit(X_train, y_train_institute)
institute_predictions_knn = knn_model.predict(X_test)

# Evaluate Institute Prediction
accuracy_institute = accuracy_score(y_test_institute, institute_predictions_knn) * 100
precision_institute = precision_score(y_test_institute, institute_predictions_knn, average='weighted')
recall_institute = recall_score(y_test_institute, institute_predictions_knn, average='weighted')
f1_institute = f1_score(y_test_institute, institute_predictions_knn, average='weighted')

print("\nEvaluation for Institute Prediction:")
print("Accuracy: {:.2f}%".format(accuracy_institute))
print("Precision (Weighted): {:.2f}".format(precision_institute))
print("Recall (Weighted): {:.2f}".format(recall_institute))
print("F1-Score (Weighted): {:.2f}".format(f1_institute))


# ===== PROGRAM PREDICTION =====
# Train and predict for Program
knn_model.fit(X_train, y_train_program)
program_predictions_knn = knn_model.predict(X_test)

# Evaluate Program Prediction
accuracy_program = accuracy_score(y_test_program, program_predictions_knn) * 100
precision_program = precision_score(y_test_program, program_predictions_knn, average='weighted')
recall_program = recall_score(y_test_program, program_predictions_knn, average='weighted')
f1_program = f1_score(y_test_program, program_predictions_knn, average='weighted')

print("\nEvaluation for Academic Program Name Prediction:")
print("Accuracy: {:.2f}%".format(accuracy_program))
print("Precision (Weighted): {:.2f}".format(precision_program))
print("Recall (Weighted): {:.2f}".format(recall_program))
print("F1-Score (Weighted): {:.2f}".format(f1_program))


# ===== ROUND PREDICTION =====
# Train and predict for Round
knn_model.fit(X_train, y_train_round)
round_predictions_knn = knn_model.predict(X_test)

# Evaluate Round Prediction
accuracy_round = accuracy_score(y_test_round, round_predictions_knn) * 100
precision_round = precision_score(y_test_round, round_predictions_knn, average='weighted')
recall_round = recall_score(y_test_round, round_predictions_knn, average='weighted')
f1_round = f1_score(y_test_round, round_predictions_knn, average='weighted')

print("\nEvaluation for Round Prediction:")
print("Accuracy: {:.2f}%".format(accuracy_round))
print("Precision (Weighted): {:.2f}".format(precision_round))
print("Recall (Weighted): {:.2f}".format(recall_round))
print("F1-Score (Weighted): {:.2f}".format(f1_round))


# ===== SUMMARY TABLE =====
print("\nSummary of Metrics:")

print(f"\nInstitute Prediction:")
print(f"Accuracy: {accuracy_institute:.2f}%")
print(f"Precision (Weighted): {precision_institute:.2f}")
print(f"Recall (Weighted): {recall_institute:.2f}")
print(f"F1-Score (Weighted): {f1_institute:.2f}")

print(f"\nProgram Prediction:")
print(f"Accuracy: {accuracy_program:.2f}%")
print(f"Precision (Weighted): {precision_program:.2f}")
print(f"Recall (Weighted): {recall_program:.2f}")
print(f"F1-Score (Weighted): {f1_program:.2f}")

print(f"\nRound Prediction:")
print(f"Accuracy: {accuracy_round:.2f}%")
print(f"Precision (Weighted): {precision_round:.2f}")
print(f"Recall (Weighted): {recall_round:.2f}")
print(f"F1-Score (Weighted): {f1_round:.2f}")

