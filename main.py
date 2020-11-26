student_tests_file = open("studenttests.txt")
student_tests_read = student_tests_file.read() #Some have no tests done at all
l_student_tests = student_tests_read.splitlines() #Each student with their tests is an element

passed_tests_file = open("studentpassedtests.txt")
passed_tests_read = passed_tests_file.read() #Some have no passed tests
l_passed_tests = passed_tests_read.splitlines() #Each student with their passed tests is an element

l_student_numbers_1 = [] #student numbers that did tests
l_tests_taken_1 = [] #tests taken but not split per subject yet
l_tests_taken_2 = [] #tests taken and split per subject, is list of lists

for test_1 in l_student_tests:
    x_1 = test_1.split(":") #splits the student numbers from the tests
    student_numbers_1 = x_1[0] #the student numbers
    tests_taken = x_1[1] #all the tests taken, but not yet split
    if tests_taken == '': #if tests_taken_split empty -> don't use student_numbers with same index
        continue
    else:
        l_student_numbers_1.append(student_numbers_1)
        l_tests_taken_1.append(tests_taken)

for code_1 in l_tests_taken_1: #all the tests taken and split, then stored in list
    tests_taken_split = code_1.split(",")
    l_tests_taken_2.append(tests_taken_split)

l_student_numbers_2 = [] #student numbers that passed tests and are in other student numbers list
l_tests_passed_1 = [] #tests passed but not split per subject yet
l_tests_passed_2 = [] #tests passed and split per subject, is list of lists

for test_2 in l_passed_tests:
    x_2 = test_2.split(":") #splits the student numbers from the passed tests
    student_numbers_2 = x_2[0] #the student numbers
    tests_passed = x_2[1] #all the tests passed, but not yet split
    if student_numbers_2 in l_student_numbers_1: #if student numbers relevant, add numbers, tests to lists
        l_student_numbers_2.append(student_numbers_2)
        l_tests_passed_1.append(tests_passed)
    else:
        continue #not relevant so do nothing

for code_2 in l_tests_passed_1:
    tests_passed_split = code_2.split(",") #all the tests taken and split
    l_tests_passed_2.append(tests_passed_split)

amount_total_tests = []
amount_passed_tests = []
amount_failed_tests = []

for number_1 in l_tests_taken_2: #creates list with amount of total tests done per studentnumber
    amount_1 = len(number_1)
    amount_total_tests.append(amount_1)


for number_2 in l_tests_passed_2: #creates list with amount of passed tests done per studentnumber
    if number_2 == ['']:
        amount_2 = len(number_2) - 1
        amount_passed_tests.append(amount_2)
    elif number_2 != '':
        amount_2 = len(number_2)
        amount_passed_tests.append(amount_2)

index_1 = 0 #amount of failed test for one index

while index_1 <= 244: #calculates amount of failed tests per student
   failed_test = amount_total_tests[index_1] - amount_passed_tests[index_1]
   amount_failed_tests.append(failed_test)
   index_1 += 1

student_score = [] #list of score by total tests / failed tests, no fails is total tests * 2

index_2 = 0

while index_2 <= 244: #assigns scores to each student
    if amount_failed_tests[index_2] == 0: #bonus for students without failed tests
        score = amount_total_tests[index_2] * 2
        student_score.append(score)
        index_2 += 1
    elif amount_failed_tests[index_2] == amount_total_tests[index_2]:
        score = 1.0
        student_score.append(score)
        index_2 += 1
    elif amount_failed_tests[index_2] != amount_total_tests[index_2]: #score assignment for students with failed tests
        score = amount_total_tests[index_2] / amount_failed_tests[index_2]
        student_score.append(score)
        index_2 += 1

students_information = []

index_3 = 0

while index_3 <= 244:
    adding_info = []
    adding_info.append(l_student_numbers_1[index_3])
    adding_info.append(student_score[index_3])
    adding_info.append(amount_failed_tests[index_3])
    students_information.append(adding_info)
    index_3 += 1

sorted_list = sorted(students_information)

for i in sorted_list:
    print(i)
