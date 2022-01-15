# fruits = ['apple', 'banana', 'cherry', 'cherry', 'pineapple']
# doble = []
# difs = []
# for fruit in fruits:
#     if fruit in doble:
#         doble.append(fruit)
#     else:
#         difs.append(fruit)
# for dif in set(difs):
#     print(fruits.count(dif))

# list_1 = [1,4,65,8567,2,34,6]
# list_1.clear()
# print(dir(list_1))

# копирование списка
# с помощью среза
fruits = ['apple', 'banana', 'cherry', 'cherry', 'pineapple', {1,2,3}, {1:2, 2:3, 3:4}, [1,2,3,4,5,6,7]]

# fr = fruits
# print("id fr:         ", id(fr))
# print("id fruits:     ", id(fruits))
#
# fr = fruits[:]
# print("id fr :        ", id(fr))
# print("id fruits [:]: ", id(fruits))
#
# fruits.append("cherry")
# print("fruits:",fruits)
# print("fr    :",fr)

# с помощью метода списка copy
# fr = fruits.copy()
# print("id fr:         ", id(fr))
# print("id fruits:     ", id(fruits))

#
# from copy import copy, deepcopy
# fr = copy(fruits)
# print("id fr_copy:         ", id(fr))
# print("id fruits:          ", id(fruits))
# print("id fr_copy[5]:      ", id(fr[5]))
# print("id fruits[5]:       ", id(fruits[5]))
# print("id fr_copy[6][1]:      ", id(fr[6][1]))
# print("id fruits[6][1]:       ", id(fruits[6][1]))
#
# fr = deepcopy(fruits)
# print("\n","id fr_deep:         ", id(fr))
# print("id fruits:          ", id(fruits))
# print("id fr_deep[5]:      ", id(fr[5]))
# print("id fruits[5]:       ", id(fruits[5]))
# print("id fr_deep[6][1]:      ", id(fr[6][1]))
# print("id fruits[6][1]:       ", id(fruits[6][1]))

# две формы записи
res = []
for i in range(1,100,2):
    if i % 2 == 0:
        res.append(i**2)  # в соучае List Comprehension отказываемся от метода .append
#List Comprehension
res = [i**2 for i in range(1,100,2) if i % 2 == 0]

bad_lists = ['Adobe', 'Audience', 'Manager', 'Ds', 'This','There', 'These']
filter_list = ['This', 'Ds', 'There', 'These']
result_list = [i for i in bad_lists if i not in filter_list]












