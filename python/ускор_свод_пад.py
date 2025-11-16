import matplotlib.pyplot as plt
from statistics import median
from math import pi


data = open("9_градусов_0.001сек_51см.txt").readline()

nums = list(map(int, data.split()))
counter = 0
time = []
for i in range(len(nums)):
    time.append(counter * 1)
    counter += 1

t1 = 0
periods = []
time_of_periods = []
counter = 0
for i in range(len(nums) - 1):
    if nums[i] == 1 and nums[i + 1] == 0:
        counter += 1
        if counter == 1:
            t1 = time[i + 1]
        if counter == 3:
            periods.append(time[i + 1] - t1)
            t1 = time[i + 1]
            time_of_periods.append(time[i + 1])
            counter = 0

# ДЛЯ КОНФ. 2.3
time_of_periods = time_of_periods[:260]
periods = periods[:260]
good_periods = list(filter(lambda x: x > 1430, periods))
sred = sum(good_periods) / len(good_periods)
periods = [i if i in good_periods else sred for i in periods]
g = [(4 * pi ** 2 * 0.51 / (i * 10 ** -3) ** 2) for i in periods]
sred_g = sum(g) / len(g)
print(sred_g)
summ = sum([(i - sred_g) ** 2 for i in g])
m = len(g) * (len(g) - 1)
print((summ / m) ** 0.5)







# ДЛЯ КОНФ. 2.2
# time_of_periods = time_of_periods[:241]
# periods = periods[:241]
# good_periods = list(filter(lambda x: x > 1420, periods))
# sred = sum(good_periods) / len(good_periods)
# periods = [i if i in good_periods else sred for i in periods]
# g = [(4 * pi ** 2 * 0.51 / (i * 10 ** -3) ** 2) for i in periods]
# sred_g = sum(g) / len(g)
# print(sred_g)
# summ = sum([(i - sred_g) ** 2 for i in g])
# m = len(g) * (len(g) - 1)
# print((summ / m) ** 0.5)





# ДЛЯ КОНФ. 2.1
# time_of_periods = time_of_periods[:32]
# periods = periods[:32]
# good_periods = list(filter(lambda x: x > 1400, periods))
# sred = sum(good_periods) / len(good_periods)
# periods = [i if i in good_periods else sred for i in periods]
# g = [(4 * pi ** 2 * 0.51 / (i * 10 ** -3) ** 2) for i in periods]
# sred_g = sum(g) / len(g)
# print(sred_g)
# summ = sum([(i - sred_g) ** 2 for i in g])
# m = len(g) * (len(g) - 1)
# print((summ / m) ** 0.5)


#ДЛЯ КОНФ. 1.3
# time_of_periods = time_of_periods[:201]
# periods = periods[:201]
# good_periods = list(filter(lambda x: x > 1820, periods))
# sred = sum(good_periods) / len(good_periods)
# periods = [i if i in good_periods else sred for i in periods]
# g = [(4 * pi ** 2 * 0.86 / (i * 10 ** -3) ** 2) for i in periods]
# sred_g = sum(g) / len(g)
# print(sred_g)
# summ = sum([(i - sred_g) ** 2 for i in g])
# m = len(g) * (len(g) - 1)
# print((summ / m) ** 0.5)





# ДЛЯ КОНФ. 1.2
# time_of_periods = time_of_periods[150:476]
# periods = periods[150:476]
# good_periods = list(filter(lambda x: x > 1850, periods))
# sred = sum(good_periods) / len(good_periods)
# periods = [i if i in good_periods else sred for i in periods]
# g = [(4 * pi ** 2 * 0.86 / (i * 10 ** -3) ** 2) for i in periods]
# sred_g = sum(g) / len(g)
# summ = sum([(i - sred_g) ** 2 for i in g])
# m = len(g) * (len(g) - 1)
# print((summ / m) ** 0.5)





# ДЛЯ КОНФ. 1.1
# time_of_periods = time_of_periods[:200]
# periods = periods[:200]
# good_periods = list(filter(lambda x: x > 1750, periods))
# sred = sum(good_periods) / len(good_periods)
# periods = [i if i in good_periods else sred for i in periods]
# g = [(4 * pi ** 2 * 0.86 / (i * 10 ** -3) ** 2) for i in periods]
# print(sum(g) / len(g))
