users = ["Alice", "Bob", "Charlie","admin","operator"]
for user in users:
    if user == "admin" :
        print(user + " is an admin ")
    else:
        print(user + " Helloword!")
        
del users[:]
if not users:
   print("No users found")