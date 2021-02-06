import numpy as np
import random
import time
import matplotlib.pyplot as plt


def check_sort(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True


def monkey_sort(unsorted):
    while not check_sort(unsorted):
        random.shuffle(unsorted)
    return unsorted


def measure_monkey_sort(n):
    sorting_time = {'n_of_obj': [i for i in range(1, n+1)],
                    'mean_time': [],
                    'sd_time': []}
    for i in range(1, n+1):
        results = []
        print(i)
        for j in range(4):
            a = np.random.randint(50, size=i)
            start = time.time()
            monkey_sort(a)
            end = time.time()
            result = end - start
            results += [result]
        mu = np.mean(results)
        sd = np.std(results)
        sorting_time['mean_time'] += [mu]
        sorting_time['sd_time'] += [sd]
    return sorting_time


monkey_sort_10 = measure_monkey_sort(10)
monkey_sort_10['errors'] = [b / m for b, m in zip(monkey_sort_10['sd_time'], np.sqrt(monkey_sort_10['mean_time']))]

# image size
plt.figure(figsize=(12, 8))
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['font.size'] = 15

# labels are needed for a legend
bars = monkey_sort_10['mean_time']
errors = monkey_sort_10['errors']
xs = monkey_sort_10['n_of_obj']
plt.bar(xs, bars, width=0.8, yerr=errors, capsize=7, label='mean time')

plt.title('Time of monkey sorting')

# add labels
plt.xlabel('size of list to be sorted')
plt.ylabel('time, s')

# add legend
plt.legend()

plt.savefig('2_sort_time.png')
