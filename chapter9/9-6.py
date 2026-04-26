class Restaurant():
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
    
class IceCreamstand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'coffee', 'caramel']
    def show_flavors(self):
        print("The available flavors are:")
        for flavor in self.flavors:
            print(flavor)

ice_cream_stand = IceCreamstand("Jams's Ice Cream Stand", "ice cream")
ice_cream_stand.show_flavors()
ice_cream_stand.set_number_served(100)
ice_cream_stand.increment_number_served(50)
print("Number of customers served: " + str(ice_cream_stand.number_served))