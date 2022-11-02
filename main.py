# -------------- All imported files and libraries Starts Here-----
from tkinter import *
import random
from tkinter import messagebox

# For Background Image
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
# to run file directory
import os
# Read content using url
import urllib.request
# open url in brower for feedback
import webbrowser

# -------------- All imported files and libraries Ends Here----------------

# -------------- Color Changing and logo Variables Starts here -----------

# Window Icon or logo
logo = "assets/images/enally.ico"
# Background Image Location
wall_now = "assets/images/parking.png"
wall_now2 = "assets/images/parking2.png"
wall_now3 = "assets/images/parkin3.png"

# main background
bg = '#DBE9F7'
fg = '#fff'
fg2 = "#000"


# heading color
heading = "#021639"

# name Submit button
button_bg = "#F5DEB3"

# footer lable win and Alert color
footer_label = "#F2D40F"
footer_label_social = "#C00000"
footer_label2 = "#F8E94F"
footer_fg = "#000"

# All popup window color (Menu bar)
pop_window_color_Menu_bar = "#B7C5D5"

# fonts 

main_text = "Arial Rounded MT Bold"

# -------------- Color Changing and logo Variables Ends here ------------------

#Main window dragagger function
#mouse click saver
def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

#mouse click location tracker
def Dragging(event):
    x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
    window.geometry("+%s+%s" % (x , y))


# ------------------- Main Windows Starts Here ----------------
window = Tk()
window.title("Parking Management System")
window.iconbitmap(logo)
window.geometry("961x446")
#window['background'] = bg

#---> Hide Title Bar and calling draggable function
window.overrideredirect(1) 
window.bind('<Button-1>', SaveLastClickPos)
window.bind('<B1-Motion>', Dragging)

# Background image setup
window_background = PhotoImage(file=wall_now)
l = Label(window, image=window_background)
l.place(x=0, y=10, relwidth=1, relheight=1)


# Login
def login():
    window5 = tk.Toplevel()
    window5.iconbitmap(logo)
    window5.geometry("446x446")
    window5.title('Login')
    window5.config(background=pop_window_color_Menu_bar)

    window_background_material = PhotoImage(file=wall_now2)
    material_lable = Label(window5, image=window_background_material)
    material_lable.place(x=0, y=10, relwidth=1, relheight=1)

    # Window Heading
    credit_label = Label(window5, width=100, text="Welcome Back", font=("'Helvetica 21"), background=heading, foreground=fg)
    credit_label.pack(pady=0)

    credit_label = Label(window5, width=100, text="Login", font=("'Helvetica 16"), background=heading, foreground=fg)
    credit_label.pack(pady=6)

     # Username label
    username_label = Label(window5, text="Username: " ,font=(main_text, 12,), width = 10, bg=heading, fg="white" )
    username_label.place(y=114,x=50)

    # Password label
    username_label = Label(window5, text="Password: " ,  font=(main_text, 12,), width = 10, bg=heading, fg="white" )
    username_label.place(y=164,x=50)

    # Username input
    username = tk.Text(window5,bd=1,height=1, font=(main_text, 13,), width=15, bg=footer_label)
    username.place(y=115,x=160)

    password = tk.Text(window5,bd=1,height=1, font=(main_text, 13,), width=15, bg=footer_label)
    password.place(y=165,x=160)

    register_btn = Button(window5, text="Login", width=10, height=1, command=window.destroy, font=(main_text, 12), bd=1, background="#851519", foreground="white")
    register_btn.place(x=185, y=210)

    restPass = Label(window5, text="Reset Password" ,font=(main_text, 9,),  width = 20, bg=heading, fg="white" )
    restPass.place(y=250,x=70)

    username_label = Label(window5, text="New User" ,font=(main_text, 9,),  width = 10, bg=heading, fg=footer_label )
    username_label.place(y=250,x=210)

    window5.mainloop()

