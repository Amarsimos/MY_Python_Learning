sandwich_orders = ['ham', 'turkey','beef', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
for sandwich in finished_sandwiches:
    print("Your " + sandwich + " sandwich is ready.")
print(finished_sandwiches)