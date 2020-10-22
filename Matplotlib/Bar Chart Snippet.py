from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter


#print(plt.style.available)      #Shows the different themes style to apply on the plotting

plt.style.use('fivethirtyeight')
#plt.xkcd()      #Comic Style

""" dev_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

x_indices = np.arange(len(dev_x))   
width = 0.36

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

 """
""" plt.bar(x_indices-width, dev_y, width=width ,label='Developers')
plt.bar(x_indices, py_dev_y,width=width, label='Python')
 
plt.xlabel('Age')
plt.ylabel('Salary')

plt.xticks(ticks=x_indices, label=dev_x)
plt.title('Median Salary (INR by Age)')

#plt.grid(True)
plt.tight_layout()
plt.legend()
 """

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

    
languages = []
popularity = [] 



for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.xlabel('Popularity')


#plt.xticks(ticks=languages, label=dev_x)
plt.title('Most Popular Languages')

#plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()

