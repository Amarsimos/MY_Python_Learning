class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("The name of the restaurant is " + self.name)
    def open_restaurant(self):
        print("The restaurant is open.")

my_restaurant = Restaurant("Zhangwangao's Restaurant", "Chinese")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

jams_restaurant = Restaurant("Jams' Restaurant", "American")
jams_restaurant.describe_restaurant()
jams_restaurant.open_restaurant()

muindi_restaurant = Restaurant("Muindi's Restaurant", "Thai")
muindi_restaurant.describe_restaurant()
muindi_restaurant.open_restaurant()