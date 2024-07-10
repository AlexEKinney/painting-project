from tkinter import *
import tkinter as tk
import csv
import src.estimateP2 as ep2
create_estimate = None
def checkE(id, name, phone, qualification):
    # open csv file and check if the employee exists
    with open('data/employee.csv', mode='r') as employee_file:
        employee_reader = csv.reader(employee_file)
        for row in employee_reader:
            if row[0] == id and row[1] == name and row[2] == phone and row[3] == qualification:
                showPopup(row)
                return
    showError()

def createEstimate():
    global create_estimate ## i love python i love python
    def onConfirm():
        id = employee_id_entry.get()
        name = employee_name_entry.get()
        phone = employee_phone_entry.get()
        qualification = clicked.get()
        checkE(id, name, phone, qualification)

    # create estimate window
    create_estimate = Tk()
    create_estimate.title("Create Estimate")
    create_estimate.geometry("500x800")
    create_estimate.resizable(False, False)

    # create employee details label
    employee_details_label = Label(create_estimate, text="Enter Employee Details", font=("Ubuntu", 20))
    employee_details_label.pack(pady=20)

    # create employee ID label
    employee_id_label = Label(create_estimate, text="Enter Employee ID", font=("Ubuntu", 15))
    employee_id_label.pack(pady=10)

    # create employee ID entry
    employee_id_entry = Entry(create_estimate, font=("Ubuntu", 15))
    employee_id_entry.pack(pady=10)

    # create employee name label
    employee_name_label = Label(create_estimate, text="Enter Employee Name", font=("Ubuntu", 15))
    employee_name_label.pack(pady=10)

    # create employee name entry
    employee_name_entry = Entry(create_estimate, font=("Ubuntu", 15))
    employee_name_entry.pack(pady=10)

    # create employee phone number label
    employee_phone_label = Label(create_estimate, text="Enter Employee Phone Number", font=("Ubuntu", 15))
    employee_phone_label.pack(pady=10)

    # create employee phone number entry
    employee_phone_entry = Entry(create_estimate, font=("Ubuntu", 15))
    employee_phone_entry.pack(pady=10)

    # create employee qualification label
    employee_qualification_label = Label(create_estimate, text="Enter Employee Qualification", font=("Ubuntu", 15))
    employee_qualification_label.pack(pady=10)

    # create qualification dropdown
    options = ["AP", "FQ"]
    clicked = StringVar(create_estimate)
    clicked.set(options[0])
    qualification = OptionMenu(create_estimate, clicked, *options)
    qualification.pack()

    # create confirm button
    confirm_button = Button(create_estimate, text="Confirm", font=("Ubuntu", 15), command=onConfirm)
    confirm_button.pack(pady=10)

    # create confirm label
    confirm_label = Label(create_estimate, text="By submitting the form, you agree to all info being correct.", font=("Ubuntu", 10))
    confirm_label.pack(pady=10)

    # create back button
    back_button = Button(create_estimate, text="Back to main menu", font=("Ubuntu", 15), command=create_estimate.destroy)
    back_button.pack(pady=10)

    create_estimate.mainloop()

def manageData():
    print("Manage Data")

def showError():
    # open popup window error
    error_window = tk.Tk()
    error_window.title("Error")
    error_window.geometry("500x200")

    # create error label
    error_label = Label(error_window, text="Employee does not exist", font=("Ubuntu", 20))
    error_label.pack(pady=20)

    # create error info label
    error_info_label = Label(error_window, text="Please check the details you entered", font=("Ubuntu", 15))
    error_info_label.pack(pady=10)

    # create back button
    back_button = Button(error_window, text="Close", font=("Ubuntu", 15), command=error_window.destroy)
    back_button.pack(pady=10)

def showPopup(employee_info):
    def onContinue():
        global create_estimate
        popup.destroy()
        create_estimate.destroy()
        ep2.calc(employee_info)

    def onCancel():
        popup.destroy()

    popup = tk.Tk()
    popup.title("Employee Info")
    popup.geometry("400x400")

    # Display employee info
    info_text = f"ID: {employee_info[0]}\nName: {employee_info[1]}\nPhone: {employee_info[2]}\nQualification: {employee_info[3]}"
    info_label = Label(popup, text=info_text, font=("Ubuntu", 15))
    info_label.pack(pady=20)

    # create continue button
    continue_button = Button(popup, text="Continue", font=("Ubuntu", 15), command=onContinue)
    continue_button.pack(pady=10)

    # create cancel button
    cancel_button = Button(popup, text="Cancel", font=("Ubuntu", 15), command=onCancel)
    cancel_button.pack(pady=10)

    popup.mainloop()

