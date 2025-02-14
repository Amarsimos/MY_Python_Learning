import time
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    def greets_user(self):
        print("Hello", self.first_name, self.last_name, "!")
    def describe(self):
        print("I am", self.age, "years old and my name is", self.first_name, self.last_name)
    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Login attempts:", self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Login attempts:", self.login_attempts)

class Privileges():
    def __init__(self ):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print("Privileges:", self.privileges)

class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = Privileges()


admin1 = Admin("John", "Doe", 30)
admin1.greets_user()
admin1.describe()
admin1.privileges.show_privileges()

user1 = User("Amarsimos", "Gen", 25)
print('greeted people')
user1.greets_user()
print('described people')
user1.describe()

print('login attempts')
print(user1.login_attempts, 'attempts')
user1.increment_login_attempts()
time.sleep(1)
user1.increment_login_attempts()
time.sleep(1)
user1.increment_login_attempts()
time.sleep(1)
user1.increment_login_attempts()
time.sleep(1)
user1.increment_login_attempts()
time.sleep(1)

print('reset')
user1.reset_login_attempts()