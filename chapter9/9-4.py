class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("The name of the restaurant is " + self.name)
    def open_restaurant(self):
        print("The restaurant is open.")
    def set_number_served(self,number_served):
        if number_served < self.number_served:
            print("Invalid input.")
        else:
            self.number_served = number_served
    def increment_number_served(self, number):
        if number < 0:
            print("Invalid input.")
        else:
            self.number_served += number
    
one_restaurant = Restaurant("One", "Chinese")
print(one_restaurant.name + " have served " + str(one_restaurant.number_served) + " people.")
one_restaurant.set_number_served(100)
print(one_restaurant.name + " have served " + str(one_restaurant.number_served) + " people.")
ok = input("Press any key to continue...")

one_restaurant.increment_number_served(50)
print(one_restaurant.name + " have served " + str(one_restaurant.number_served) + " people.")