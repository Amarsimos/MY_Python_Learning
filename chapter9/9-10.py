import Restaurant as r

my_restaurant = r.Restaurant("Jams's Ice Cream Stand", "ice cream")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant() 
my_restaurant.set_number_served(100)
my_restaurant.increment_number_served(50)
print("Number of customers served: " + str(my_restaurant.number_served))