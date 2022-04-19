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

    login_as_page('yaswanthkommineni1611@gmail.com',root,db)
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
        elif len(mobile) != 10:
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
        details = db.get_user_details(email)
        customer = User(email, details[0], details[1], details[2])
        customer_home_page(customer, root, db)

    def login_as_manager_clicked():

        details = db.get_user_details(email)
        manager = Manager(email, details[0], details[1], details[2], details[3])
        manager_home_page(manager, root, db)
    def login_as_delivery_person_clicked():
        details = db.get_user_details(email)
        customer = User(email, details[0], details[1], details[2], details[3])
        delivery_person_homepage(customer, root, db)

    login_customer_button = Button(root, text="Login as Customer", command=login_as_customer_clicked, font=("Ariel 15 bold"))
    login_customer_button.place(x=window_width // 8, y=1.5 * window_height // 10, height=window_height // 5,
                       width=3 * window_width // 4 - 10)

    login_manager_button = Button(root, text="Login as Manager", command=login_as_manager_clicked, font=("Ariel 15 bold"))
    login_manager_button.place(x=window_width // 8, y=4 * window_height // 10, height=window_height // 5,
                          width=3 * window_width // 4 - 10)

    login_delivery_person_button = Button(root, text="Login as Delivery Person", command=login_as_delivery_person_clicked, font=("Ariel 15 bold"))
    login_delivery_person_button.place(x=window_width // 8, y=6.5 * window_height // 10, height=window_height // 5,

                       width=3 * window_width // 4 - 10)
    root.mainloop()

def add_restaurant_page(manager, parent_window = None, db = None):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Register restaurant')

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

    cities = db.get_all_cities()

    frame = Frame(root, bg="white")

    city_clicked = StringVar()
    area_clicked = StringVar()

    city_clicked.set(cities[0])
    areas = db.get_areas_in_city(cities[0])
    area_clicked.set(areas[0])

    frame.place(x=window_width//15, y=(window_height//6), height = 540, width = 4*window_width//7)


    name_label = Label(frame, text="Restaurant name", font = ("Goudy old style",17,"bold"),fg="grey",bg="white")
    name_entry = Entry(frame,font=("times new roman",15),bg="lightgray")
    name_entry.focus()
    opening_label = Label(frame, text="Opening time", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    opening_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable = StringVar(root,"09:00"))
    closing_label = Label(frame, text="Closing time", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    closing_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable = StringVar(root,"22:30"))
    city_label = Label(frame, text="City", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    city_entry = OptionMenu(frame, city_clicked, *cities)
    area_label = Label(frame, text="Area", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    area_entry = OptionMenu(frame, area_clicked, *areas)
    address_label = Label(frame, text="Address", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    address_entry = Entry(frame, font=("times new roman", 15), bg="lightgray")
    phone_label = Label(frame, text="Phone", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    phone_entry = Entry(frame, font=("times new roman", 15), bg="lightgray")
    note_msg = "Note: Enter the time in HH:MM format. For example, 4 hours 20 minutes can be entered as 04:20."
    note_label = Label(frame, text = note_msg, font = ("Goudy old style", 12), fg = "grey", bg = "white")

    def check(event):
        nonlocal areas
        nonlocal area_entry
        nonlocal area_clicked
        areas = db.get_areas_in_city(city_clicked.get())
        if area_clicked.get() not in areas:
            area_clicked.set(areas[0])
        area_entry = OptionMenu(frame, area_clicked, *areas)
        area_entry.place(y=240, x=240, width=350, height=30)
        area_entry.bind('<Enter>', check)

    area_entry.bind('<Enter>', check)

    name_label.place(y = 60,x =  40)
    name_entry.place(y = 60,x = 240,width = 350, height = 30)
    opening_label.place(y = 120,x = 40)
    opening_entry.place(y = 120,x =  190,width = 150,height = 30)
    closing_label.place(y = 120,x =  360)
    closing_entry.place(y=120, x=510, width=150,height = 30)
    city_label.place(y=180, x=40)
    city_entry.place(y=180, x=240, width=350, height=30)
    area_label.place(y=240,x=40)
    area_entry.place(y=240,x=240,width=350,height=30)
    address_label.place(y=300, x=40)
    address_entry.place(y=300, x=240, width=350, height=30)
    phone_label.place(y=360, x=40)
    phone_entry.place(y=360, x=240, width=350, height=30)
    note_label.place(y = 480,x = 40)

    def register_clicked():
        open = opening_entry.get()
        close = closing_entry.get()
        phone = phone_entry.get()
        name = name_entry.get()
        address = address_entry.get()
        msg = ""
        if(len(open)!=5 or len(close)!=5 or open[2] != ':' or close[2] != ':'):
            msg = "Please enter a valid time"
        (open_hours,open_minutes,close_hours,close_minutes) = (None,None,None,None)
        if msg == "" and ((not is_numeric(open[0:2]) )or (not is_numeric(close[0:2])) or (not is_numeric(open[3:5])) or (not is_numeric(close[3:5]))):
            msg = "Please enter a valid time"
        if len(msg) == 0:
            (open_hours,open_minutes) = get_hours_minutes_from_time(open)
            (close_hours,close_minutes) = get_hours_minutes_from_time(close)
        if msg == "" and max(open_hours,close_hours) > 23:
            msg = "Please enter a valid time"
        if msg == "" and max(open_minutes, close_minutes) > 59:
            msg = "Please enter a valid time"
        if msg == "" and ((not is_numeric(phone)) or len(phone) != 10):
            msg = "Please enter a valid phone number"
        if msg == "" and len(name) < 4:
            msg = "Restaurant name must contain at least 4 characters"
        if msg == "" and len(address) < 10:
            msg = "Address field must contain at least 10 characters"

        if len(msg) != 0:
            showinfo(
                title = "Error",
                message = msg
            )
            return

        result = db.insert_restaurant(manager.email,name,open,close,address,area_clicked.get(),city_clicked.get(),phone)

        if result == 1:
            msg = "There exists a restaurant with the same name and in the same area."
        elif result == 2:
            msg = "The given phone number already exists."

        if len(msg) != 0:
            showinfo(
                title = "Error",
                message = msg
            )
            return

        msg = "Restaurant successfully added."
        showinfo(
            title = "Success",
            message = msg
        )
        manager_home_page(manager,root,db)

    def cancel_clicked():
        manager_home_page(manager, root, db)

    register_button = Button(frame, text="Register", command=register_clicked, font = ("Ariel 15 bold"))
    register_button.place(x = 40,y = 420,height = 40,width = 250)

    cancel_button = Button(frame, text="Cancel", command=cancel_clicked, font = ("Ariel 15 bold"))
    cancel_button.place(x = 340,y = 420,height = 40,width = 250)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root,db), font=("Ariel 15 bold"))
    logout_button.place(x=24*window_width // 30, y=window_height // 20, height=window_height // 15,
                          width=1 * window_width // 5 - 35)

    root.mainloop()

def manager_home_page(manager, parent_window = None, db = None):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Manage restaurant')

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
    frame = Frame(root, bg="white")
    frame.place(x=window_width // 15, y=(window_height // 4), height=window_height // 3,
                      width=4 * window_width // 9)

    def add_restaurant_clicked():
        add_restaurant_page(manager,root,db)


    if details == None:
        label = Label(frame, text="You are not a manager of any restaurant", font=("Goudy old style", 20, "bold"), fg="grey", bg="white")
        label.place(y=2 * window_height // 20, x=window_width // 30)
        add_restaurant_button = Button(frame, text="Add a restaurant", command=add_restaurant_clicked, font = ("Ariel 15 bold"))
        add_restaurant_button.place(x = window_width//30,y = 3.5*window_height//20,height = window_height//15,width = 2*window_width//5-35)
    else:

        restaurant = Restaurant(details[0],details[1],details[2],details[3],details[4],details[5],details[6],details[7],convert_string_to_bool(details[8]))
        email_label = Label(frame, text="Restaurant name: {0}".format(details[2]), font=("Goudy old style", 20, "bold"),
                            fg="grey", bg="white")
        email_label.place(y=2 * window_height // 20, x=window_width // 30)
        manage_restaurant_button = Button(frame, text="Manage", command=lambda: manage_restaurant_page(restaurant,root,db),
                                       font=("Ariel 15 bold"))
        manage_restaurant_button.place(x=window_width // 30, y=3.5 * window_height // 20, height=window_height // 15,
                                    width=2 * window_width // 5 - 35)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24 * window_width // 30, y=window_height // 20, height=window_height // 15,
                        width=1 * window_width // 5 - 35)

    root.mainloop()

def manage_restaurant_page(restaurant,parent_window = None,db = None, page_number = 0):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Manage restaurant')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6*screen_width)//7
    window_height = (6*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)

    data = db.get_food_items(restaurant.id)
    restaurant.foodItems = []

    for x in data:
        new_food_item = FoodItem(x[0], x[1], x[2], x[3], x[5], convert_string_to_bool(x[4]))
        restaurant.addFoodItem(new_food_item)

    background_image = ImageTk.PhotoImage(
        Image.open('Images/manager_home_page_background.jpg').resize((window_width + 100, window_height),
                                                                     Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    frames = []

    num_pages = (len(restaurant.foodItems)+5)//6

    for j in range(6*page_number, min(6*page_number+6, len(restaurant.foodItems))):
        i = j-(6*page_number)
        xval = 30 + (i % 3)*350
        yval = 50 + (i // 3)*320
        new_frame = Frame(root, bg="white")
        new_frame.place(x=xval, y=yval, height=270, width=300)

        entry_frame = Frame(new_frame, bg="white")
        entry_frame.place(x=0, y=0, height=150, width=300)

        name_label = Label(entry_frame, text="Name: ", font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        name_value = Text(entry_frame, font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        name_value.insert('1.0',restaurant.foodItems[j].name)
        name_value['state'] = 'disabled'
        availability_label = Label(entry_frame, text="Availability: ", font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        availability_value = Text(entry_frame, font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        availability_value.insert('1.0', convert_availability_to_string(restaurant.foodItems[j].availability))
        availability_value['state'] = 'disabled'
        price_label = Label(entry_frame, text="Price: ", font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        price_value = Text(entry_frame, font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        price_value.insert('1.0', str(restaurant.foodItems[j].price))
        price_value['state'] = 'disabled'
        name_label.place(x=10, y=30)
        name_value.place(x=110, y=30, width=180)
        availability_label.place(x=10, y=70)
        availability_value.place(x=110, y=70, width=180)
        price_label.place(x=10, y=110)
        price_value.place(x=110, y=110, width=180)

        def info_clicked():
            x = root.winfo_pointerx()
            y = root.winfo_pointery()
            ind = 6*page_number
            if y > 500:
                ind += 3
            if x > 730:
                ind += 2
            elif x > 380:
                ind += 1
            showinfo(
                title='Information',
                message=restaurant.foodItems[ind].description
            )

        def edit_clicked():
            x = root.winfo_pointerx()
            y = root.winfo_pointery()
            ind = 6*page_number
            if y > 500:
                ind += 3
            if x > 730:
                ind += 2
            elif x > 380:
                ind += 1
            manage_food_item(restaurant, restaurant.foodItems[ind], root, db)

        edit_button = Button(new_frame, text="Edit", command=edit_clicked, font=("Ariel 15 bold"))
        edit_button.place(x=20, y=210, height=40, width=170)

        info_button = Button(new_frame, text="More info", command=info_clicked, font=("Ariel 15 bold"))
        info_button.place(x=20, y=160, height=40, width=170)

        frames.append(new_frame)

    def page_clicked():
        x = root.winfo_pointerx()
        ind = ((x-window_width//2+100)+70)//60
        ind -= 3
        print(ind)
        manage_restaurant_page(restaurant, root, db, ind)

    for i in range(num_pages):
        color = "white"
        if i == page_number:
            color = "grey"
        button = Button(root, text=str(i+1), command=page_clicked, font=("Ariel 15 bold"), bg = color)
        button.place(x=window_width//2+i*60-100, y=window_height-70, height=30, width=50)

    add_food_item_button = Button(root, text="Add Food Item", command=lambda: add_food_item_page(restaurant,root, db), font=("Ariel 15 bold"))
    add_food_item_button.place(x=24 * window_width // 30, y=3*window_height // 20, height=window_height // 15,
                        width=1*window_width // 5 - 35)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24 * window_width // 30, y=window_height // 20, height=window_height // 15,
                        width=1*window_width // 5 - 35)

    root.mainloop()

def manage_food_item(restaurant, fooditem, parent_window, db):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Manage food item')

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

    frame = Frame(root, bg="white")

    frame.place(x=window_width//15, y=(window_height//6), height=540, width=4*window_width//7)

    availability_clicked = StringVar()
    availability_clicked.set(convert_availability_to_string(fooditem.availability))

    options = ['Available', 'Not available']

    name_label = Label(frame, text="Name", font=("Goudy old style",17,"bold"),fg="grey",bg="white")
    name_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable = StringVar(root,fooditem.name))
    name_entry.focus()
    description_label = Label(frame, text="Address", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    description_entry = Text(frame, font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
    description_entry.insert('1.0', fooditem.description)
    price_label = Label(frame, text="Name", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    price_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable = StringVar(root,str(fooditem.price)))
    availability_label = Label(frame, text="Availability", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    availability_entry = OptionMenu(frame, availability_clicked, *options)

    def ok_clicked():
        name = name_entry.get()
        price = price_entry.get()
        msg = ""
        if len(name) < 4:
            msg = "Food item name should contain at least 4 characters"
        if msg == "" and (not is_double(price)):
            msg = "Enter a valid price"

        if msg != "":
            showinfo(
                title='Error',
                message=msg
            )
            return
        availability = ""
        if availability_clicked.get() == "Available":
            availability = 'True'
        else:
            availability = 'False'
        db.edit_food_item(fooditem.food_id, name, description_entry.get('1.0', 'end'), price, availability)
        showinfo(
            title='Success',
            message='Food item got successfully updated'
        )
        manage_restaurant_page(restaurant, root, db)

    ok_button = Button(frame, text="OK", command=ok_clicked, font=("Ariel 15 bold"))
    ok_button.place(x=40, y=380, height=40, width=250)

    def cancel_clicked():
        manage_restaurant_page(restaurant, root, db)

    def delete_clicekd():
        a = 1

    name_label.place(y=60, x=40)
    name_entry.place(y=60, x=240, width=350, height=30)
    description_label.place(y=120, x=40)
    description_entry.place(y=120, x=240, width=450, height=90)
    price_label.place(y=240, x=40)
    price_entry.place(y=240, x=240, width=350, height=30)
    availability_label.place(y=300, x=40)
    availability_entry.place(y=300, x=240, width = 350, height = 30)

    cancel_button = Button(frame, text="Cancel", command=cancel_clicked, font = ("Ariel 15 bold"))
    cancel_button.place(x=340, y=380, height=40, width=250)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24*window_width // 30, y=window_height // 20, height=window_height // 15, width=1 * window_width // 5 - 35)

    delete_button = Button(root, text="Delete this item", command=lambda: delete_clicked, font=("Ariel 15 bold"))
    delete_button.place(x=100, y=450, height=40, width=350)

    root.mainloop()

def add_food_item_page(restaurant, parent_window = None, db = None):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Add Food Item')

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

    frame = Frame(root, bg="white")

    frame.place(x=window_width // 15, y=(window_height // 6), height=360, width=4 * window_width // 7)

    name_label = Label(frame, text="Food name", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    name_entry = Entry(frame, font=("times new roman", 15), bg="lightgray")
    name_entry.focus()
    description_label = Label(frame, text="Description", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    description_entry = Text(frame, font=("times new roman", 14), bg="lightgray")
    price_label = Label(frame, text="Price", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    price_entry = Entry(frame, font=("times new roman", 15), bg="lightgray")

    def add_clicked():
        name = name_entry.get()
        price = price_entry.get()
        msg = ""
        if len(name) < 4:
            msg = "Food item name should contain at least 4 characters"
        if msg == "" and (not is_double(price)):
            msg = "Enter a valid price"

        if msg != "":
            showinfo(
                title='Error',
                message=msg
            )
            return
        db.insert_food_item(restaurant.id, name, description_entry.get('1.0', 'end'), price)
        showinfo(
            title='Success',
            message='Food item successfully added to the restaurant menu'
        )
        manage_restaurant_page(restaurant, root, db)

    add_button = Button(frame, text="Add Food Item", command=add_clicked, font=("Ariel 15 bold"))
    add_button.place(x=40, y=280, height=40, width=250)

    cancel_button = Button(frame, text="Cancel", command=lambda: manage_restaurant_page(restaurant,root,db), font=("Ariel 15 bold"))
    cancel_button.place(x=340, y=280, height=40, width=250)

    name_label.place(y=60, x=40)
    name_entry.place(y=60, x=240, width=350, height=30)
    description_label.place(y=120, x=40)
    description_entry.place(y=120, x=240, width=450, height=70)
    price_label.place(y=220, x=40)
    price_entry.place(y=220, x=240, width=350, height=30)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24 * window_width // 30, y=window_height // 20, height=window_height // 15,
                        width=1 * window_width // 5 - 35)

    root.mainloop()


def add_address(user, parent_window=None, db=None):
    if db == None:
        db = DataBase()
    if (parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Add your address')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (2 * screen_width) // 3
    window_height = (2 * screen_height) // 3

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/address.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    cities = db.get_all_cities()

    frame = Frame(root, bg="white")

    city_clicked = StringVar()
    area_clicked = StringVar()

    city_clicked.set(cities[0])
    areas = db.get_areas_in_city(cities[0])
    area_clicked.set(areas[0])

    frame.place(x=window_width // 15, y=(window_height // 6), height=350, width=4 * window_width // 7)

    city_label = Label(frame, text="City", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    city_entry = OptionMenu(frame, city_clicked, *cities)
    area_label = Label(frame, text="Area", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    area_entry = OptionMenu(frame, area_clicked, *areas)
    address_label = Label(frame, text="Address", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    address_entry = Text(frame, font=("times new roman", 15), bg="lightgray")

    def check(event):
        nonlocal areas
        nonlocal area_entry
        nonlocal area_clicked
        areas = db.get_areas_in_city(city_clicked.get())
        if area_clicked.get() not in areas:
            area_clicked.set(areas[0])
        area_entry = OptionMenu(frame, area_clicked, *areas)
        area_entry.place(y=120, x=140, width=250, height=30)
        area_entry.bind('<Enter>', check)

    area_entry.bind('<Enter>', check)

    city_label.place(y=50, x=40)
    city_entry.place(y=50, x=140, width=250, height=30)
    area_label.place(y=120, x=40)
    area_entry.place(y=120, x=140, width=250, height=30)
    address_label.place(y=190, x=40)
    address_entry.place(y=190, x=140, width=250, height=50)

    def register_clicked():
        address = address_entry.get('1.0', 'end')
        msg = ""
        if msg == "" and len(address) < 10:
            msg = "Address field must contain at least 10 characters"

        if len(msg) != 0:
            showinfo(
                title="Error",
                message=msg
            )
            return

        result = db.update_user_area(user.email, address, area_clicked.get(), city_clicked.get())

        if result == 1:
            msg = "Profile updated succesfully"

        if len(msg) != 0:
            showinfo(
                title="Success",
                message=msg
            )
            customer_home_page(user, root, db)
            return

        msg = "There is some error while updating address."
        showinfo(
            title="Error",
            message=msg
        )

    register_button = Button(frame, text="Update address", command=register_clicked, font=("Ariel 12 bold"))
    register_button.place(x=150, y=260, height=40, width=150)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=700, y=20)

    root.mainloop()


def edit_profile(user, parent_window=None, db=None):
    if db == None:
        db = DataBase()
    if (parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Your profile')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (2 * screen_width) // 3
    window_height = (3 * screen_height) // 4

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/profile.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    cities = db.get_all_cities()

    frame = Frame(root, bg="white")

    city_clicked = StringVar(value="Select your city")
    area_clicked = StringVar(value="Select your area")

    # city_clicked.set(cities[0])
    areas = db.get_areas_in_city(cities[0])
    # area_clicked.set(areas[0])

    frame.place(x=window_width // 12, y=(window_height // 15), height=450, width=4 * window_width // 7)

    name_label = Label(frame, text="Name", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    name = StringVar(root, value=user.name)
    name_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable=name)
    mobile_label = Label(frame, text="Mobile No", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    mobile = StringVar(root, value=user.contact)
    mobile_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable=mobile)
    city_label = Label(frame, text="City", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    city_entry = OptionMenu(frame, city_clicked, *cities)
    area_label = Label(frame, text="Area", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    area_entry = OptionMenu(frame, area_clicked, *areas)
    address_label = Label(frame, text="Address", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    address_entry = Text(frame, font=("times new roman", 15), bg="lightgray")
    address_entry.insert(END, user.address)

    def check(event):
        nonlocal areas
        nonlocal area_entry
        nonlocal area_clicked
        areas = db.get_areas_in_city(city_clicked.get())
        if area_clicked.get() not in areas:
            area_clicked.set(areas[0])
        area_entry = OptionMenu(frame, area_clicked, *areas)
        area_entry.place(y=260, x=150, width=250, height=30)
        area_entry.bind('<Enter>', check)

    area_entry.bind('<Enter>', check)

    name_label.place(y=50, x=40)
    name_entry.place(y=50, x=150, width=250, height=30)
    mobile_label.place(y=120, x=40)
    mobile_entry.place(y=120, x=150, width=250, height=30)
    city_label.place(y=190, x=40)
    city_entry.place(y=190, x=150, width=250, height=30)
    area_label.place(y=260, x=40)
    area_entry.place(y=260, x=150, width=250, height=30)
    address_label.place(y=330, x=40)
    address_entry.place(y=330, x=150, width=250, height=50)

    def update_clicked():
        address = address_entry.get('1.0', 'end')
        msg = ""

        if city_clicked.get() == "Select your city":
            msg = "Pls select your city and area"

        if msg == "" and len(address) < 10:
            msg = "Address field must contain at least 10 characters"

        if len(msg) != 0:
            showinfo(
                title="Error",
                message=msg
            )
            return

        result = db.update_user_profile(user.email, name_entry.get(), mobile_entry.get(), address, area_clicked.get(),
                                        city_clicked.get())

        if result == 1:
            msg = "Area updated succesfully"

        if len(msg) != 0:
            showinfo(
                title="Success",
                message=msg
            )
            customer_home_page(user, root, db)
            return

        msg = "There is some error while updating address."
        showinfo(
            title="Error",
            message=msg
        )

    register_button = Button(frame, text="Update profile", command=update_clicked, font=("Ariel 12 bold"))
    register_button.place(x=150, y=400, height=40, width=150)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=700, y=20)

    root.mainloop()


def customer_home_page(user, parent_window=None, db=None):
    if db == None:
        db = DataBase()

    details = db.get_user_details(user.email)
    user = User(user.email, details[0], details[1], details[2], details[3])
    areaid = user.area_id
    if (parent_window != None):
        parent_window.destroy()
    root = tk.Tk()

    if (areaid == None):
        add_address(user, root, db)

    root.title("Order your food")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6 * screen_width) // 7
    window_height = (6 * screen_height) // 7

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/cus.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    avbl_restaurants = db.restaurants_by_city(areaid)
    print(avbl_restaurants)

    profile_button = Button(root, text="Edit profile", command=lambda: edit_profile(user, root, db),
                            font=("Ariel 15 bold"))
    profile_button.place(x=window_width // 30, y=window_height // 20, height=window_height // 15,
                         width=1 * window_width // 5 - 35)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24 * window_width // 30, y=window_height // 20, height=window_height // 15,
                        width=1 * window_width // 5 - 35)

    root.mainloop()


def delivery_person_homepage(user, parent_window=None, db=None):
    if db == None:
        db = DataBase()
    if (parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Deliver an order')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6 * screen_width) // 7
    window_height = (6 * screen_height) // 7

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/del.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24 * window_width // 30, y=window_height // 20, height=window_height // 15,
                        width=1 * window_width // 5 - 35)

    root.mainloop()