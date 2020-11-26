"""
Chapter 10.A Plotting Netflix
Second exercise

"""

import numpy as np
import matplotlib.pyplot as plt

file = open("tv_shows.txt", encoding="utf-8")

tv_shows = file.read().splitlines()

ratings = [0] * 10 #fill the list with 10 zeroes

#print(ratings)

for i in tv_shows:
    helo = i.split(";")
    if helo[2] != '':
        average = float(helo[2])
        min = int (average) # ook je index
        #print (average, min, max)
        if min <= average < min + 1:
            ratings[min] += 1


#print(ratings)

binList = ["0-1", "1-2", "2-3", "3-4", "4-5", "5-6", "6-7", "7-8", "8-9", "9-10"]
# print(len(binList))
# print(len(ratings))
# print(ratings)
index = 0
for i in binList:
    print(i +  ": " + str(ratings[index]))
    index += 1


x_plot = np.array(binList)
y_plot = np.array(ratings)

plt.xlabel("Bins")
plt.ylabel("Amount of movies in bin")
plt.plot(x_plot, y_plot, marker = "o", label = "Bins and amount of movies in bin")

plt.title("A plot of bins of Rating and their corresponding amount of movies having that rating")
plt.legend()
plt.show()
