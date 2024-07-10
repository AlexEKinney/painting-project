# import tk advancd module
from tkinter import *
import src.manageData as md
# open main menu
def main_menu():
    # create main menu window
    main_menu = Tk()
    main_menu.title("Python Painting Estimator Project") ## set title
    main_menu.geometry("300x300") ## we do not need that much space yet
    main_menu.resizable(False, False) ## can cause display issues 

    # create main menu label
    main_menu_label = Label(main_menu, text="Main Menu", font=("Ubuntu", 20))
    main_menu_label.pack(pady=20)

    # create main menu buttons
    # create new game button
    new_game_button = Button(main_menu, text="Create an estimate", font=("Ubuntu", 15) , command=md.createEstimate)
    new_game_button.pack(pady=10)

    # create load game button
    load_game_button = Button(main_menu, text="Manage data", font=("Ubuntu", 15), command=md.manageData)
    load_game_button.pack(pady=10)

    # create exit button
    exit_button = Button(main_menu, text="Exit", font=("Ubuntu", 15), command=exit)
    exit_button.pack(pady=10)

    # run main menu
    main_menu.mainloop()



main_menu()