# Register
def register():
    window6 = tk.Toplevel()
    window6.iconbitmap(logo)
    window6.geometry("446x446")
    window6.title('Register')
    window6.config(background=pop_window_color_Menu_bar)

    window_background_material = PhotoImage(file=wall_now3)
    material_lable = Label(window6, image=window_background_material)
    material_lable.place(x=0, y=10, relwidth=1, relheight=1)

    # Window Heading
    credit_label = Label(window6, width=100, text="Welcome", font=("'Helvetica 21"), background=heading, foreground=fg)
    credit_label.pack(pady=0)

    credit_label = Label(window6, width=100, text="Register", font=("'Helvetica 16"), background=heading, foreground=fg)
    credit_label.pack(pady=6)

    # Username label    
    userName = Label(window6, text="Name: " ,font=(main_text, 12,), width = 10, bg=heading, fg="white" )
    userName.place(y=114,x=50)

    regNo = Label(window6, text="Reg NO: " ,font=(main_text, 12,), width = 10, bg=heading, fg="white" )
    regNo.place(y=154,x=50)    

    hostelBlock = Label(window6, text="Hostel/Block: " ,font=(main_text, 12,), width = 10, bg=heading, fg="white" )
    hostelBlock.place(y=192,x=50)

    mobNo = Label(window6, text="Mobile No: " ,font=(main_text, 12,), width = 10, bg=heading, fg="white")
    mobNo.place(y=228,x=50)

    emailId = Label(window6, text="Email ID: " ,font=(main_text, 12,), width = 10, bg=heading, fg="white")
    emailId.place(y=268,x=50)

    gender = Label(window6, text="Gender: " ,font=(main_text, 12,), width = 10, bg=heading, fg="white")
    gender.place(y=306,x=50)

    userNameInput = tk.Text(window6,bd=1,height=1, font=(main_text, 13,), width=15, bg=footer_label)
    userNameInput.place(y=115,x=210)

    regNoInput = tk.Text(window6,bd=1,height=1, font=(main_text, 13,), width=15, bg=footer_label)
    regNoInput.place(y=155,x=210)

    hostelBlockInput = tk.Text(window6,bd=1,height=1, font=(main_text, 13,), width=15, bg=footer_label)
    hostelBlockInput.place(y=193,x=210)

    mobNoInput = tk.Text(window6,bd=1,height=1, font=(main_text, 13,), width=15, bg=footer_label)
    mobNoInput.place(y=229,x=210)

    emailIdInput = tk.Text(window6,bd=1,height=1, font=(main_text, 13,), width=15, bg=footer_label)
    emailIdInput.place(y=268,x=210)

    v = StringVar(window6, "1")

    Radiobutton(window6, text = "Male", variable = v, value = "Male", indicator = 0, width=5, background = footer_label).place(y=306,x=215)
    Radiobutton(window6, text = "Female", variable = v, value = "Female", indicator = 0, width=5, background = footer_label).place(y=306,x=265)
    Radiobutton(window6, text = "Other", variable = v, value = "Other", indicator = 0, width=5, background = footer_label).place(y=306,x=315)
    
    register_btn = Button(window6, text="Register", width=10, height=1, command=window.destroy, font=(main_text, 12), bd=1, background="#851519", foreground="white")
    register_btn.place(x=235, y=340)

    window6.mainloop()

# Register
def availableSlot():
    window7 = tk.Toplevel()
    window7.iconbitmap(logo)
    window7.geometry("446x446")
    window7.title('Available Parking Slot')
    window7.config(background=pop_window_color_Menu_bar)

    window_background_material = PhotoImage(file=wall_now3)
    material_lable = Label(window7, image=window_background_material)
    material_lable.place(x=0, y=10, relwidth=1, relheight=1)

    # Window Heading
    credit_label = Label(window7, width=100, text="Booking", font=("'Helvetica 21"), background=heading, foreground=fg)
    credit_label.pack(pady=0)

    credit_label = Label(window7, width=100, text="Availability", font=("'Helvetica 16"), background=heading, foreground=fg)
    credit_label.pack(pady=6)

    # Username label    
    regno = Label(window7, text="Reg No: " ,font=(main_text, 12,), width = 10, bg=heading, fg="white" )
    regno.place(y=114,x=50)

    parkingblock = Label(window7, text="Parking Slot: " ,font=(main_text, 12,), width = 10, bg=heading, fg="white" )
    parkingblock.place(y=154,x=50)    

    price = Label(window7, text="Price ₹: " ,font=(main_text, 12,), width = 10, bg=heading, fg="white" )
    price.place(y=192,x=50)

    # inputs
    regnoInput = tk.Text(window7,bd=1,height=1, font=(main_text, 13,), width=15, bg=footer_label)
    regnoInput.place(y=115,x=210)

    parkingblockInput = tk.Text(window7,bd=1,height=1, font=(main_text, 13,), width=15, bg=footer_label)
    parkingblockInput.place(y=155,x=210)

    priceInput = tk.Text(window7,bd=1,height=1, font=(main_text, 13,), width=15, bg=footer_label)
    priceInput.place(y=193,x=210)

    register_btn = Button(window7, text="Order", width=10, height=1, command=window.destroy, font=(main_text, 12), bd=1, background="#851519", foreground="white")
    register_btn.place(x=235, y=240)

    window7.mainloop()


