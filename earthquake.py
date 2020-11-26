"""
Chapter 12.A Earthquakes
Practicing dictionaries
"""

# your code goes here
import csv
file = open('earthquakes-1998.csv')
file_reader = csv.reader(file, delimiter=",") #csv module has this reader function that makes a list of every line and use , as delimitr

next(file_reader) #Skip the first line Next() is also from csv module

outputMonth = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8:"August", 9:"September", 10:"October", 11: "November", 12: "December"}
avg_amount_earthquakes = {1:0,2: 0,3: 0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
avg_magnitude = {1:0,2: 0,3: 0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}

for f in file_reader:
    date = f[0]
    date = date.split("/")
    month = int(date[0])
    magnitude = float(f[-2])
    avg_amount_earthquakes[month] += 1
    avg_magnitude[month] += magnitude

    # if month[1] == 1:
    #     avg_amount_earthquakes[month] += 1
    #     avg_magnitude[month] += magnitude

print("Number of earthquakes, and average magnitude of earthquakes per month of 1998 are:")
for i in range(1,13):
    avg_magnitude[i] = avg_magnitude[i]/avg_amount_earthquakes[i]
    print( outputMonth[i], avg_amount_earthquakes[i], round(avg_magnitude[i],1))
