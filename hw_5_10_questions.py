"""
задача1
    Из двух случайных чисел, одно из которых четное,
    а другое нечетное, определить и вывести на экран нечетное число.
"""

# num_1 = int(input("please enter the even number: "))
# num_2 = int(input("please enter the not an even number: "))
# if num_1 == 0 or num_2 == 0:
#     print("invalid input, please try again")
# else:
#     if num_1 % 2 == 0:
#         print(num_1)
#     else:
#         print(num_2)
"""
задача2
    Вводятся три разных числа. Найти, какое из них 
    является средним (больше одного, но меньше другого).
"""

# three_numbers  = []
# three_numbers.append(int(input("please enter the first number: ")))
# three_numbers.append(int(input("please enter next number: ")))
# three_numbers.append(int(input("please enter the last number: ")))
# three_numbers.sort()
# print("your number in the middle is: ", three_numbers[1])

"""
задача3
    Вводятся координаты (x; y) точки и радиус круга (r).
    Определить принадлежит ли данная точка кругу, если его центр находится в начале координат.
"""

# x_coordinates = int(input("X: "))
# y_coordinates = int(input("Y: "))
# rad_of_cyrcle = int(input("Radius: "))
# abs_rad_of_cyrcle = abs(rad_of_cyrcle)
#
# if x_coordinates > abs_rad_of_cyrcle or y_coordinates > abs_rad_of_cyrcle:
#     print("your POINT is OUT side the cyrcle")
# else:
#     print("your POINT is IN side the cyrcle")

"""
задача5
    Вводятся три целых числа. Определить какое из них наибольшее.
"""

# biggest_of_the_numbers  = []
# biggest_of_the_numbers.append(int(input("please enter the first number: ")))
# biggest_of_the_numbers.append(int(input("please enter next number: ")))
# biggest_of_the_numbers.append(int(input("please enter the last number: ")))
# biggest_of_the_numbers.sort()
# print("your BIGGEST number is: ", biggest_of_the_numbers[-1])

#######################################################################################################################№
#=======================================================================================================================
# пока не понял механику, проверка треугольеиков по градусам углов, я думаю...
"""
задача6 -- ############# прочитать геометрию
    По длинам трех отрезков, введенных пользователем, 
    определить возможность существования треугольника, 
    составленного из этих отрезков. Если такой треугольник существует, 
    то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

# first_segment_ab = int(input("please enter the length of the first segment"))
# second_segment_bc = int(input("please enter the length of the second segment"))
# third_segment_ca = int(input("please enter the length of the third segment"))
#======================================================================================================================
#######################################################################################################################
"""
задача7
    Определить четверть координатной плоскости, 
    которой принадлежит точка. Координаты точки ввести с клавиатуры.
"""

# x_coord_of_point = int(input("X: "))
# y_coord_of_point = int(input("Y: "))
#
# if x_coord_of_point > 0 and y_coord_of_point > 0:
#     print("I")
# elif x_coord_of_point < 0 and y_coord_of_point > 0:
#     print("II")
# elif x_coord_of_point < 0 and y_coord_of_point < 0:
#     print("III")
# elif x_coord_of_point > 0 and y_coord_of_point < 0:
#     print("IV")
# else:
#     print("please try again")

"""
задача8
    Вводятся два целых числа. Проверить делится ли первое на второе. 
    Вывести на экран сообщение об этом, а также остаток (если он есть) и частное (в любом случае).
"""

# first_integer_number = int(input("enter the first integer number: "))
# second_integer_number = int(input("enter the second integer number: "))
#
# if second_integer_number == 0:
#     print("the number is not divisible")
# else:
#     print("the number is divisible")
#     if first_integer_number%second_integer_number == 0:
#         print(f"{first_integer_number} / {second_integer_number} = {first_integer_number // second_integer_number}")
#     else:
#         print(f"{first_integer_number} / {second_integer_number} = {first_integer_number // second_integer_number},{first_integer_number % second_integer_number}")

"""
задача 9
    Заданы строковые обэкты ”””
      File "leveleUp.py", line 34
        tem = 5 if current_temperature >= 5
                                          ^
    SyntaxError: invalid syntax
    ”””
    и
    ”””
    Traceback (most recent call last):
      File "leveleUp.py", line 18, in <module>
        print("current_temperature: ---------", current_temperature, f"Type is: ----- {type(current_temperature)}")
    NameError: name 'current_temperature' is not defined
    ”””
    
    Если тип ошибки SyntaxError, Заменить последнюю строку любим другим сообщением.
"""

## здесь я меняю выхлоп ошибки с SyntaxError: invalid syntax ==>  NameError: name 'num2' is not defined
current_temperature = 1
tem = 5 if current_temperature >= 5 else num2

## здесь я убираю ошибку
tem = 5 if current_temperature >= 5 else 3




"""
Задача 10
    Повторить все методи строкових обектов
"""

#в файле hw_5_task_10