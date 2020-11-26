"""
Chapter 11 Grading Students
Practicing sets
"""

file1 = open("studenttests.txt")
file2 = open("studentpassedtests.txt")

studenttests = file1.read().splitlines()
studentpassedtests = file2.read().splitlines()

list2 = []
for (i, j) in zip( studenttests, studentpassedtests) :
    studenttests = i.split(":")
    studentpassedtests = j.split(":")

    studentpassedtests_numbers = studentpassedtests[0]
    studentpassedtests_courses = studentpassedtests[1]
    studentpassedtests__courses_splitlist = studentpassedtests_courses.split(',')

    studenttests_numbers = studenttests[0]
    studenttests_courses = studenttests[1]
    studenttests_courses_splitlist = studenttests_courses.split(',')

    studentpassedtests_set = set(studentpassedtests__courses_splitlist)
    studenttests_set = set(studenttests_courses_splitlist)
    setResult = studenttests_set - studentpassedtests_set #amount of courses failed
    # print(studentpassedtests_set, studenttests_set)

    studenttests_set_value = 0
    if studenttests_set == {''}:
        studenttests_set_value = 0
    else:
        studenttests_set_value = len(studenttests_set)
    #print(studenttests_set, studenttests_set_value, len(setResult))
    try:
        scoreStudent = studenttests_set_value/len(setResult)
        #print (studenttests_numbers, scoreStudent)
    except Exception as ex:
        #print(studenttests_numbers, ex)
        scoreStudent = studenttests_set_value*2
        #print (studenttests_numbers, scoreStudent)

    list1 = []
    list1.append(str(studenttests_numbers))
    list1.append(scoreStudent)
    list1.append(len(setResult))
    list2.append(list1) # puts in a new list
    # print(list1)  # this will also print it nice but not sorted

sortedList = sorted(list2)
for i in sortedList:
    print (i)
