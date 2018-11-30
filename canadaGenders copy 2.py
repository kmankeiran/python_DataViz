import csv
import matplotlib.pyplot as plt
# These are creating buckets to divide the genders between men and women
women = []
men = []
# This is opening the olympics folder and reading it
with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0
    for row in reader:
        if row[5] == "Men":
            men.append(row)
        else:
            women.append(row)
        line_count += 1

print('The total number of men winning medals:', len(men))
print('The total number of women winning medals:', len(women))

# The number of medals won by the gender divided by how many medals there are in total
pct_men = int(len(men) / line_count * 100)
pct_women = int(len(women) / line_count * 100)

print(pct_men)
print(pct_women)

labels = "Men, Women"
sizes = [pct_men, pct_women]
colors = ['yellowgreen', 'lightskyblue']
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Which Gender won more medals?")
plt.xlabel("This chart shows which gender won more medals than the other throughout the world and time")
plt.show()
