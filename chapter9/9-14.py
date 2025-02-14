import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll(self):
        x = random.randint(1, self.sides)
        print(x,end=" ")#控制结尾的换行符
    
die6 = Die(6)
die10 = Die(10)
die20 = Die(20)

print("Rolling a 6-sided die 10 times:")
for i in range(10):
    die6.roll()
print('\n')

print("Rolling a 10-sided die 10 times:")
for i in range(10):
    die10.roll()
print('\n')

print("Rolling a 20-sided die 10 times:")
for i in range(10):
    die20.roll()