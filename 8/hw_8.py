from Functions import di
"""
task 1
    Задан некоторый список A содержащий целые числа.
    Используя инструкцию while разработать программу,
    которая вычисляет сумму элементов списка.
"""
a = [number for number in range(2,100,2)]
counter = 0
lens_of_numbers_list = len(a)
sum = 0
while counter < lens_of_numbers_list:
    sum += a[counter]
    counter += 1
print(f"сумма всех элеменьов списка: {sum}")

"""
task 2
    Задано число a (1<a<1.5). Из чисел 1+1/2, 1+1/3, 1+1/4 …,
    напечатать те, которые не меньше a
"""

"""
task 3
    Задан список строк. В каждой строке подсчитать 
    количество вхождений заданного любого символа
"""

list_hw_8_with_strings = ["jnbfg", "sdkfjds", "sldfjk", "sdkbohjgpid"]
some_letter = "b"
line = 0
lens_of_list_with_strings = len(list_hw_8_with_strings)
start = 0
stop = (len(list_hw_8_with_strings))
while start < stop:
    print(f"в строке {line} {list_hw_8_with_strings[start].count(some_letter)} символов {some_letter}")
    start += 1
    line += 1

"""
task 4 
Пользователь вводит число. Определение наличия заданного элемента в списке
list_=[2,8,3,4,3,5,2,1,0,3,4,4,5,8,7,7,5]. Если элемент не найден,
то выводится соответствующее сообщение.
"""

list_=[2,8,3,4,3,5,2,1,0,3,4,4,5,8,7,7,5]
user_type = int(input("Введите число для проверки: "))
if user_type in list_:
    print(user_type)

"""
task 5
Рассмотреть методи тюплов из пространства импен.
"""
tp = 2,
print(di(tp))
print(tp.count(2))
print(tp.index(2))














