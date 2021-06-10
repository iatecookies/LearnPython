# numbers = [5, 7, 2, 1, 19, 87]
# new_numbers = []
# while numbers:
#     min = numbers[0]
#     for i in range(len(numbers)):
#         if numbers[i] < min:
#             min = numbers[i]
#     new_numbers.append(min)
#     numbers.remove(min)
# print(new_numbers)


# x = 9
# y = 9
# if x < y:
#     print("Optie1")
# else:
#     print("Optie2")

# days = [5, 7, 2, 1, 19, 87]
# values = [1, 2, 3, 4]
#
#
# def moving_average(values: list[int], n: int) -> list[Optional[float]]:
#     moving_average_values = []
#     for i in range(len(values)):
#         moving_average = None
#
#         if(i >= n-1):
#             moving_average = 0
#             selector = i-n
#             while(selector < i):
#                 selector += 1
#                 moving_average += values[selector]/n
#         moving_average_values.append(moving_average)
#     return moving_average_values
#
#
# print(moving_average(days))


# for i in range(3):
#     for j in range(3):
#         print(str(i) + ',' + str(j))


# number = [1, 2, 3, 4]
# number2 = [2, 2, 3, 4]
#
# result = number + number2
# print(result)

print(bool([1, 2, 3]))

print(bool([2, 3, 4, 5] == False))
#
#
# klinkers = ['a', 'e', 'i', 'o', 'u']
# print(klinkers[0:3])

# even_numbers = {2, 4, 6, 8, 10}
# odd_numbers = {1, 3, 5, 7, 9}
# print(even_numbers - even_numbers)


# print(bool(2460 != "2460"))
#
#
# print([12, 11] + 12)

# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [163, 1241]]
#
# sum = 0
# avg = 0
# tel = 0
# for number in numbers:
#     for i in number:
#         sum = sum + i
#         tel = tel + 1
# print(f"total = {sum}")
# print(f"average = int({sum/tel})")

# klinkers = ['a', 'e', 'i', 'o', 'u']
#
# print(klinkers.index('m'))


# def process_list(list_of_lists):
#     new_list = []
#     for sub_list in list_of_lists:
#         for item in sub_list:
#             new_list.append(item.capitalize())
#     return new_list
#
#
# super_list = [["duck", "cat", "monkey"], [
#     "flower",  "tree", "bush"], ["whale", "swordfish", "shark"]]
# processed_list = process_list(super_list)
#
# print(processed_list)

# brands = ["Playstation", "Nitendo", "Xbox"]
# teller = 0
# while teller < len(brands):
#     if len(brands[teller]) > 5:
#         print(brands[teller])
#     else:
#         print("Dat is een korte naam...")
#
#     teller = teller + 1

# total = """sdfsdf
#
# sdfsdf
# """
#
# print(total)

# bytes = [0, 1, 1, 1, 0, 1, 0, 1]
# for s in bytes:
#     if s == 0:
#         continue
#     print(s)


# bytes = [0, 1, 1, 1, 0, 1, 0, 1]
# for s in bytes:
#     if s == 1:
#         break
#     print(s)
# import math
#
#
# def volume(radius, height=1.5):
#     return math.pi * radius ** 2 * height
#
#
# print(volume(10, 1.5))
# import numpy as np
#
# count = np.array([6, 4, 1.0, 6, 100])
#
# print(type(count))

# output = []
# saturation = [2, 5, -1, 41, 21, 9, -5]
#
# for s in saturation:
#     if s > 0:
#         continue
#     output.append(s)
#
# print(output)


# sudoku_region = [[1, 9, 7], [8, 5, 4], [8, 6, 2]]
# print(sudoku_region[1][2])

# import numpy as np
# array = np.array([])
#
# print(array)
# for i in range(10):
#     array = np.insert(array, 2*i, 6-i)
#
# print(array)


# list = [0, 1, 3]
# for i in range(0, 13):
#     print(i)
