response = {}

ask_flag = True
while ask_flag:
    name = input("What's your name?")
    place = input("Where you want to go?")

    response[name] = place
    repeat = input("Do you want to add more people? (y/n)")
    if repeat == "n":
        ask_flag = False

print("\n---poll result---")
for name,place in response.items():
    print(name,"wants to go to",place)