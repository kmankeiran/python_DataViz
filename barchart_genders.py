import csv
import matplotlib.pyplot as plt
# These are creating buckets to divide the genders between men and women
year = [1924, 1948, 1972, 2002, 2014]
women = [10, 20, 30, 40, 50]

plt.bar(year, women, label='Women')
# you can do plt.bar, plt.plot, plt.scatter


plt.xlabel('Years')
plt.ylabel('Women')
plt.legend()
plt.title("What year did women win more medals?")
plt.xlabel("This chart shows how many medals women won at what year")
plt.show()