def developers(x):
    if x == 1:
        print(" Opening Website and instagram: https://pms.in & https://instagram.com/pms")
        website_url = "https://pms.in"
        webbrowser.open_new(website_url)

        # instagram
        time.sleep(2)
        website_url = "https://instagram.com/pmsw"
        webbrowser.open_new(website_url)
       
    elif x == 2:
        print(" ")
        linkedIn_url = "https://www.linkedin.com/in/pms/"
        webbrowser.open_new(linkedIn_url)

    elif x == 3:
        print(" ")
        github_url = "https://github.com/pms/"
        webbrowser.open_new(github_url)


def main_options():
    login_.place(x=70, y=120)
    register_.place(x=70, y=170)
    available_.place(x=70, y=220)
    more_opt.place(x=70, y=270)
    main_opt.place_forget()

    # hide more options
    Website.place_forget()
    linkedin.place_forget()
    github.place_forget()


def more_options():
    login_.place_forget()
    register_.place_forget()
    available_.place_forget()
    more_opt.place_forget()
    main_opt.place(x=70, y=270)

    # more options
    Website.place(x=70, y=120)
    linkedin.place(x=70, y=170)
    github.place(x=70, y=220)


# Heading
credit_label = Label(window, width=35, text="", font=("'Helvetica 18"), background=heading, foreground=fg)
credit_label.place(y=0,x=0)

credit_label = Label(window, width=35, text="", font=("'Helvetica 18"), background=fg, foreground=fg)
credit_label.place(y=0,x=496)

credit_label = Label(window, width=28, text="Parking Management System", font=("'Helvetica 22"), background=heading, foreground=fg)
credit_label.place(y=10,x=6)

# Buttons
login_ = Button(window, text="Login", width=18, height=1,command=lambda: login(), font=("'Helvetica 12"), background=footer_label, foreground=footer_fg)

register_ = Button(window, text="Register", width=18, height=1, command=lambda: register(), font=("'Helvetica 12"), background=footer_label, foreground=footer_fg)

available_ = Button(window, text="Available Parking Slot", width=18, height=1, command= lambda: availableSlot(), font=("'Helvetica 12"), background=footer_label, foreground=footer_fg)

more_opt = Button(window, text="Options", width=18, height=1, command=lambda: more_options(), font=("'Helvetica 12"), background=footer_label2, foreground=footer_fg)

main_opt = Button(window, text="Back", width=18, height=1, command=lambda: main_options(), font=("'Helvetica 12"), background=footer_label2, foreground=footer_fg)

Website = Button(window, text="Website", width=18, height=1, command=lambda: developers(1), font=("'Helvetica 12"), background=footer_label_social, foreground=fg)

linkedin = Button(window, text="LinkedIn", width=18, height=1, command=lambda: developers(2), font=("'Helvetica 12"), background=footer_label_social, foreground=fg)

github = Button(window, text="GitHub", width=18, height=1, command=lambda: developers(3), font=("'Helvetica 12"), background=footer_label_social, foreground=fg)

main_options()

exit = Button(window, text="Help", width=10, height=1, command=window.destroy, font=(main_text, 9), bd=0, background="white", foreground="red")
exit.place(x=830, y=6)

exit = Button(window, text="i", width=2, height=1, command=window.destroy, font=(main_text, 9), bd=0, background="white", foreground="red")
exit.place(x=900, y=6)

exit = Button(window, text="X", width=2, height=1, command=window.destroy, font=(main_text, 9), bd=0, background="white", foreground="red")
exit.place(x=930, y=6)

exit = Button(window, text="Developed by KUMAR GAURAV", width=24, height=1, command=window.destroy, font=(main_text, 8), bd=0, background="white", foreground=footer_fg)
exit.place(x=775, y=424)

window.mainloop()
# ------------------- Main Windows Starts Here --------------------------------------