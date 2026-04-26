while True:
    number = input("Enter a number: ")
    if int(number) % 10 == 0:
            print(number, "is a multiple of 10")
    else:
        print(number, "is not a multiple of 10")