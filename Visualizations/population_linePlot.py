import matplotlib.pyplot as plt

years = [2015, 2016, 2017, 2018, 2019]
total_populations = [1310152403, 1324517249, 1338676785, 1352642280, 1366417754]

plt.plot(years, total_populations)
plt.title("Year vs Population in India")
plt.xlabel("Year")
plt.ylabel("Total Population")
plt.show()
plt.close()
