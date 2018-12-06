import csv
import matplotlib.pyplot as plt

gold_1924 = []
gold_1948 = []
gold_1972 = []
gold_2002 = []
gold_2014 = []

women_1924 = []
women_1948 = []
women_1972 = []
women_2002 = []
women_2014 = []

men_1924 = []
men_1948 = []
men_1972 = []
men_2002 = []
men_2014 = []

categories = []

year = [1924, 1948, 1972, 2002, 2014]
women = [len(women_1924), len(women_1948), len(women_1972), len(women_2002), len(women_2014)]
men = [len(men_1924), len(men_1948), len(men_1972), len(men_2002), len(men_2014)]


with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1

        else:
            if row[0] == "1924":
                if row[5] == "Men" and row[7] =="Gold":
                    men_1924.append(row)
                else:
                    women_1924.append(row)

            if row[0] == "1948":
                if row[5] == "Men" and row[7] =="Gold":
                    men_1948.append(row)
                else:
                    women_1948.append(row)

            if row[0] == "1972":
                if row[5] == "Men" and row[7] =="Gold":
                    men_1972.append(row)
                else:
                    women_1972.append(row)

            if row[0] == "2002":
                if row[5] == "Men" and row[7] =="Gold":
                    men_2002.append(row)
                else:
                    women_2002.append(row)

            if row[0] == "2014":
                if row[5] == "Men" and row[7] =="Gold":
                    men_2014.append(row)
                else:
                    women_2014.append(row)


plt.scatter(year, women, label='Women')
plt.scatter(year, men, label='Men')
# you can do plt.bar, plt.plot, plt.scatter


plt.xlabel('Years')
plt.ylabel('Women and men')
plt.legend()
plt.title("What year did women win more golds vs men?")
plt.xlabel("This chart shows how many gold medals women and men won in each year")
plt.show()
