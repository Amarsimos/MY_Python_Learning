from random import randint
import pygal

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

die1 = Die(8)
die2 = Die(8)

results = []
for roll_num in range(500000000):
    result = die1.roll()+die2.roll()
    results.append(result)

frequencies = []
max_result = die1.sides + die2.sides
for value in range (2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)
# print(results)
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
#                  '11', '12','13','14','15','16']
hist.x_labels = [i for i in range(2,max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D10', frequencies)
hist.render_to_file('die_2_visual.svg')