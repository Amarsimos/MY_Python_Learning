import json

filename = "usersname.json"

try:
    with open(filename, "r") as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your username? ")
    with open(filename, "w") as f:
        json.dump(username, f)
        print("we'll remember you when you come back " + username + "!")
else:
    print("Welcome back " + username + "!")

