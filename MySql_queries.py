import MySQLdb as mdb
#from mysql.connector import Error
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
                                                opening_time varchar(5),
                                                closing_time varchar(5),
                                                address varchar(200),
                                                area_id varchar(10),
                                                phone varchar(10),
                                                flag varchar(5))''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS food_items(
                                                food_id varchar(50) PRIMARY KEY,
                                                restaurant_id varchar(50),
                                                name varchar(50),
                                                description varchar(300),
                                                availability varchar(5),
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

    def get_areas_in_city(self,city):
        cursor = self.database.cursor()
        cursor.execute("select name from areas where city = '{0}'".format(city))
        data = cursor.fetchall()
        result = []
        for x in data:
            result.append(x[0])
        return result

    def insert_restaurant(self,manager_email,name,opening_time,closing_time,address,area,city,phone):
        cursor = self.database.cursor()
        id = ""
        for i in range(10):
            id += (chr(np.random.randint(ord('0'), ord('9') + 1)))
        cursor.execute("select area_id from areas where city = '{0}' and name = '{1}'".format(city,area))
        data = cursor.fetchall()
        area_id = data[0][0]
        cursor.execute("select * from restaurants where name = '{0}' and area_id = '{1}'".format(name,area_id))
        data = cursor.fetchall()
        if len(data) > 0:
            return 1
        cursor.execute("select * from restaurants where phone = '{0}'".format(phone))
        data = cursor.fetchall()
        if len(data) > 0:
            return 2

        cursor.execute("INSERT into restaurants (restaurant_id,manager_email,name,opening_time,closing_time,address,area_id,phone,flag) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','False')".format(id,manager_email,name,opening_time,closing_time,address,area_id,phone))
        self.database.commit()

    def update_user_area(self, email, address, area, city):

        cursor = self.database.cursor()

        cursor.execute("select area_id from areas where city = '{0}' and name = '{1}'".format(city, area))

        data = cursor.fetchall()

        area_id = data[0][0]

        print(area_id)

        print(email, address, area, city)

        cursor.execute(
            "update users set address = '" + address + "', area_id = '" + area_id + "' where email = '" + email + "'")

        self.database.commit()

        cursor.close()

        return 1

    def insert_food_item(self,restaurant_id,name,description,price):
        cursor = self.database.cursor()
        id = ""
        for i in range(10):
            id += (chr(np.random.randint(ord('0'), ord('9') + 1)))
        cursor.execute("INSERT into food_items (food_id, restaurant_id, name, description, availability, price) values ('{0}','{1}','{2}','{3}','False',{4})".format(id, restaurant_id, name, description, price))
        self.database.commit()

    def get_food_items(self, restaurant_id):
        cursor = self.database.cursor()
        cursor.execute("select * from food_items where restaurant_id = '{0}'".format(restaurant_id))
        data = cursor.fetchall()
        return data

    def switch_availability(self, food_id, value):
        cursor = self.database.cursor()
        cursor.execute("UPDATE food_items SET availability = '{0}' where food_id = '{1}'".format(value, food_id))
        self.database.commit()

    def edit_food_item(self, id, name, description, price):
        cursor = self.database.cursor()
        cursor.execute("UPDATE food_items SET name = '{0}', description = '{1}', price = {2} where food_id = '{3}'".format(name, description, price, id))
        self.database.commit()

