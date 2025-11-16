import matplotlib.pyplot as plt


file_name = input()
data = open(file_name).readline()
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

plt.scatter(time_of_periods, periods, color="orange")
plt.grid()
plt.suptitle("Зависимость T(t)")
plt.xlabel("t мс (время)")
plt.ylabel("T мс (период)")
plt.show()