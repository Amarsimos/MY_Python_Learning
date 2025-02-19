import json
filename = "numbers.json"
try:
    with open(filename, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    number = input("Enter  like number:")
    with open(filename, "w") as f:
        data = json.dump(number,f)
        print("your number has been saved in the file" + data)
else:
    print("The number is:", data)