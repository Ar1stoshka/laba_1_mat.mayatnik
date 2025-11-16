import matplotlib.pyplot as plt
from statistics import median


data = open("3_градуса_0.005сек_86см.txt").readline()

nums = list(map(int, data.split()))
counter = 0
time = []
for i in range(len(nums)):
    time.append(counter * 5)
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

time_of_periods = time_of_periods[:200]
periods = periods[:200]
good_periods = list(filter(lambda x: x > 1750, periods))
sred = sum(good_periods) / len(good_periods)
periods = [i if i in good_periods else sred for i in periods]
plt.hist(periods, 16, color="#31A09A")
plt.suptitle("Гистограмма распределение обработанных периодов")
plt.xlabel("T мс (период)")
plt.ylabel("А (кол-во данных)")
plt.grid()
plt.show()


