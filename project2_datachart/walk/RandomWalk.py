import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    def __init__(self,num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([-9,9])
        distance = choice([0,1,2,3,4,5,6,7,8,9])
        step = direction * distance
        return step

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
            

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.figure(figsize=(10,6))

    point_number = list(range(rw.num_points))
    plt.plot(rw.x_values,rw.y_values)
    # plt.plot(rw.x_values,rw.y_values,c=point_number,cmap=plt.cm.Blues,edgecolor='none',s=1)

    plt.scatter(0,0,c='green',edgecolor='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',cmap=plt.cm.Blues,edgecolor='none',s=100)

    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    # plt.axis('off')

    plt.show()

    keep_running = input("Keep running? (y/n): ")
    if keep_running == 'n':
        break
