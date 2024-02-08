import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
from tkinter.ttk import Combobox


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        file_name = file_path.split("/")[-1]
        label.config(text=f"Selected file: {file_name}")
        process_data(file_path)


def process_data(file_path):
    try:
        data = pd.read_csv(file_path)
        X = data.drop('target', axis=1)
        y = data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
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

        classifier = LogisticRegression()
        classifier.fit(X_train, y_train)

        predictions = classifier.predict(X_test)

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


def predict():
    try:
        user_values = [float(x.strip()) for x in entry_user_values.get().split(',')]

        model = RandomForestClassifier()

        train_data = pd.read_csv('train_data.csv')
        model.fit(train_data.drop('target', axis=1), train_data['target'])

        input_array = np.array(user_values).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        probability = model.predict_proba(input_array)[0][1]

        messagebox.showinfo("Prediction Result",
                            f"Output: {'Heart Disease' if prediction == 1 else 'No Heart Disease'}\nProbability: {probability:.4f}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values separated by commas.")
    except Exception as e:
        messagebox.showerror("Error", f"Error predicting: {str(e)}")


def analyze():
    try:
        gender = selection()
        fbs_value = selection2()
        exang_value = selection3()
        cp_value = selection4()
        slope_value = selection5()
        trestbps_value = float(trestbps.get())
        chol_value = float(chol.get())
        thalach_value = float(thalach.get())
        oldpeak_value = float(oldpeak.get())

        user_values = [gender, fbs_value, exang_value, cp_value, restecg_combobox.get(), slope_value, ca_combobox.get(),
                       thal_combobox.get(),
                       choice, trestbps_value, chol_value, thalach_value, oldpeak_value]

        model = RandomForestClassifier()

        train_data = pd.read_csv('train_data.csv')
        model.fit(train_data.drop('target', axis=1), train_data['target'])

        input_array = np.array(user_values).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        probability = model.predict_proba(input_array)[0][1]

        report.config(
            text=f"Output: {'Heart Disease' if prediction == 1 else 'No Heart Disease'}\nProbability: {probability:.4f}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid values.")
    except Exception as e:
        messagebox.showerror("Error", f"Error analyzing: {str(e)}")


