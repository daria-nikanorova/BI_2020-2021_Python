import numpy as np
import random
import time
import matplotlib.pyplot as plt


def np_random_time(n):
    np_result, random_result, np_size_result = [], [], []
    up = 1
    while up <= n:
        start1 = time.time()
        np.random.uniform(0, 1, size=up)
        end1 = time.time()
        np_size_time = end1 - start1
        np_size_result += [np_size_time]
        start2 = time.time()
        for i in range(0, up):
            np.random.uniform(0, 1)
        end2 = time.time()
        np_time = end2 - start2
        np_result += [np_time]
        start3 = time.time()
        for j in range(0, up):
            random.uniform(0, 1)
        end3 = time.time()
        random_time = end3 - start3
        random_result += [random_time]
        up *= 10
    return np_result, random_result, np_size_result


res = np_random_time(10000)
np_res = res[0]
random_res = res[1]
np_size_res = res[2]
xs = [10 ** i for i in range(len(np_res))]

# image size
plt.figure(figsize=(12, 8))
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['font.size'] = 15

# labels are needed for a legend
plt.plot(xs, np_res, label='numpy random')
plt.plot(xs, random_res, label='random')
plt.plot(xs, np_size_res, label='numpy random (with size parameter)')

plt.title('Numpy random vs random')

# add labels
plt.xlabel('number of randomly taken floats')
plt.ylabel('time, s')

# add legend
plt.legend()

# add grid
plt.grid()

# plt.show()
plt.savefig('1_np_random_time.png')
