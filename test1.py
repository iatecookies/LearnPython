file = open("earthquakes-1998.csv", "r")
earthquakes = ""
for line in file:
    earthquakes += line
earthquakes = earthquakes[0:-1]

# Start coding below


class Event:
    def __init__(self, magnitude, __):  # finish this method to store the right fields
        self.magnitude = magnitude
        self.__ = __

    def __str__(self):
        # finish this method to print the right sentence for each event.
        return 'An event occurred on '


class Nuclear_explosion(Event):
    def __init__(self):
        # finish this constructor yourself
        self.__ = __

    def __str__(self):
        return __  # finish this too

# and totally create your own Nuclear Explosions class


all_earthquakes = earthquakes.split('\n')  # split the input based on the newline character

for row in all_earthquakes:
    row_list = row.split(',')  # split the list

    # create the needed variables here
    type = row_list[4]

    if type == 'Earthquake':
        # create an earthquake instance and print it
        print(__)
    else:
        # create a nuclear explosion instance and append it
        print(__)
