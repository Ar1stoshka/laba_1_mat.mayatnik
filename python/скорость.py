import matplotlib.pyplot as plt


file_name = input()
data = open(file_name).readline()
nums = list(map(int, data.split()))
counter = 0
time = []
for i in range(len(nums)):
    time.append(counter * 5)
    counter += 1
periods = []
time_of_periods = []
for i in range(len(nums) - 10000):
    if nums[i] == 1 and nums[i + 1] == 0:
        t1 = time[i + 1]
    if nums[i] == 0 and nums[i + 1] == 1:
        periods.append(time[i] - t1)
        time_of_periods.append(time[i])


# для каждых данных индивидуально
time_of_periods = time_of_periods[:757]
periods = periods[:757]
# для каждых данных индивидуально
good_periods = list(filter(lambda x: x > 50, periods))
obr_periods = []
for i in range(len(periods)):
    if periods[i] in good_periods:
        obr_periods.append(periods[i])
        pred = periods[i]
    else:
        obr_periods.append(pred)


speed = [70 / i for i in obr_periods]
plt.plot(time_of_periods, speed, color="#149C07")
plt.suptitle("Зависимость V(t)")
plt.ylabel("V мм/мс (скорость в ниж. точке траектории)")
plt.xlabel("t мс (время)")
# для каждых данных индивидуально
plt.ylim(0, 0.5)
plt.grid()
plt.show()