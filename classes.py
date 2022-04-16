class FoodItem:
    def __init__(self, foodId, foodName, price):
        self.foodId = foodId
        self.foodName = foodName
        self.price = price
        self.availability = False
    def updateFoodItem(self, price):
        self.price = price
    def switchAvailability(self):
        self.availability = not self.availability

class User:
    def __init__(self, email, name, contact, area = None, area_id = None):
        self.email = email
        self.name = name
        self.contact = contact
        self.area = area
        self.area_id = area_id

class Manager(User):
    def __init__(self, email, name, contact, area = None, area_id = None, restaurant = None):
        User.__init__(self, email, name, contact, area, area_id)
        self.restaurant = restaurant
    def add_restaurant(self, restaurant):
        if(self.restaurant == None):
            self.restaurant = restaurant
            return True
        else:
            return False
    def addFoodItem(self, foodId, foodName, price):
        if(self.restaurant == None):
            return False
        self.restaurant.foodItems.append(FoodItem(foodId, foodName, price))
        return True
    def removeRestaurant(self):
        self.restaurant = None
    def updateRestaurantStatus(self, status):
        self.restaurant.status = status
    #def updateRestaurantDetails(self):

class Restaurant:
    def __init__(self, name, id, manager, area, address, phoneNumber):
        self.name = name
        self.id = id
        self.manager = manager
        self.area = area
        self.address = address
        self.phoneNumber = phoneNumber
        self.foodItems = []
        self.orders = []
        self.status = False
    def getStatus(self):
        return self.status
    #def displayFoodItems(self):