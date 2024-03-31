import tkinter as tk
from tkinter import*
from tkinter import ttk
import random
from random import randint

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("570x600+100+200")
root.resizable(True, True)
root.config(bg="lightcyan3")


image = tk.PhotoImage(file=r"C:\DHANYASRI\RPS2.png")

image_label = tk.Label(root, image=image)
image_label.pack()

rock = PhotoImage(file=r"C:\DHANYASRI\rock.png")
paper = PhotoImage(file=r"C:\DHANYASRI\paper.png")
scissors = PhotoImage(file=r"C:\DHANYASRI\scissors.png")

image_list = [rock,paper,scissors]

#pick a random number 0-2
pick_num = randint(0,2)

#throw up an image
image_label = Label(root,image=image_list[pick_num],bd=0)
image_label.pack()

#spin func
def spin():
    pick_num = randint(0,2)
    image_label.config(image=image_list[pick_num])

    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissors":
        user_choice_value = 2


    #user choice is rock
    if user_choice_value == 0:
        if pick_num == 0:
            wl_label.config(text="It's a tie...! SPIN AGAIN",font=("Lucida Handwriting",14,"bold"))
        elif pick_num == 1:
            wl_label.config(text="Paper cover rock Computer wins...!SPIN AGAIN",font=("Lucida Handwriting",14,"bold"))
        elif pick_num == 2:
            wl_label.config(text="Rock smaches scissors User wins...!SPIN AGAIN",font=("Lucida Handwriting",14,"bold"))


    #user choice is paper
    if user_choice_value == 1:
        if pick_num == 0:
            wl_label.config(text="Paper cover rock User wins...!SPIN AGAIN",font=("Lucida Handwriting",14,"bold"))
        elif pick_num == 1:
            wl_label.config(text="It's a tie...! SPIN AGAIN",font=("Lucida Handwriting",14,"bold"))
        elif pick_num == 2:
            wl_label.config(text="Scissors cut paper Computer wins...!SPIN AGAIN",font=("Lucida Handwriting",14,"bold"))

    #user choice is scissors
    if user_choice_value == 2:
        if pick_num == 0:
            wl_label.config(text="Rock smaches scissors Computer wins...!SPIN AGAIN",font=("Lucida Handwriting",14,"bold"))
        elif pick_num == 1:
            wl_label.config(text="Scissors cut paper User wins SPIN AGAIN",font=("Lucida Handwriting",14,"bold"))
        elif pick_num == 2:
            wl_label.config(text="It's a tie...!SPIN AGAIN",font=("Lucida Handwriting",14,"bold"))
    

#user choice list
user_choice=ttk.Combobox(root,value=("Rock","Paper","Scissors"))
user_choice.current(0)
user_choice.pack()

#spin button
spin_button = Button(root,text="SPIN",font=("Lucida Handwriting",20,"bold"),command=spin)
spin_button.pack()

#win/lose label
wl_label=Label(root,text="",font=("Lucida Handwriting",18,"bold"))
wl_label.pack()

root.mainloop()
