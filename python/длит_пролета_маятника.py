import matplotlib.pyplot as plt
from statistics import median


data = open("3_градуса_0.005сек_86см.txt").readline()
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


plt.scatter(time_of_periods, periods, color="#639FF8")
plt.grid()
plt.suptitle("Зависимость t'(t)")
plt.xlabel("t мс (время)")
plt.ylabel("t' мс (время пролета маятника через датчик)")
plt.xlim(0, 600000)
plt.show()


