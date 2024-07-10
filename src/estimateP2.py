from tkinter import *
import tkinter as tk
import csv
import os
from uuid import uuid4
from time import time

def calc(i):

    def createCustomer():
        ## open customer csv
        with open("data/customer.csv", mode="r+") as customer_file:
            ## make customer with the next id in the list
            ## we first go to last line and get the id
            nextId = customer_file.readlines()[-1].split(",")[0]
            ## then we write the new customer
            customer_writer = csv.writer(customer_file)
            customer_writer.writerow([str(int(nextId)+1)])
            id = int(nextId)+1
            os.makedirs("customerData/"+str(id))
            ## now clear screen
            create_estimate.destroy() 
            roomQuotes(id, i)
    ## open dialog 
    create_estimate = Tk()
    create_estimate.title("Create Estimate")
    create_estimate.geometry("500x800")
    create_estimate.resizable(False, False)
    ## welcome msg
    employee_details_label = Label(create_estimate, text="Welcome user", font=("Ubuntu", 20))
    employee_details_label.pack(pady=20)
    ## button create id / enter id
    customer_buttom_create = Button(create_estimate, text="Create Customer", font=("Ubuntu", 15), command=lambda: createCustomer())
    customer_buttom_create.pack(pady=10)
    ## button create enter id
    ## text field as well so less dialog
    customer_detials_label= Label(create_estimate, text="Enter Customer ID", font=("Ubuntu", 15))
    customer_detials_label.pack(pady=10)
    customer_id_entry = Entry(create_estimate, font=("Ubuntu", 15))
    customer_id_entry.pack(pady=10)
    ## button create estimate
    customer_buttom_create = Button(create_estimate, text="Continue", font=("Ubuntu", 15), command=lambda: roomQuotes(customer_id_entry.get(), i))
    customer_buttom_create.pack(pady=10)

