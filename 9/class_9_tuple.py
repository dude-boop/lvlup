from Functions import di
## возможность дупликации
fruits = ("banana", "cherry", "apple", "banana", "cherry")
print("fruits: ", fruits)
## тип данных может быть любой
tuple1 = ("abc", 34, True, 40.9, "male", None, [1, 3, 4])
print("tuple1: ", tuple1)

def some_func(a, b):
    return a, b

def new_func(a):
    b = 2
    c = 3
    return a, b, c

print(list(some_func("a","b")))

t = 2
print(type(t))
t = 2,
print(type(t))
t = (2,)
print(type(t))

print(di(new_func("1")))

# упаковка элементов кортежа
some_tuple = ("foo", "bar", "baz", "qux",)
(s1, s2, s3, s4, ) = some_tuple

# args
fruits = ("apple", "banana", "cherry", "apple", "banana", "cherry")
(green, yellow, *red) = fruits
print(green, yellow, red)

## получается генератор, а кортежа не получается
tc = (i*2 for i in (1, 2, 3,))
print('tc: ', tc)
## что бы все получилось нужно делать через КОНСТРУКТОР tuple()
tc = tuple(i*2 for i in (1, 2, 3,))
print('tc: ', tc)

