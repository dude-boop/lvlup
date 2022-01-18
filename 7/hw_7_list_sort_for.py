
"""
task 1
    Рассмотреть метод sort
"""
list_hw_7_for_sort = ["lsblk", "cat/proc/cpuinfo", "blkid", "grep", "mount"]
print(list_hw_7_for_sort)
list_hw_7_for_sort.sort()
print(list_hw_7_for_sort)

list_hw_7_for_sort.sort(reverse = True)
print(list_hw_7_for_sort)
#
def myfunc(n):                          # не нашел применение
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#
# case sensitive
list_hw_7_for_sort = ["Virgo", "gemini", "leo", "tourus", "aquarus", "Sageterus"]
list_hw_7_for_sort.sort()
print(list_hw_7_for_sort)
#
# case ignor if add the function
list_hw_7_for_sort.sort(key = str.lower)
print(list_hw_7_for_sort)

list_hw_7_for_sort.reverse()
print(list_hw_7_for_sort)

"""
task 2
    Реализовать копирование списков через “spred” оператор, и конструктор list() проверить id
"""
some_list = [4, 6, 8, 63, 345, 25, 235, ]
another_list = [*some_list]
print(id(another_list))
print(id(some_list))
print(id(some_list[2]))
print(id(another_list[2]))

"""
task 3
    Задана строка “sdhfueiyr37456328579efhigrh4uty44ty73hfwekjfherouty298r23fh’aQWFHWE;” 
    создать список которий содержит только цифри.
"""
string_hw_7_to_take_the_numeric = "sdhfueiyr37456328579efhigrh4uty44ty73hfwekjfherouty298r23fh’aQWFHWE;"

if_numeric_list = []
for j in string_hw_7_to_take_the_numeric:
    if j.isdigit():
        if_numeric_list.append(j)
print(if_numeric_list)
# list comprehension
if_numeric_list =[j for j in string_hw_7_to_take_the_numeric if j.isdigit()]

"""
task 4
    Зада список [121, 544, 111, 99, 77] создать список элементи которого деляться на 11.
"""
list_for_chech_the_numbers = [121, 544, 111, 99, 77]
list_for_numbers_devided_on_11 = [j for j in list_for_chech_the_numbers if j%11 == 0]
print(list_for_numbers_devided_on_11)

"""
task 5
    Имеетс я начальный список цен на изделия. Сегодня на них дана скидка 10 %. 
    Составить новый с учетом удешевления стоимости.
"""
lst_day_prices = [4999, 70000, 86000, 429000, 302000, 21000]
today_prices_with_10_persents_discount = [j*0.9 for j in lst_day_prices]
print(today_prices_with_10_persents_discount)

"""
task 6
    Задан список фруктов ['apple', ‘pear’, 'banana', 'melon', 'pineapple'] создать список если слово начинаеться букви “р”, 
    добавить до слова “my ”. Нужно получить такой список ['my pear', 'my pineapple'].
"""
list_with_fruits = ['apple', 'pear', 'banana', 'melon', 'pineapple']
list_with_added_word_my = [f"my {fruit}" for fruit in list_with_fruits if fruit.startswith("p")]
print(list_with_added_word_my)
