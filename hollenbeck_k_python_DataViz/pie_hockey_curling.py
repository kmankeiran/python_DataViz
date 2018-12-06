import csv
import matplotlib.pyplot as plt

curling = []
ice_hockey = []
# This is opening the olympics folder and reading it
with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0
    for row in reader:
        if row[6] == "Ice Hockey":
            ice_hockey.append(row)
        else:
            curling.append(row)
        line_count += 1

print('The total number of people winning in Ice Hockey:', len(ice_hockey))
print('The total number of people winning in Curling :', len(curling))

# The number of medals won by the gender divided by how many medals there are in total
pct_ice_hockey = int(len(ice_hockey) / line_count * 100)
pct_curling = int(len(curling) / line_count * 100)

print(pct_ice_hockey)
print(pct_curling)

labels = "Ice Hockey, Curling"
sizes = [pct_ice_hockey, pct_curling]
colors = ['yellowgreen', 'lightcoral']
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Which game has more winners?")
plt.xlabel("This chart shows how many people win in Ice Hockey vs Curling")
plt.show()
