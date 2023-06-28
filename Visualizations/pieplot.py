import matplotlib.pyplot as plt
sizes = [20, 25, 40, 15]
labels = ["Cats", "Dogs", "Rabbits", "Parrots"]

plt.pie(sizes, labels = labels, autopct = "%.2f")
plt.show()
plt.close()
