class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("Woof!")
    def sit(self):
        print(self.name + " is now sitting.")

my_dog = Dog("Buddy", 3)
my_dog.bark()
my_dog.sit()