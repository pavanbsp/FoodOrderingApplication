import MySQLdb as mdb
from mysql.connector import Error
import numpy as np

class DataBase:
    def __init__(self):
        try:
            self.database = mdb.connect('localhost', 'root', 'Ypk@1050', 'temp')

            cursor = self.database.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                                email varchar(50) PRIMARY KEY,
                                                password varchar(40),
                                                name varchar(100),
                                                contact varchar(10),
                                                address varchar(200),
                                                area_id varchar(10))''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS restaurants (
                                                restaurant_id varchar(50) PRIMARY KEY,
                                                manager_email varchar(50),
                                                name varchar(100),
                                                opening_time time,
                                                closing_time time,
                                                status varchar(4),
                                                address varchar(200),
                                                area_id varchar(10),
                                                phone varchar(10))''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS food_items(
                                                food_id varchar(50) PRIMARY KEY,
                                                restaurant_id varchar(50),
                                                name varchar(50),
                                                description varchar(300),
                                                availability varchar(4),
                                                price double
                                                )''')


            cursor.execute('''CREATE TABLE IF NOT EXISTS areas(
                                                area_id varchar(10) PRIMARY KEY,
                                                name varchar(100),
                                                city varchar(100))''')

            cursor = self.database.cursor()
            cursor.execute("select * from areas")
            data = cursor.fetchall()

            if len(data) == 0:
                areas = dict()
                areas['Hyderabad'] = ['Uppal', 'Madhapur', 'Banjara Hills', 'Ameerpet'
                    , 'Begumpet', 'Somajiguda', 'Gachibowli', 'Manikonda',
                                      'Miyapur', 'Kondapur']
                areas['Guntur'] = ['Lakshmipuram', 'Brodipet', 'Arundelpet', 'Chandramouli Nagar',
                                   'Brindavan Gardens', 'Koritepadu', 'Pattabhipuram', 'Old town',
                                   'Vidya Nagar', 'Nagaraly']


                for x in areas.keys():
                    for y in areas[x]:
                        area_id = ""
                        for i in range(5):
                            area_id += (chr(np.random.randint(ord('0'),ord('9')+1)))
                        cursor.execute("INSERT into areas (area_id,name,city) values ('{0}','{1}','{2}')".format(area_id,y,x))
                        self.database.commit()



        except Exception as error:
            print(error)

    
    def user_login(self, email, password):
        cursor = self.database.cursor()
        cursor.execute("select * from users where email='"+email+"' and password='"+password+"'")
        data = cursor.fetchall()
        cursor.close()
        if len(data) > 0:
            return True
        else:
            return False

    def insert_user(self, name, email, password, contact):
        cursor = self.database.cursor()
        cursor.execute("select * from users where email = '{0}'".format(email))
        data = cursor.fetchall()
        if len(data) != 0:
            return False
        cursor.execute("select * from users where contact = '{0}'".format(contact))
        data = cursor.fetchall()
        val = (email, password, name, contact)
        if len(data) != 0:
            return False
        cursor.execute("INSERT into users (email,password,name,contact) values (%s,%s,%s,%s)", val)
        self.database.commit()
        cursor.close()
        return True

    def get_user_details(self, email):
        cursor = self.database.cursor()
        cursor.execute("select name, contact, address, area_id from users where email = '{0}'".format(email))
        data = cursor.fetchall()
        if len(data) == 0:
            return False
        else:
            return data[0]

    def get_restaurant_details_managed_by(self, email):
        cursor = self.database.cursor()
        cursor.execute("select * from restaurants where manager_email = '{0}'".format(email))
        data = cursor.fetchall()
        if len(data) == 0:
            return None
        else:
            return data[0]

    def get_all_cities(self):
        cursor = self.database.cursor()
        cursor.execute("select distinct city from areas")
        data = cursor.fetchall()
        result = []
        for x in data:
            result.append(x[0])
        return result

