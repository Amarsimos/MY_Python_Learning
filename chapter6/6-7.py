me = {'first name':'shimotsuki','last name':'gen', 'age':25, 'city':'Tokyo'}
alice = {'first name':'alice','last name':'smith', 'age':23, 'city':'New York'}
bob = {'first name':'bob','last name':'jones', 'age':30, 'city':'Los Angeles'}
people = [me, alice, bob]
for person in people:
    print(person)
print(me['age'])
print(me['city'])
print(me['first name'])
print(me['last name'])