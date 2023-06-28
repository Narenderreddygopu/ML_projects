import matplotlib.pyplot as plt
values = [1, 2, 5, 6, 6, 7, 7, 8, 8, 8, 9, 10, 21]

plt.boxplot(values)
plt.yticks(range(1, 22))
plt.ylabel("Value")
plt.show()
plt.close()
