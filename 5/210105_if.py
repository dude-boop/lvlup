## if else
# if 2 == 2 :
#     print('2=2')
# else:
#     print('2!=2')
## elif
# a = 3
# if 2 == a :
#     print('2=2')
# elif 3 == a:
#     print('3==3')
# else:
#     print('a!=2, a!=3')
## validator

# current_temperature = int(input('Enter the text please: '))
# if current_temperature >= 5:
#     print('you can dont wear the hat')
# else:
#     print('please whear the hat')

##

# current_temperature = int(input('Enter the text please: '))
# if current_temperature >= 5:
#     print('you do not must wear the hat')
# elif current_temperature <= 5:
#     print('please whear the hat')
# else:
#     print('do not go outside')

## тернарный оператор

# current_temperature = int(input('Enter the text please: '))

# print('больше 5-ти') if current_temperature >= 5 else print('меньше пяти')

##
# current_temperature = int(input('Enter the text please: '))
#
# tem = 5 if current_temperature >= 5 else 0
# print(tem)
## пространство имен

# stro = ''
# str_2 = ""
# # print(dir(stro))

## кавычки

# str_3 = 'hsbd fj ksdhf s kdfjh asdfjk hs adkjh' \
#     'asdkahjfjks sdjfkh sd f shjf jksh' \
#     'asd  asd sfd s df s'
# print(str_3)
#
# str_4 = '\nhsbd fj ksdhf s kdfjh asdfjk hs adkjh\n' \
#     'asdkahjfjks sdjfkh sd f shjf jksh\n' \
#     'asd  asd sfd s df s\n'
# print(str_4)
#
# str_5 = """hsbd fj ksdhf s kdfjh asdfjk hs adkjh
# asdkahjfjks sdjfkh sd f shjf jksh
# asd  asd sfd s df s"""
# print(str_5)

## Форматирование строк
age = 36
txt = "my name is John i am " + str(age)
txt1  = "my name is John i ma %s " %age
txt2 = f"my name is John i am {age}"
print(txt,txt1,txt2)
