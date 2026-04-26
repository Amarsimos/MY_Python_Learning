while True:
    number1 = input("Enter 1 number: ")
    number2 = input("Enter other 1 number: ")
    try:
        int(number1)
        int(number2)
    except ValueError:
        print("Invalid input")
    else:
        print(number1 + number2)
