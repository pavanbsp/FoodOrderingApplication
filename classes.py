class FoodItem:
    def __init__(self, food_id, restaurant_id, name, description, price, availability=False):
        self.food_id = food_id
        self.restaurant_id = restaurant_id
        self.name = name
        self.description = description
        self.price = price
        self.availability = False
    def updateFoodItem(self, price):
        self.price = price
    def switchAvailability(self):
        self.availability = not self.availability

class User:
    def __init__(self, email, name, contact, area_id = None):
        self.email = email
        self.name = name
        self.contact = contact
        self.area_id = area_id

class Manager(User):
    def __init__(self, email, name, contact, area_id = None, restaurant = None):
        User.__init__(self, email, name, contact, area_id)
        self.restaurant = restaurant
    def add_restaurant(self, restaurant):
        if(self.restaurant == None):
            self.restaurant = restaurant
            return True
        else:
            return False
    def removeRestaurant(self):
        self.restaurant = None
    #def updateRestaurantDetails(self):

class Restaurant:
    def __init__(self, id, manager_email, name, open_time, close_time, address, area_id, phone, flag = False):
        self.name = name
        self.id = id
        self.manager_email = manager_email
        self.area_id = area_id
        self.close_time = close_time
        self.open_time = open_time
        self.phone = phone
        self.address = address
        self.foodItems = []
        self.orders = []
        self.flag = flag

    def toggleFlag(self):
        if self.flag == False:
            self.flag = True
        else:
            self.flag = False

    def addFoodItem(self, foodItem):
        self.foodItems.append(foodItem)

    #def getStatus(self):
        #return self.status
    #def displayFoodItems(self):