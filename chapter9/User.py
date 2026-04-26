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
