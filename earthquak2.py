"""
Chapter 12.A Earthquakes
Practicing dictionaries
"""
import csv
tel = 1965
while tel < 2017:
    file = open('earthquakes-multiple-years.csv')
    file_reader = csv.reader(file, delimiter=",") #csv module has this reader function that makes a list of every line and use , as delimitr

    next(file_reader) #Skip the first line Next() is also from csv module

    outputMonth = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8:"August", 9:"September", \
     10:"October", 11: "November", 12: "December"}
    avg_amount_earthquakes = {1:0,2: 0,3: 0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    avg_magnitude = {1:0,2: 0,3: 0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    for f in file_reader:
        date = f[0]
        date = date.split("/")
        month = int(date[0])
        year = int(date[2])
        magnitude = float(f[-2])
        if 65 <= year <= 99:
            year = year + 1900
        else:
            year = year + 2000

        if tel == year:
            for i in range(1,13):
                if i == month:
                    avg_amount_earthquakes[i] += 1
                    avg_magnitude[i] += magnitude

    for j in range(1,13):
        if avg_amount_earthquakes[i] != 0:
            printIT = True
        else:
            printIT = False
            break
    # if avg_amount_earthquakes[1] != 0 and avg_amount_earthquakes[2] != 0 and avg_amount_earthquakes[3] != 0 and avg_amount_earthquakes[4] != 0 \
    #     and avg_amount_earthquakes[5] != 0 and avg_amount_earthquakes[6] != 0 and avg_amount_earthquakes[7] != 0 and avg_amount_earthquakes[8] != 0 \
    #     and avg_amount_earthquakes[9] != 0 and avg_amount_earthquakes[10] != 0 and avg_amount_earthquakes[11] != 0 and avg_amount_earthquakes[12] != 0:
    #
    if printIT:
        print(f"Number of earthquakes, and average magnitude of earthquakes per month of {tel} are:")
        for i in range(1,13):    
            avg_magnitude[i] = avg_magnitude[i]/avg_amount_earthquakes[i]
            print (outputMonth[i], avg_amount_earthquakes[i], round(avg_magnitude[i],1))
    file.close()
    tel += 1
