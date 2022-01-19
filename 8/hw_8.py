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
print(sum)

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

list_hw_8_with_strings = ["jnfg", "sdkfjds", "sldfjk", "sdkbohjgpid"]
some_letter = "b"
lens_of_list_with_strings = len(list_hw_8_with_strings)
counter = 0
