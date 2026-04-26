pizaa = ""
while pizaa != "quit":
    pizaa = input("Enter a pizza souce: ")#提示输入要放在最前面,避免用户输入quit
    if pizaa == "quit":
        print("You have ordered a pizza with the following toppings:")
        break
    else:
        print("We will add " + pizaa + " to your pizza.")
