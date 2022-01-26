from Functions import di

"""
в блок try вносятся только те строки которые могут дать ошибку
блок try минимальный
в блок try как можно меньше строк

если могут быть разные ошибки лучше сделать несколько try
"""

try:
    2/0
except SyntaxError as err:
    print(err, "1")
except ZeroDivisionError as err:
    print(err, "2")

try:
    print(_str)
except:
    print("an error ocured")

a = 3
b = 0
try:
    print(a/b)
except ZeroDivisionError as err:
    print(err)

a = "3.23"

try:
    c = int(a)
except ValueError:
    print(help(ValueError.__traceback__))

str_ = "Hello, World!"
try:
    print(str_)
except:
    print("something went wrong")
else:
    print("Nothing went wrong")
