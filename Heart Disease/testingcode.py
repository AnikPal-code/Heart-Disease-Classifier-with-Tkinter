import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

class HeartDiseaseClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Heart Disease Classifier")
        self.root.geometry("600x300")
        self.root.resizable(width=False, height=False)

        self.label = tk.Label(root, text="Select CSV file:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=10)

        self.logistic_button = tk.Button(root, text="Train and Test Logistic Regression", command=self.train_and_test_logistic)
        self.logistic_button.pack(pady=10)

        self.random_forest_button = tk.Button(root, text="Train and Test Random Forest", command=self.train_and_test_random_forest)
        self.random_forest_button.pack(pady=10)

        self.label_predict = tk.Label(root, text="Enter values for independent variables ie. X-variables (comma-separated):")
        self.label_predict.pack(pady=10)

        self.entry_user_values = tk.Entry(root, width=50)
        self.entry_user_values.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.predict)
        self.submit_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            file_name = file_path.split("/")[-1]  
            self.label.config(text=f"Selected file: {file_name}")
            self.process_data(file_path)


    def process_data(self, file_path):
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

    def train_and_test_logistic(self):
        try:
            train_data = pd.read_csv('train_data.csv')
            X_train = train_data.drop('target', axis=1)
            y_train = train_data['target']

            test_data = pd.read_csv('test_data.csv')
            X_test = test_data.drop('target', axis=1)
            y_test = test_data['target']

            classifier = LogisticRegression()
            classifier.fit(X_train, y_train)

            predictions = classifier.predict(X_test)

            accuracy = accuracy_score(y_test, predictions)
            report = classification_report(y_test, predictions)

            messagebox.showinfo("LogisticRegression Results", f"Accuracy: {accuracy}\n\nClassification Report:\n{report}")

        except Exception as e:
            messagebox.showerror("Error", f"Error training and testing logistic regression: {str(e)}")

    def train_and_test_random_forest(self):
        self.train_and_test_classifier(RandomForestClassifier())

    def train_and_test_classifier(self, classifier):
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

    def predict(self):
        try:
            user_values = [float(x.strip()) for x in self.entry_user_values.get().split(',')]

            model = RandomForestClassifier()  

            train_data = pd.read_csv('train_data.csv')
            model.fit(train_data.drop('target', axis=1), train_data['target'])

            input_array = np.array(user_values).reshape(1, -1)
            prediction = model.predict(input_array)[0]
            probability = model.predict_proba(input_array)[0][1]

            messagebox.showinfo("Prediction Result", f"Output: {'Heart Disease' if prediction == 1 else 'No Heart Disease'}\nProbability: {probability:.4f}")

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values separated by commas.")
        except Exception as e:
            messagebox.showerror("Error", f"Error predicting: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HeartDiseaseClassifierApp(root)
    root.mainloop()
