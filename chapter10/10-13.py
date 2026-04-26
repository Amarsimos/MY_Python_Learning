import json 

def greet_user():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
        print(f"Hello, {username}!")
    else:
        check_username = input("Enter your name to check: ")
        if check_username == username:
            print(f"Hello, {username}!")
        else:
            print("Incorrect username.")
            new_username = get_new_username()
            print(f"Hello, {new_username}!")#(f格式简洁好用)

def get_new_username():
    username = input("What is your new name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


greet_user()
