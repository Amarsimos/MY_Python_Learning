flag = True
while flag:
    age = input("How old are you? ")
    if age == "quit":
        flag = False
        break
    if int(age)<3:
        print("Ticket is free for you.") 
    if int(age)>=3 and int(age)<=12:
        print("Ticket is $10.")
    if int(age)>12:
        print("Ticket is $15.")
    