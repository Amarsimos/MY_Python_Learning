def sandwich(*toppings):
    print("You ordered a sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)

sandwich("ham", "cheese", "tomato", "lettuce")
sandwich("bread", "butter", "eggs")
sandwich("ham", "cheese", "tomato", "lettuce", "mustard", "mayo")