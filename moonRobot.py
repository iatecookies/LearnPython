"""
Author: Jun Fei Cheung (s1719890) & Kyra Koper (s2767902)
Last worked: 4-11-2020
"""
import numpy as np
import random


def findPath(listOfCoordinates):
    # Determine what would be the fastest way, first stone 1 or first stone 2?
    # steps from start to stone1
    stepStone1 = listOfCoordinates[0][0] + listOfCoordinates[0][1]
    # step from start to stone2
    stepStone2 = listOfCoordinates[1][1] + listOfCoordinates[1][0]

    totalDistance = 0
    # Check which step is shortest
    if stepStone1 <= stepStone2:
        print("Stone1 at location " + str(listOfCoordinates[0]) + " is the shortest path.")
        totalDistance = stepStone1
    else:
        listOfCoordinates.reverse()
        print("Stone2 at location " + str(listOfCoordinates[0]) + " is the shortest path.")
        totalDistance = stepStone2

    print(f"List of coordinates {listOfCoordinates}. \n")

    # Travel the coordinates and keep track of your route
    # Travel from start point (0,0) to stone1
    path = [[0,0]]
    point = [0,0]
    while listOfCoordinates[0] != point:
        # Check if on same x coordinate
        if point[0] != listOfCoordinates[0][0]:
            point[0] = point[0] + 1
            path.append([point[0],point[1]])
        else:
            if point[1] != listOfCoordinates[0][1]:
                point[1] = point[1] + 1
                path.append([point[0],point[1]])

    # Travel to stone2, through x axis
    xDiff = listOfCoordinates[1][0] - listOfCoordinates[0][0]
    if xDiff > 0:
        for i in range(xDiff):
            point[0] = point[0] + 1
            path.append([point[0],point[1]])
    else:
        for i in range(-xDiff):
            point[0] = point[0] - 1
            path.append([point[0],point[1]])
        xDiff = xDiff * - 1

    # Travel to stone2, through y axis
    yDiff = listOfCoordinates[1][1] - listOfCoordinates[0][1]
    if yDiff > 0:
        for i in range(yDiff):
            point[1] = point[1] + 1
            path.append([point[0],point[1]])
    else:
        for i in range(-yDiff):
            point[1] = point[1] - 1
            path.append([point[0],point[1]])
        yDiff = yDiff * - 1

    totalDistance = totalDistance + xDiff + yDiff
    return path, totalDistance



def giveCoordinates(tupleArray):
    # (array([2, 2], dtype=int64), array([1, 2], dtype=int64))
    reverse_listOfCoordinates = list(zip(tupleArray[0], tupleArray[1]))
    listOfCoordinates = []
    for coordinate in reverse_listOfCoordinates:
        listOfCoordinates.append(list(coordinate[::-1]))
    return listOfCoordinates



def findStone(moon):
    return np.where(moon == 1)



def printResult(moon, shortestPath, totalDistance):
    # Print result of shortest path and how many steps needed to take
    print(shortestPath)
    print(f"The shortest path to get both stones is {totalDistance} steps \n")

    moon = moon.astype('str')
    for path in shortestPath:
        moon[path[1], path[0]] = " X "

    print("This is the path that the moonrobot follows: \n")
    print(moon)



def main():
    moonSize, moon = getMoon()
    print(moon)
    # Find the location of both stones
    # coordinates are in (row, column)
    # (array([2, 2], dtype=int64), array([1, 2], dtype=int64))
    tupleArray = findStone(moon)

    # Give coordinates of the stones
    listOfCoordinates = giveCoordinates(tupleArray)

    # Find shortest path
    shortestPath, totalDistance = findPath(listOfCoordinates)

    # Print your route as well as the length of your travels
    printResult(moon, shortestPath, totalDistance)

# You get this function for free to retrieve the size of the moon from the user. You're free to write your own!
def getMoon():
    moonSize = input("On what moon size do you want your robot to search (5, 6, 7 or 8)? ")
    try:
        moonSize = int(moonSize)
        if moonSize in [5, 6, 7, 8]:
            moon = np.zeros((moonSize, moonSize))
            while moon[0, 0] == 1 or ((moon == 1).sum() < 2):
                moon[0, 0] = 0
                moon[random.randint(0, moonSize-1), random.randint(0, moonSize-1)] = 1
            return moonSize, moon
        else:
            print("Your input is invalid!")
            return getMoon()
    except:
        print("Your input is invalid!")
        return getMoon()

# This makes sure that the program start running with the main() function
if __name__ == "__main__":
    main()
