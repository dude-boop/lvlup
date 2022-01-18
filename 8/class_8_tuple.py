tuple_dir = ()
print(dir(tuple_dir))

tuple_dir = ('2','3','5','10','44')
print(tuple_dir)
list_after_tuple_dir = [*tuple_dir]     #  разные способы
list_after_tuple_dir = list(tuple_dir)  #  перевода tuple в list
print(list_after_tuple_dir)
print(id(tuple_dir))
print(id(list_after_tuple_dir))

# отличие tuple от list
# tuple - не изменяемый, list - изменяемый
# работа с tuple должна быть быстрее чем с list
# dict один об'ект должен быть не изменяемый

# создание tuple
tp = (1, 2, 3,)    # после последнего аргумента ставить запятую, для удобства работы с текстом "горячими клавишами"
tp = 1,2,3,
print(type(tp),"\n",dir(tp))
show_you_dir_without_spaces = [obj for obj in dir(tp) if not obj.startswith("__")]
print(show_you_dir_without_spaces)

from Functions import di

print(di(tp))

tuple_dir = ('2','3','5','10','44')
list_after_tuple_dir = list(tuple_dir)
print(di(tuple_dir))
print(di(list_after_tuple_dir))

# tuple comprehension
tp = tuple(num for num in range(5,10)) # только через '... = tuple(...)', если пробовать через '... = (...) получим генератор

print(id(tp))
