import csv
import matplotlib.pyplot as plt
# These are creating buckets to divide the genders between men and women

men_and_women = [1, 0]
how_many = [75, 63]


#Men = 75, Women = 63

plt.bar(men_and_women, how_many, label='Women and Men')




plt.xlabel('Men and Women')
plt.ylabel('Numbers')
plt.legend()
plt.title("Who participated in the most popular sport?")
plt.xlabel("This chart shows how many men and women participated and won in ice hockey")
plt.show()