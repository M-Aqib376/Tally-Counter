import tkinter as tk   #Gui,lable,button bnany k lay
from datetime import date #ye library date nekalny k lay istamal hovi hai
import json #json file data ko file me text ki form store krny k lay istamal hoti hai. 
import os  #os ye check krti hai k file me data hai ya nhi

FILE_NAME = "counter_data.json" #ye file ka name hai jahan data store krty hai


data = {} #   ye previous date ky data ko store krta hai.
if os.path.exists(FILE_NAME):
    try:
        with open(FILE_NAME, "r") as file: # is used to open the file in read mode ("r").ye open function file handler ka kam krti hai     khud open or close hota hai
            data = json.load(file)  # ye python ka function hai jo json file ko read kr k dictionary me change kr deta hai
    except json.JSONDecodeError:
        data = {}

def save_data():
    data[date.today().isoformat()] = count
    with open(FILE_NAME, "w") as file:
        json.dump(data, file)
    status_label.config(text="Count saved!")

def show_previous():
    if data:
        result = "\n".join([f"{d}: {c}" for d, c in data.items()])
    else:
        result = "No saved data found."
    popup = tk.Toplevel(root)
    popup.title("Previous Counts")
    tk.Label(popup, text="Previous Data", font=("Arial", 14)).pack()
    tk.Message(popup, text=result, width=300).pack()

def increase():
    global count
    count += 1
    update_label()


def reset():
    global count, last_count
    last_count = count
    count = 0
    update_label()
    status_label.config(text="Count reset. You can undo.")

def undo_reset():
    global count
    count = last_count
    update_label()
    status_label.config(text="Reset undone.")

def update_label():
    label.config(text=str(count))
    status_label.config(text="")

count = 0
last_count = 0

root = tk.Tk()   #This creates the main window for a GUI application.
root.title("Tally Counter") #An identifier (variable) that holds the reference to the main window.Set the title of the window





label = tk.Label(root, text=str(count), font=("Arial", 50))
label.pack(pady=20) #This method is used to display the label on the window.
                    # Padding in the y-direction (vertical)

tk.Button(root, text="Increase", command=increase, width=15).pack(pady=2)

tk.Button(root, text="Reset", command=reset, width=15).pack(pady=2)
tk.Button(root, text="Undo Reset", command=undo_reset, width=15).pack(pady=2)
tk.Button(root, text="Save Count", command=save_data, width=15).pack(pady=2)
tk.Button(root, text="Show Previous Data", command=show_previous, width=15).pack(pady=2)

status_label = tk.Label(root, text="", font=("Arial", 20), fg="green")
status_label.pack(pady=5)

root.mainloop()# ye loop event k lay istamal hoti hai such button clicks, key presses, etc., and triggers

