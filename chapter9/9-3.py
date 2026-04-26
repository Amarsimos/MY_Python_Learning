class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def greets_user(self):
        print("Hello", self.first_name, self.last_name, "!")
    def describe(self):
        print("I am", self.age, "years old and my name is", self.first_name, self.last_name)

user1 = User("Amarsimos", "Gen", 25)
user1.greets_user()
user1.describe()