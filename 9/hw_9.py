"""
task 1
Дано два списка
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
Создать из них список кортежей
list_c = [(1,5), (2,6), (3,7), (4,8)]

"""
list_c = []
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
for len_ in range(len(list_a)):
    tuple_ = list_a[len_],list_b[len_]
    list_c.append(tuple_)
print(list_c)

"""
taks 2
Дано список
["bar", "baz", "qux", "etc"]
Создать кортеж
("foo", "bar", "baz", "qux", "etc")

"""
some_list_fot_9_hw = ["bar", "baz", "qux", "etc"]
some_list_fot_9_hw.insert(0,"foo")
some_list_fot_9_hw = tuple(some_list_fot_9_hw)
print(some_list_fot_9_hw)

"""
task 3
Задано список my_list = (1, 2, 3, 4, 5)
Получите шестой єлемент списка. В случае его отсутствия 
видайте відайте сообщение о его отсутствии.

"""

my_list = [1, 2, 3, 4, 5]
try:
    print(my_list[6])
except IndexError:
    print("index `6` is not in list")