import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import Combobox
from datetime import *
import mlCode
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        file_name = file_path.split("/")[-1]
        label.config(text=f"Selected file: {file_name}")
        mlCode.process_data(file_path)


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
        age_value = int(age.get())
        restecg_value = restecg_combobox.get()
        ca_value = ca_combobox.get()
        thal_value = thal_combobox.get()

        user_values = [age_value, gender, cp_value, trestbps_value, chol_value, fbs_value, restecg_value,
                       thalach_value, exang_value, oldpeak_value, slope_value, ca_value, thal_value]

        result_text = mlCode.analyze(user_values)
        report.config(text=result_text)

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

    root.config(bg=background)
    image_icon = PhotoImage(file="icon.png")
    root.iconphoto(False, image_icon)

    define = PhotoImage(file="definition.png").subsample(1)
    define_background = Label(image=define)
    define_background.place(x=540, y=450)

    heart = PhotoImage(file="heartPhoto2.png")
    heart = heart.zoom(2)
    heart_background = Label(image=heart)
    heart_background.place(x=0, y=10)

    Heading_entry = Frame(root, width=800, height=190, bg=background)
    Heading_entry.place(x=700, y=20)

    Label(Heading_entry, text="Patient Id No: ", font='arial 13', fg=framefg, bg=framebg).place(x=40, y=0)
    Label(Heading_entry, text="Date: ", font='arial 13', fg=framefg, bg=framebg).place(x=440, y=0)
    Label(Heading_entry, text="Name of Patient: ", font='arial 13', fg=framefg, bg=framebg).place(x=40, y=90)
    Label(Heading_entry, text="Birth Year: ", font='arial 13', fg=framefg, bg=framebg).place(x=440, y=90)

    Entry_image = PhotoImage(file="Rounded Rectangle 1.png").subsample(2)

    Label(Heading_entry, image=Entry_image, bg="#df2d4b").place(x=10, y=30)
    Label(Heading_entry, image=Entry_image, bg="#df2d4b").place(x=410, y=30)
    Label(Heading_entry, image=Entry_image, bg="#df2d4b").place(x=10, y=120)
    Label(Heading_entry, image=Entry_image, bg="#df2d4b").place(x=410, y=120)

    Registration = IntVar()
    reg_entry = Entry(Heading_entry, textvariable=Registration, width=15, font="arial 15", bg="#0e5363", fg="white", bd=0)
    reg_entry.place(x=10, y=30)

    Date = StringVar()
    today = date.today()
    d1 = today.strftime("   %d-%m-%Y")
    date_entry = Entry(Heading_entry, textvariable=Date, width=15, font='arial 15', bg="#0e5363", fg="white", bd=0)
    date_entry.place(x=410, y=30)
    Date.set(d1)

    Name = StringVar()
    name_entry = Entry(Heading_entry, textvariable=Name, width=15, font="arial 15", bg="#0e5363", fg="white", bd=0)
    name_entry.place(x=10, y=120)

    BirthDate = IntVar()
    birthdate_entry = Entry(Heading_entry, textvariable=BirthDate, width=15, font="arial 15", bg="#0e5363", fg="white", bd=0)
    birthdate_entry.place(x=410, y=120)

    Detail_entry = Frame(root, width=490, height=260, bg="#F585CB", bd=1)
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


    exang = None

    def selection3():
        global exang
        if gen.get() == 1:
            exang = 1
            return exang
        elif gen.get() == 2:
            exang = 0
            return exang
        else:
            print(exang)


    def selection4():
        global exang
        input_value = cp_combobox.get()
        if input_value == "0 = typical angina":
            return exang
        elif input_value == "1 = atypical angina":
            return 1
        elif input_value == "2 = non-anginal pain":
            return 2
        elif input_value == "3 = asymptomatic":
            return 3
        else:
            print(exang)


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

    def selection5():
        input = slope_combobox.get()
        if input == "0 = upsloping":
            return (0)
        elif input == "1 = flat":
            return (1)
        elif input == "2 = downsloping":
            return (2)
        else:
            print(exang)


    cp_combobox = Combobox(Detail_entry, values=['0 = typical angina', '1 = atypical angina', '2 = non-aniginal pain', '3 = asymptomatic'], font="arial 12", state="r", width=14)
    restecg_combobox = Combobox(Detail_entry, values=['0', '1', '2'], font="arial 12", state="r", width=11)
    slope_combobox = Combobox(Detail_entry, values=['0 = upsloping', '1 = flat', '2 = downsloping'], font="arial 12", state="r", width=12)
    ca_combobox = Combobox(Detail_entry, values=['0', '1', '2', '3', '4'], font="arial 12", state="r", width=14)
    thal_combobox = Combobox(Detail_entry, values=['0', '1', '2', '3'], font="arial 12", state="r", width=14)

    cp_combobox.place(x=50, y=50)
    restecg_combobox.place(x=80, y=90)
    slope_combobox.place(x=70, y=130)
    ca_combobox.place(x=50, y=170)
    thal_combobox.place(x=50, y=210)

    Label(Detail_entry, text="Age", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=50)
    Label(Detail_entry, text="trestbps:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=90)
    Label(Detail_entry, text="chol:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=130)
    Label(Detail_entry, text="thalach:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=170)
    Label(Detail_entry, text="oldpeak:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=210)

    trestbps = StringVar()
    chol = StringVar()
    thalach = StringVar()
    oldpeak = StringVar()
    age = StringVar()

    trestbps_entry = Entry(Detail_entry, textvariable=trestbps, width=10, font='arial 12', bg="#ededed", fg="#222222", bd=0)
    chol_entry = Entry(Detail_entry, textvariable=chol, width=10, font='arial 12', bg="#ededed", fg="#222222", bd=0)
    thalach_entry = Entry(Detail_entry, textvariable=thalach, width=10, font='arial 12', bg="#ededed", fg="#222222", bd=0)
    oldpeak_entry = Entry(Detail_entry, textvariable=oldpeak, width=10, font='arial 12', bg="#ededed", fg="#222222", bd=0)
    age_entry = Entry(Detail_entry, textvariable=age, width=10, font='arial 12', bg="#ededed", fg="#222222", bd=0)

    age_entry.place(x=320, y=50)
    trestbps_entry.place(x=320, y=90)
    chol_entry.place(x=320, y=130)
    thalach_entry.place(x=320, y=170)
    oldpeak_entry.place(x=320, y=210)

    square_report_image = PhotoImage(file="Report.png")
    report_background = Label(image=square_report_image, bg=background)
    report_background.place(x=1140, y=340)

    report = Label(root, font="arial 11 bold", bg="white", fg="black")
    report.place(x=1160, y=550)


    report1 = Label(root, font="arial 11", bg="white")
    report1.place(x=1130, y=610)

    analysis_button = PhotoImage(file="Analysis.png")
    Button(root, image=analysis_button, bd=0, bg=background, cursor="hand2", command=analyze).place(x=1150, y=240)

    logo = PhotoImage(file="images.png")
    label = tk.Label(root, text="Select CSV file: ")
    label.pack(pady=10)
    label.place(x=100, y=350)

    browse_button = tk.Button(root, text="Browse", command=browse_file)
    browse_button.pack(pady=10)
    browse_button.place(x=100, y=380)

    Label(text="Training type:", font="arial 12", bg=framebg, fg=framefg).place(x=300, y=350)
    train_type_combobox = Combobox(root, values=['Logistic', 'Random Forest'], font="arial 13", state='readonly', width=10)
    train_type_combobox.place(x=400, y=350)
    train_type_combobox.set('Logistic')

    def logout():
        root.destroy()
    logout_icon = PhotoImage(file="logout.png").subsample(4)
    logout_button = Button(root, image=logout_icon, bg="#BBC0BF", cursor="hand2", bd=0, command=logout)
    logout_button.place(x=1380, y=20)


    def refresh():

        reg_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        birthdate_entry.delete(0, 'end')
        trestbps_entry.delete(0, 'end')
        chol_entry.delete(0, 'end')
        thalach_entry.delete(0, 'end')
        oldpeak_entry.delete(0, 'end')
        age_entry.delete(0, 'end')

        gen.set(0)
        fbs.set(0)
        exang.set(0)

        cp_combobox.set('')
        restecg_combobox.set('')
        slope_combobox.set('')
        ca_combobox.set('')
        thal_combobox.set('')

    refresh_icon = PhotoImage(file="refresh.png").subsample(1)
    refresh_button = Button(root, image=refresh_icon, bg="#BBC0BF", cursor="hand2", bd=0, command=refresh)
    refresh_button.place(x=800, y=250)

    root.mainloop()
