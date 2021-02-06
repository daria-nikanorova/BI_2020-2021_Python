import numpy as np
import random
import time
import matplotlib.pyplot as plt


def np_random_time(n):
    np_result, random_result = [], []
    up = 1
    while up <= n:
        start = time.time()
        for i in range(0, up):
            np.random.uniform(0, 1)
        end = time.time()
        np_time = end - start
        np_result += [np_time]
        start = time.time()
        for j in range(0, up):
            random.uniform(0, 1)
        end = time.time()
        random_time = end - start
        random_result += [random_time]
        up *= 10
    return np_result, random_result


res = np_random_time(100000)
np_res = res[0]
random_res = res[1]
xs = [10 ** i for i in range(len(np_res))]

# image size
plt.figure(figsize=(12, 8))
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['font.size'] = 15

# labels are needed for a legend
plt.plot(xs, np_res, label='numpy random')
plt.plot(xs, random_res, label='random')

plt.title('Numpy random vs random')

# add labels
plt.xlabel('number of randomly taken floats')
plt.ylabel('time, s')

# add legend
plt.legend()

# add grid
plt.grid()

plt.savefig('1_np_random_time.png')
