import matplotlib.pyplot as plt
from statistics import median


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
print(len(periods) - len(good_periods))
print(len(periods))
sred = sum(good_periods) / len(good_periods)
print(sred)
periods = [i if i in good_periods else sred for i in periods]
plt.scatter(time_of_periods, periods)
plt.ylim(0,1900)
plt.show()




# ДЛЯ КОНФ. 2.2
# time_of_periods = time_of_periods[:241]
# periods = periods[:241]
# good_periods = list(filter(lambda x: x > 1420, periods))
# print(len(periods) - len(good_periods))
# print(len(periods))
# sred = sum(good_periods) / len(good_periods)
# print(sred)
# periods = [i if i in good_periods else sred for i in periods]
# plt.scatter(time_of_periods, periods)
# plt.ylim(0,1900)
# plt.show()




# ДЛЯ КОНФ. 2.1
# time_of_periods = time_of_periods[:32]
# periods = periods[:32]
# good_periods = list(filter(lambda x: x > 1400, periods))
# print(len(periods) - len(good_periods))
# sred = sum(good_periods) / len(good_periods)
# print(sred)
# periods = [i if i in good_periods else sred for i in periods]
# plt.scatter(time_of_periods, periods)
# plt.ylim(0,1800)
# plt.show()




# ДЛЯ КОНФ. 1.3
# time_of_periods = time_of_periods[:201]
# periods = periods[:201]
# good_periods = list(filter(lambda x: x > 1820, periods))
# print(len(periods) - len(good_periods))
# sred = sum(good_periods) / len(good_periods)
# print(sred)
# periods = [i if i in good_periods else sred for i in periods]
# plt.scatter(time_of_periods, periods)
# plt.ylim(0, 2100)
# plt.show()





# ДЛЯ КОНФ. 1.2
# time_of_periods = time_of_periods[150:476]
# periods = periods[150:476]
# good_periods = list(filter(lambda x: x > 1850, periods))
# print(len(periods) - len(good_periods))
# sred = (sum(good_periods) / len(good_periods))
# print(sred)
# periods = [i if i in good_periods else sred for i in periods]
# plt.scatter(time_of_periods, periods, color="#8E3115")
# plt.ylim(0, 2100)
# plt.show()







# ДЛЯ КОНФ. 1.1
# time_of_periods = time_of_periods[:200]
# periods = periods[:200]
# good_periods = list(filter(lambda x: x > 1750, periods))
# print(len(periods) - len(good_periods))
# sred = sum(good_periods) / len(good_periods)
# print(sred)
# periods = [i if i in good_periods else sred for i in periods]
# plt.scatter(time_of_periods, periods, color="#8E3115")
# plt.grid()
# plt.ylim(0, 2400)
# plt.xlim(0, 550000)
# plt.suptitle("Зависимость T(t) без аномалий")
# plt.xlabel("t мс (время)")
# plt.ylabel("T мс (период)")
# plt.show()