if __name__ == "__main__":

    background = "#EEC766"
    framebg = "#62a7ff"
    framefg = "#fefbfb"

    root = tk.Tk()
    root.title("Heart Disease Classifier System")
    root.geometry("1450x730+60+80")
    root.resizable(width=False, height=False)

    root.config(bg=background)
    image_icon = PhotoImage(file="icon.png")
    root.iconphoto(False, image_icon)

    Detail_entry = Frame(root, width=490, height=260, bg="#dbe0e3", bd=1)

    Detail_entry.place(x=30, y=450)


    Label(Detail_entry, text="sex:", font="arial 13", bg=framebg, fg=framefg).place(x=10, y=10)
    Label(Detail_entry, text="fbs:", font="arial 13", bg=framebg, fg=framefg).place(x=180, y=10)
    Label(Detail_entry, text="exang:", font="arial 13", bg=framebg, fg=framefg).place(x=335, y=10)

    def selection():
        if gen.get() == 1:
            Gender=1
            return(Gender)
            print(Gender)
        elif gen.get()==2:
            Gender=0
            return (Gender)
            print(Gender)
        else:
            print(Gender)

    def selection2():
        if fbs.get() == 1:
            Fbs=1
            return(Fbs)
            print(Fbs)
        elif fbs.get()==2:
            Fbs=0
            return (Fbs)
            print(Fbs)
        else:
            print(Fbs)

    def selection3():
        if exang.get() == 1:
            Exang = 1
            return (Exang)
            print(Exang)
        elif exang.get() == 2:
            Exang = 0
            return (Exang)
            print(Exang)
        else:
            print(Exang)


    gen = IntVar()
    R1 = Radiobutton(Detail_entry, text='Male', variable=gen, value=1, command=selection)
    R2 = Radiobutton(Detail_entry, text='Female', variable=gen, value=2, command=selection)
    R1.place(x=43, y=10)
    R2.place(x=93, y=10)

    fbs = IntVar()
    R3 = Radiobutton(Detail_entry, text='True', variable=fbs, value=1, command=selection)
    R4 = Radiobutton(Detail_entry, text='False', variable=fbs, value=2, command=selection)
    R3.place(x=213, y=10)
    R4.place(x=263, y=10)

    exang = IntVar()
    R5 = Radiobutton(Detail_entry, text='Yes', variable=exang, value=1, command=selection)
    R6 = Radiobutton(Detail_entry, text='No', variable=exang, value=2, command=selection)
    R5.place(x=387, y=10)
    R6.place(x=430, y=10)

    Label(Detail_entry, text="cp:", font='arial 13', bg=framebg, fg=framefg).place(x=10, y=50)
    Label(Detail_entry, text="restecg:", font='arial 13', bg=framebg, fg=framefg).place(x=10, y=90)
    Label(Detail_entry, text="slope:", font='arial 13', bg=framebg, fg=framefg).place(x=10, y=130)
    Label(Detail_entry, text="ca:", font='arial 13', bg=framebg, fg=framefg).place(x=10, y=170)
    Label(Detail_entry, text="thal:", font='arial 13', bg=framebg, fg=framefg).place(x=10, y=210)

    def selection4():
        input = cp_combobox.get()
        if input == "0 = typical anginal":
            return (0)
        elif input == "1 = atypical angina":
            return (1)
        elif input == "2 = non-aniginal pain":
            return (2)
        elif input == "3 = asymptomatic":
            return (3)
        else:
            print(Exang)

    def selection5():
        input = slope_combobox.get()
        if input == "0 = upsloping":
            return (0)
        elif input == "1 = flat":
            return (1)
        elif input == "2 = downsloping":
            return (2)
        else:
            print(Exang)

    cp_combobox = Combobox(Detail_entry, values=['0 = typical angina', '1 = atypical angina', '2 = non-aniginal pain', '3 = asymptomatic'], font="arial 14", state="r", width=14)
    restecg_combobox = Combobox(Detail_entry, values=['0', '1', '2'], font="arial 12", state="r", width=11)
    slope_combobox = Combobox(Detail_entry, values=['0 = upsloping', '1 = flat', '2 = downsloping'], font="arial 12", state="r", width=12)
    ca_combobox = Combobox(Detail_entry, values=['0', '1', '2', '3', '4'], font="arial 12", state="r", width=14)
    thal_combobox = Combobox(Detail_entry, values=['0', '1', '2', '3'], font="arial 12", state="r", width=14)

    cp_combobox.place(x=50, y=50)
    restecg_combobox.place(x=80, y=90)
    slope_combobox.place(x=70, y=130)
    ca_combobox.place(x=50, y=170)
    thal_combobox.place(x=50, y=210)

    Label(Detail_entry, text="Smoking", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=50)
    Label(Detail_entry, text="trestbps:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=90)
    Label(Detail_entry, text="chol:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=130)
    Label(Detail_entry, text="thalach:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=170)
    Label(Detail_entry, text="oldpeak:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=210)

    trestbps = StringVar()
    chol = StringVar()
    thalach = StringVar()
    oldpeak = StringVar()

    trestbps_entry = Entry(Detail_entry, textvariable=trestbps, width=10, font='arial 15', bg="#ededed", fg="#222222", bd=0)
    chol_entry = Entry(Detail_entry, textvariable=chol, width=10, font='arial 15', bg="#ededed", fg="#222222", bd=0)
    thalach_entry = Entry(Detail_entry, textvariable=thalach, width=10, font='arial 15', bg="#ededed", fg="#222222", bd=0)
    oldpeak_entry = Entry(Detail_entry, textvariable=oldpeak, width=10, font='arial 15', bg="#ededed", fg="#222222", bd=0)

    trestbps_entry.place(x=320, y=90)
    chol_entry.place(x=320, y=130)
    thalach_entry.place(x=320, y=170)
    oldpeak_entry.place(x=320, y=210)

    square_report_image = PhotoImage(file="Report.png")
    report_background = Label(image=square_report_image, bg=background)
    report_background.place(x=1120, y=340)

    report = Label(root, font="arial 25 bold", bg="white", fg="#8dc63f")
    report.place(x=1170, y=550)

    report1 = Label(root, font="arial 10 bold", bg="white")
    report1.place(x=1130, y=610)

    analysis_button = PhotoImage(file="Analysis.png")
    Button(root, image=analysis_button, bd=0, bg=background, cursor="hand2").place(x=1130, y=240)

    button_mode = True
    choice = "smoking"
    def changemode():
        global button_mode, choice
        if button_mode:
            choice = "non_smoking"
            mode.config(image=non_smoking_icon, activebackground="white")
            button_mode = False
        else:
            choice = "smoking"
            mode.config(image=smoking_icon, activebackground="white")
            button_mode = True
        print(choice)


    smoking_icon = PhotoImage(file="smoker.png")
    non_smoking_icon = PhotoImage(file="non-smoker.png")
    mode = Button(root, image=smoking_icon, bg="#dbe0e3", bd=0, cursor="hand2", command=changemode)
    mode.place(x=350, y=495)



    logo = PhotoImage(file="images.png")
    label = tk.Label(root, text="Select CSV file:")
    label.pack(pady=10)
    label.place(x=100, y=400)


    browse_button = tk.Button(root, text="Browse", command=browse_file)
    browse_button.pack(pady=10)
    browse_button.place(x=195, y=400)


    Label(text="Training type:", font="arial 12", bg=framebg, fg=framefg).place(x=1000, y=50)
    train_type_combobox = Combobox(root, values=['Logistic', 'Random Forest'], font="arial 13", state='readonly', width=10)
    train_type_combobox.place(x=1100, y=50)
    train_type_combobox.set('None')


    label_predict = tk.Label(root, text="Enter values for independent variables ie. X-variables (comma-separated):")
    label_predict.pack(pady=10)

    entry_user_values = tk.Entry(root, width=50)
    entry_user_values.pack(pady=10)

    submit_button = tk.Button(root, text="Submit", command=predict)
    submit_button.pack(pady=10)


    root.mainloop()
