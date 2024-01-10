# import module from tkinter for UI
from tkinter import *
import os
from datetime import datetime;

# creating instance of TK
root = Tk()

root.configure(background="black")


# root.geometry("300x300")

def function1():
    os.system("py Pedestrian.py")


def function2():
    os.system("py Pedestrian_vid.py")


def function3():
    os.system("py lane.py")


def function6():
    root.destroy()


# stting title for the window
root.title("Detections")

# creating a text label
Label(root, text="Pedestrian and Lane Detection System", font=("times new roman", 20), fg="white",
      bg="black", height=3).grid(row=0, rowspan=2, columnspan=2, sticky=N + E + W + S, padx=8, pady=8)

Label(root, text="Members of the Project Group", font=("times new roman", 15),
      fg="white", bg="black", height=3).grid(row=1, rowspan=2, columnspan=2, sticky=N + E + W + S, padx=10, pady=10)

Label(root, text="Pranav Patil, Sanket Golar, Atharv Thakur, Ashwajeet Fulzele", font=("times new roman", 12),
      fg="white", bg="black", height=3).grid(row=2, rowspan=2, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating first button
Button(root, text="Pedestrian Detecton(Image)", font=("times new roman", 20), bg="#000000", fg='green', command=function1).grid(row=4,
                                                                                                                  columnspan=2,
                                                                                                                  sticky=W + E + N + S,
                                                                                                                  padx=5,
                                                                                                                  pady=5)

# creating second button
Button(root, text="Pedestrian Detection(Video)", font=("times new roman", 20), bg="#000000", fg='green', command=function2).grid(
    row=6, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating third button
Button(root, text="Lane Detection", font=('times new roman', 20), bg="#000000", fg="green",
       command=function3).grid(row=7, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

Button(root, text="Exit", font=('times new roman', 20), bg="black", fg="red", command=function6).grid(row=9,
                                                                                                      columnspan=2,
                                                                                                      sticky=N + E + W + S,
                                                                                                      padx=5, pady=5)

root.mainloop()