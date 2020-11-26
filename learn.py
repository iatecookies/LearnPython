"""
Chapter 10.A Plotting Netflix
First exercise
Learning how to use matplotlib
"""


import numpy as np
import matplotlib.pyplot as plt

file = open("tv_shows.txt", encoding="utf-8")
tv_shows = file.read().splitlines()
year = 0
#yearList = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
yearList = list(range(2000,2021))
#print(years)
yearCount = [0] * 21 #fill the list with 21 zeroes
average = 0
sumRating = [0] * 21

for i in tv_shows:
    index = 0
    helo = i.split(";")
    year = int(helo[1])
    if helo[2] != '':
        average = float(helo[2])
        if year in yearList:
            index = yearList.index(year)
            yearCount[index] += 1
            sumRating[index] = sumRating[index] + average

# print(yearCount)
# print (sumRating)
arrayList = []
index = 0
for i in yearList:
    avg = sumRating[index] / yearCount[index]
    arrayList.append( round(avg, 4))
    print(str(i) + ": " + str(round(avg, 4))) #round to a maximum of four decimals
    index += 1

avg_plot = np.array(arrayList)
year_plot = np.array(yearList)

plt.xlabel("Years")
#plt.xticks(yearList)
plt.ylabel("Average rating")
plt.plot(year_plot, avg_plot, label = "Years and average rating")

plt.title("A plot of years and their corresponding average ratings")
plt.legend()
plt.show()
