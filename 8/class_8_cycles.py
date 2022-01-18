# fruits = ['apple', 'banana', 'melon', 'pineaple', {1,2,3}, {1:2,2:3}]
# copy_fruits = [*fruits]

# While --
# list1 = ['1','2','s','g','a','3','4']
# i = 30
# ii = 0
# while ii<i:
#     print(ii)
#     ii+=1

text = 'Hello Worlds'
for letter in text:
    print(letter)

text = 'Hello Worlds'
for letter in text:
    print(letter)
# НЕ ПРАВИЛЬНО
yes = [2,35,6,7]
for i in yes:   # запись работать будет. Но! читаемости нет, не использовать переменные как "i"
    print(i)

# if __iter__ object is iter(итерируемый)
string_for_show_the_iter = ''
print(dir(string_for_show_the_iter))

# оператор continue
string_for_continue = "345678sdhfueiyr37456328579efhigrh4uty44ty73hfwekjfherouty298r23fh’aQWFHWE;99\n"
for letter in string_for_continue:
    if letter.isalpha():
        continue
    print(letter * 2, end='')

the_o_letter = 'o'
for letter in 'hello world':
    if letter == the_o_letter:
        break
else:
    print((f'буквы {the_o_letter} нет в этой итерации'))
