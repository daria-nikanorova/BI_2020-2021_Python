import numpy as np
import random
import matplotlib.pyplot as plt


def walk_random(n):
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(1, n):
        random_value = random.randint(1, 4)
        if random_value == 1:
            x[i] = x[i - 1] + 1  # step to the right
            y[i] = y[i - 1]
        elif random_value == 2:
            x[i] = x[i - 1] - 1  # step to the left
            y[i] = y[i - 1]
        elif random_value == 3:
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1  # step up
        elif random_value == 4:
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1  # step down
    return x, y


steps = 10000  # number of steps
random_walk_coordinates = walk_random(steps)
random_x = random_walk_coordinates[0]
random_y = random_walk_coordinates[1]


# image size
plt.figure(figsize=(12, 8))
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['font.size'] = 15

plt.scatter(random_x, random_y, marker='$*$')

plt.title('2D random walk')

plt.savefig('3_random_walk.png')
