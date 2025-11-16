import matplotlib.pyplot as plt
from statistics import median
from math import log



data = open("9_градусов_0.001сек_51см.txt").readline()
nums = list(map(int, data.split()))
counter = 0
time = []
for i in range(len(nums)):
    time.append(counter * 1)
    counter += 1
periods = []
time_of_periods = []
for i in range(len(nums) - 10000):
    if nums[i] == 1 and nums[i + 1] == 0:
        t1 = time[i + 1]
    if nums[i] == 0 and nums[i + 1] == 1:
        periods.append(time[i] - t1)
        time_of_periods.append(time[i])



# КОНФ. 1.1
# time_of_periods = time_of_periods[:757]
# periods = periods[:757]
# good_periods = list(filter(lambda x: x > 50, periods))


# КОНФ. 1.2
# time_of_periods = time_of_periods[:1426]
# periods = periods[:1426]
# good_periods = list(filter(lambda x: x > 50, periods))


# КОНФ. 1.3
# time_of_periods = time_of_periods[:602]
# periods = periods[:602]
# good_periods = list(filter(lambda x: x > 50, periods))


# КОНФ. 2.1
# time_of_periods = time_of_periods[118:397]
# periods = periods[118:397]
# good_periods = []
# for i in range(len(periods)):
#     x = time_of_periods[i]
#     y = periods[i]
#     if y < (x / 1600) + 1775 / 2:
#         good_periods.append(periods[i])



# КОФНФ. 2.2
# time_of_periods = time_of_periods[:693]
# periods = periods[:693]
# good_periods = periods


# КОНФ. 2.3
time_of_periods = time_of_periods[:691]
periods = periods[:691]
good_periods = list(filter(lambda x: x > 70, periods))




obr_periods = []
for i in range(len(periods)):
    if periods[i] in good_periods:
        obr_periods.append(periods[i])
        pred = periods[i]
    else:
        obr_periods.append(pred)


# plt.scatter(time_of_periods, obr_periods)
# plt.show()


speed = [70 / i for i in obr_periods]
speed_t = []
for i in range(len(speed)):
    if i % 2 == 0:
        speed_t.append(speed[i])
time_of_speed = []
for i in range(len(time_of_periods)):
    if i % 2 == 0:
        time_of_speed.append(time_of_periods[i])



# plt.scatter(time_of_speed, speed_t)
# plt.show()




ub_speed = [speed_t[0]]
time_of_speed2 = [time_of_speed[0]]
a = speed_t[0]
for i in range(len(speed_t)):
    if speed_t[i] < a:
        ub_speed.append(speed_t[i])
        time_of_speed2.append(time_of_speed[i])
        a = speed_t[i]



# plt.scatter(time_of_speed2, ub_speed)
# plt.show()
#
#
#
zatux = []
for i in range(len(ub_speed) - 1):
    v1 = ub_speed[i]
    v2 = ub_speed[i + 1]
    t1 = time_of_speed2[i]
    t2 = time_of_speed2[i + 1]
    zatux.append(log(v1 / v2) / (t2 - t1))

sred = sum(zatux) / len(zatux)
m = len(zatux) * (len(zatux) - 1)
summ = sum([(i - sred) ** 2 for i in zatux])
print(sred)
print((summ / m) ** 0.5)

