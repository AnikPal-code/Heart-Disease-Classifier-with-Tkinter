import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from tkinter import messagebox
from sklearn.model_selection import GridSearchCV
import guiCode

def process_data(file_path):
    try:
        data = pd.read_csv(file_path)
        X = data.drop('target', axis=1)
        y = data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=101)
        train_data = pd.concat([X_train, y_train], axis=1)
        test_data = pd.concat([X_test, y_test], axis=1)

        train_data.to_csv('train_data.csv', index=False)
        test_data.to_csv('test_data.csv', index=False)

    except Exception as e:
        messagebox.showerror("Error", f"Error processing data: {str(e)}")

def train_and_test_logistic():
    try:
        train_data = pd.read_csv('train_data.csv')
        X_train = train_data.drop('target', axis=1)
        y_train = train_data['target']

        test_data = pd.read_csv('test_data.csv')
        X_test = test_data.drop('target', axis=1)
        y_test = test_data['target']

        # Hyperparameter tuning with GridSearchCV
        LR_hp = {
            'C': np.logspace(-4, 4, 20),
            'solver': ['liblinear']
        }

        lr_gs = GridSearchCV(LogisticRegression(),
                             param_grid=LR_hp,
                             cv=5,
                             verbose=True)
        lr_gs.fit(X_train, y_train)

        # Evaluate the model on the test set
        predictions = lr_gs.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        report = classification_report(y_test, predictions)

        messagebox.showinfo("LogisticRegression Results", f"Accuracy: {accuracy}\n\nClassification Report:\n{report}")

    except Exception as e:
        messagebox.showerror("Error", f"Error training and testing logistic regression: {str(e)}")


def train_and_test_random_forest():
    train_and_test_classifier(RandomForestClassifier())


def train_and_test_classifier(classifier):
    try:
        train_data = pd.read_csv('train_data.csv')
        classifier.fit(train_data.drop('target', axis=1), train_data['target'])

        test_data = pd.read_csv('test_data.csv')
        predictions = classifier.predict(test_data.drop('target', axis=1))

        accuracy = accuracy_score(test_data['target'], predictions)
        report = classification_report(test_data['target'], predictions)

        messagebox.showinfo(f"{classifier.__class__.__name__} Results", f"Accuracy: {accuracy}\n\nClassification Report:\n{report}")

    except Exception as e:
        messagebox.showerror("Error", f"Error training and testing model: {str(e)}")


def analyze(user_values):
    try:
        model = RandomForestClassifier()
        train_data = pd.read_csv('train_data.csv')
        model.fit(train_data.drop('target', axis=1), train_data['target'])
        input_array = np.array(user_values).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        probability = model.predict_proba(input_array)[0][1]

        result_text = f"Output: {'Heart Disease' if prediction == 1 else 'No Heart Disease'}\nProbability: {probability:.4f}"

        return result_text


    except Exception as e:
        return f"Error analyzing: {str(e)}"
