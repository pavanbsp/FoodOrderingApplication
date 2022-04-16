import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from MySql_queries import DataBase
from tkinter.messagebox import showinfo
from common_functions import *
from classes import *

def login_page(parent_window = None, db = None):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Login page')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6*screen_width)//7
    window_height = (6*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    background_image = ImageTk.PhotoImage(Image.open('Images/login-background.jpeg').resize((window_width+100,window_height),Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)
    root.resizable(False,False)

    def login_clicked(email, password):
        if db.user_login(email, password):
            login_as_page(email, root, db)

        else:
            showinfo(
                title = 'Error',
                message = 'Email and Password does not match'
            )

    def register_clicked():
        register_page(root, db)

    login_frame = Frame(root, bg="white")
    login_frame.place(x=window_width//15, y=(window_height//4), height = window_height//2, width = 3*window_width//7)

    email_label = Label(login_frame, text="Email", font = ("Goudy old style",17,"bold"),fg="grey",bg="white")
    email_entry = Entry(login_frame,font=("times new roman",15),bg="lightgray")
    email_entry.focus()
    pass_label = Label(login_frame, text="Password", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    pass_entry = Entry(login_frame, font=("times new roman", 15), bg="lightgray",show="*")
    email_label.place(y = 2*window_height//20,x =  window_width//30)
    email_entry.place(y = 2*window_height//20,x = 2.2*window_width//20,width = 2*window_width//5-130)
    pass_label.place(y = 3.5*window_height//20,x =  window_width//30)
    pass_entry.place(y = 3.5*window_height//20,x =  2.2*window_width//20,width = 2*window_width//5-130)

    login_button = Button(login_frame, text="Login", command=lambda:login_clicked(email_entry.get(), pass_entry.get()), font = ("Ariel 15 bold"))
    login_button.place(x = window_width//30,y = 5*window_height//20,height = window_height//15,width = 2*window_width//5-35)

    register_button = Button(login_frame, text="Register", command=register_clicked, font = ("Ariel 15 bold"))
    register_button.place(x = window_width//30,y = 7*window_height//20,height = window_height//15,width = 2*window_width//5-35)
    login_as_page('srilekhasomanchi@gmail.com', root)
    root.mainloop()

def register_page(parent_window = None, db = None):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Register page')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6*screen_width)//7
    window_height = (6*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/register-background.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    register_frame = Frame(root, bg="white")
    register_frame.place(x=window_width // 30, y=(window_height // 4), height=3*window_height //5,
                      width=4 * window_width // 9)

    name_label = Label(register_frame, text="Name", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    name_entry = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
    name_entry.focus()
    mobile_label = Label(register_frame, text="Mobile No.", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    mobile_entry = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
    email_label = Label(register_frame, text="Email", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    email_entry = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
    pass_label = Label(register_frame, text="Password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    pass_entry = Entry(register_frame, font=("times new roman", 15), bg="lightgray", show="*")
    name_label.place(y=2 * window_height // 20, x=window_width // 30)
    name_entry.place(y=2 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    mobile_label.place(y=3.5 * window_height // 20, x=window_width // 30)
    mobile_entry.place(y=3.5 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    email_label.place(y=5 * window_height // 20, x=window_width // 30)
    email_entry.place(y=5 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    pass_label.place(y=6.5 * window_height // 20, x=window_width // 30)
    pass_entry.place(y=6.5 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)

    def register_clicked():
        name = name_entry.get()
        email = email_entry.get()
        password = pass_entry.get()
        mobile = mobile_entry.get()
        msg = ''
        if not check_length_less_than(name,100):
            msg = 'Name is too long'
        elif not is_numeric(mobile):
            msg = 'Enter a valid mobile number'
        elif not check_length_less_than(mobile,10):
            msg = 'Enter a valid mobile number'
        if len(msg) != 0:
            showinfo(
                title='Error',
                message=msg
            )
            return
        if not db.insert_user(name_entry.get(), email_entry.get(), pass_entry.get(), mobile_entry.get()):
            showinfo(
                title='Error',
                message='Email or mobile number already exists'
            )
            return
        showinfo(
            title='Success',
            message='Successfully registered'
        )
        login_page(root, db)


    def login_clicked():
        login_page(root, db)

    login_button = Button(register_frame, text="Register", command=register_clicked, font=("Ariel 15 bold"))
    login_button.place(x=window_width // 30, y=8 * window_height // 20, height=window_height // 15,
                       width=2 * window_width // 5 - 35)

    register_button = Button(register_frame, text="Already have an account?", command=login_clicked, font=("Ariel 15 bold"))
    register_button.place(x=window_width // 30, y=9.7 * window_height // 20, height=window_height // 15,
                          width=2 * window_width // 5 - 35)

    root.mainloop()

def login_as_page(email, parent_window = None,db = None):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Login page')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (1*screen_width)//3
    window_height = (1*screen_height)//3

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False,False)

    def login_as_customer_clicked():
        a = 1
    def login_as_manager_clicked():

        details = db.get_user_details(email)
        manager = Manager(email, details[0], details[1], details[2], details[3])
        manager_home_page(manager, root, db)
    def login_as_delivery_person_clicked():
        a = 1

    login_customer_button = Button(root, text="Login as Customer", command=login_as_customer_clicked, font=("Ariel 15 bold"))
    login_customer_button.place(x=window_width // 8, y=1.5 * window_height // 10, height=window_height // 5,
                       width=3 * window_width // 4 - 10)

    login_manager_button = Button(root, text="Login as Manager", command=login_as_manager_clicked, font=("Ariel 15 bold"))
    login_manager_button.place(x=window_width // 8, y=4 * window_height // 10, height=window_height // 5,
                          width=3 * window_width // 4 - 10)

    login_delivery_person_button = Button(root, text="Login as Delivery Person", command=login_as_delivery_person_clicked, font=("Ariel 15 bold"))
    login_delivery_person_button.place(x=window_width // 8, y=6.5 * window_height // 10, height=window_height // 5,

                       width=3 * window_width // 4 - 10)

def manager_home_page(manager, parent_window = None, db = None):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Manager home page')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6*screen_width)//7
    window_height = (6*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/manager_home_page_background.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)
    details = db.get_restaurant_details_managed_by(manager.email)
    login_frame = Frame(root, bg="white")
    login_frame.place(x=window_width // 15, y=(window_height // 4), height=window_height // 2,
                      width=3 * window_width // 7)
    if details == None:
        email_label = Label(login_frame, text="You are not a manager of any restaurant. You can choose the below option to ", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    #else:


#def customer_home_page():
