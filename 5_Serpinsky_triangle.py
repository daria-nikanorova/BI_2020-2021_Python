import numpy as np
import random
import matplotlib.pyplot as plt


def serpinsky_triangle(n):
    x = np.zeros(n)
    y = np.zeros(n)
    xv = [0, 10, 20]
    yv = [0, 10, 0]
    for i in range(1, n):
        random_value = random.randint(0, 2)
        x[i] = (xv[random_value] + x[i-1])/2
        y[i] = (yv[random_value] + y[i-1])/2
    return x, y


serpinsky_triangle_coordinates = serpinsky_triangle(100000)
random_x = serpinsky_triangle_coordinates[0]
random_y = serpinsky_triangle_coordinates[1]

plt.figure(figsize=(12, 8))
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['font.size'] = 15

plt.scatter(random_x, random_y, s=0.1)

plt.title('Serpinsky triangle')

plt.savefig('5_Serpinsky triangle.png')