def roomQuotes(id, i):
    def addRoom():
        def saveData(name, wallpaper, height):
            def saveData2(name, wallpaper, heights, widths):
                    file_path = f"customerData/{id}/{uuid}.csv"
                    
                    # Ensure the directory exists
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    
                    with open(file_path, mode="a", newline='') as roomQuotes_file:
                        roomQuotes_writer = csv.writer(roomQuotes_file)
                        # Write the room header
                        roomQuotes_writer.writerow([f"Room: {name}", f"Wallpaper: {wallpaper}"])
                        for i in range(len(heights)):
                            roomQuotes_writer.writerow(["", "", heights[i], widths[i]])
                            
                    add_room.destroy()
                    walls.destroy()
                    room_list.delete(0, END)
                    with open(file_path, mode="r") as roomQuotes_file:
                        roomQuotes_reader = csv.reader(roomQuotes_file)
                        for row in roomQuotes_reader:
                            if len(row) > 0:
                                room_list.insert(END, row)
            walls = Tk()
            walls.title("Add Room")
            walls.geometry("500x800")
            walls.resizable(False, False)

            canvas = Canvas(walls)
            scrollbar = Scrollbar(walls, orient="vertical", command=canvas.yview)
            scrollable_frame = Frame(canvas)
            scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            height_entries = []
            width_entries = []

            for i in range(int(height)):
                wall = Frame(scrollable_frame)
                wall.pack(pady=10)
                height_label = Label(wall, text="Height", font=("Ubuntu", 15))
                height_label.pack(pady=10)
                height_entry = Entry(wall, font=("Ubuntu", 15))
                height_entry.pack(pady=10)
                height_entries.append(height_entry)
                width_label = Label(wall, text="Width", font=("Ubuntu", 15))
                width_label.pack(pady=10)
                width_entry = Entry(wall, font=("Ubuntu", 15))
                width_entry.pack(pady=10)
                width_entries.append(width_entry)

            def collect_data_and_save():
                heights = [entry.get() for entry in height_entries]
                widths = [entry.get() for entry in width_entries]
                saveData2(name, wallpaper, heights, widths)

            saveButton = Button(walls, text="Save", font=("Ubuntu", 15), command=collect_data_and_save)
            saveButton.pack(pady=10)
      

        ## open dialog
        add_room = Tk()
        add_room.title("Add Room")
        add_room.geometry("500x800")
        add_room.resizable(False, False)
        ## add room name
        room_name_label = Label(add_room, text="Enter Room Name", font=("Ubuntu", 15))
        room_name_label.pack(pady=10)
        room_name_entry = Entry(add_room, font=("Ubuntu", 15))
        room_name_entry.pack(pady=10)
        # create wallpaper
        employee_qualification_label = Label(add_room, text="Wallpaper", font=("Ubuntu", 15))
        employee_qualification_label.pack(pady=10)

        # create qualification dropdown
        options = ["R", "K"]
        clicked = StringVar(add_room)
        clicked.set(options[0])
        qualification = OptionMenu(add_room, clicked, *options)
        qualification.pack()
        ## how many walls
        height_label = Label(add_room, text="How many walls", font=("Ubuntu", 15))
        height_label.pack(pady=10)
        height_entry = Entry(add_room, font=("Ubuntu", 15))
        height_entry.pack(pady=10)



        ## add button to save backk to the csv file
        add_room_buttom_create = Button(add_room, text="Add Room", font=("Ubuntu", 15), command=lambda: saveData( room_name_entry.get(), clicked.get(), height_entry.get()))
        add_room_buttom_create.pack(pady=10)
    ## open dialog 
    create_estimate = Tk()
    create_estimate.title("Create Estimate")
    create_estimate.geometry("500x800")
    create_estimate.resizable(False, False)
    uuid = uuid4()
    print(uuid)
    ## make csv file in customer directory
    f = open("customerData/"+str(id)+"/"+str(uuid)+".csv", "a")
    f.close()
    with open("customerData/"+str(id)+"/"+str(uuid)+".csv", mode="r+") as roomQuotes_file:
        roomQuotes_writer = csv.writer(roomQuotes_file)
        ## get current time for the data requirement 
        timestamp = time()
        roomQuotes_writer.writerow([timestamp])
    ## add time to the screen#
    employee_details_label = Label(create_estimate, text="Time: "+str(timestamp), font=("Ubuntu", 20))
    employee_details_label.pack(pady=20)
    ## add worker type
    employee_qualification_label = Label(create_estimate, text=i[3], font=("Ubuntu", 15))
    employee_qualification_label.pack(pady=10)
    ## now add option to add rooms
    room_buttom_create = Button(create_estimate, text="Add Room", font=("Ubuntu", 15), command=lambda: addRoom())
    room_buttom_create.pack(pady=10)

    ## display rooms stored in customer file as table
    room_list = Listbox(create_estimate)
    ## add from csv (format: roomName, wallpaper(trueFalse), height, width)
    ### it stats from line 2, as line 1 is the timestamp
    with open("customerData/"+str(id)+"/"+str(uuid)+".csv", mode="r") as roomQuotes_file:
        roomQuotes_reader = csv.reader(roomQuotes_file)
        for row in roomQuotes_reader:
            if len(row) > 0:
                room_list.insert(END, row)
    room_list.pack(pady=10)

    ## finish
    room_buttom_create = Button(create_estimate, text="Finish", font=("Ubuntu", 15), command=lambda: finish(uuid, id, i))
    room_buttom_create.pack(pady=10)
    def finish(uuid, id, i):
        print(uuid, id, i[3])
        ## step 1. fetch from file 
        ## step 2. calculate
        ## step 3. display
        ## step 4. save (if the user wants)
        ## step 5. go back to main menu
        with open(f"customerData/{id}/{uuid}.csv", mode="r") as roomQuotes_file:
            roomQuotes_reader = csv.reader(roomQuotes_file)
            data = []
            for row in roomQuotes_reader:
                if len(row) > 0:
                    data.append(row)
        print(data)
        
        ## calculate
        ## 1. get surface area of each wall
        ## 2. get total surface area 
        ## 3. get cost  (15£ per square meter + 70£ if wallpaper is required)
        ## 4. if wallpaper == R + 70 else keep it the same
        cost = 0
        wallpaper_cost = 0
        
        for row in data:
            if row[0].startswith("Room:"):
                # Reset wallpaper flag for each new room
                wallpaper = False
                
                # Check if wallpaper is required
                for item in row:
                    if item.startswith("Wallpaper:"):
                        wallpaper = item.split(": ")[1] == "R"
                        break
                
                if wallpaper:
                    wallpaper_cost = 70
            elif len(row) >= 4 and row[2] and row[3]:
                # Process wall dimensions
                height = int(row[2])
                width = int(row[3])
                cost += 15 * height * width
                if wallpaper:
                    cost += wallpaper_cost

        print(cost)
        ## add tech cost
        ## AP = £100, FQ = £250
        if i[3] == "AP":
            cost += 100
        else:
            cost += 250
        ## add VAT
        cost += cost * 0.2
        ## display
        ## open dialog
        create_estimate = Tk()
        create_estimate.title("Create Estimate")
        create_estimate.geometry("500x800")
        create_estimate.resizable(False, False)
        ## add cost
        employee_details_label = Label(create_estimate, text="Total cost: "+str(cost), font=("Ubuntu", 20))
        employee_details_label.pack(pady=20)
        ## add save button
        room_buttom_create = Button(create_estimate, text="Save", font=("Ubuntu", 15), command=lambda: save(uuid, id, cost))
        room_buttom_create.pack(pady=10)
        ## add back button
        room_buttom_create = Button(create_estimate, text="Back", font=("Ubuntu", 15), command=lambda: back())
        room_buttom_create.pack(pady=10)
        def save(uuid, id, cost):
            ## open csv file
            with open("data/estimate.csv", mode="r+") as estimate_file:
                estimate_writer = csv.writer(estimate_file)
                estimate_writer.writerow([uuid, id, cost])
            create_estimate.destroy()
        def back():
            create_estimate.destroy()
            calc(i)