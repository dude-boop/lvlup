### the home work exercise: try all the string methods

str_hw = "wdf ihb\tuufnn\tvj9876 0876"
# print(dir(str_hw))
"""
'capitalize', 'casefold', 'center', 'count', 'encode',
'endswith', 'expandtabs', 'find', 'format', 'format_map',
'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
'isdigit', 'isidentifier', 'islower', 'isnumeric',
'isprintable', 'isspace', 'istitle', 'isupper',
'join', 'ljust', 'lower', 'lstrip', 'maketrans',
'partition', 'replace', 'rfind', 'rindex', 'rjust',
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

"""
print(str_hw.capitalize())
print(str_hw.casefold())
print(str_hw.center(50, "-"))
print(str_hw.count("i"))
print(str_hw.encode(encoding="ascii",errors="xmlcharrefreplace")) # не понял
print(str_hw.endswith("76"))
print(str_hw.expandtabs(10))
str_hw = "wdf ihb\tuufnn\tvj9876 0876"
print(str_hw.find("i"))
print(str_hw.index("i"))
# format
print(str_hw.isalnum())
print(str_hw.isalpha())
print(str_hw.isdecimal()) # не понял
str_hw = "7634758290329487538929485"
print(str_hw.isdigit())
str_hw = "sadjfnj34857"
print(str_hw.isidentifier())
print(str_hw.islower())
str_hw = "45678"
print(str_hw.isnumeric())
str_hw = "\n sdf 94835"
print(str_hw.isprintable())
print(str_hw.isspace())
str_hw = "   "
print(str_hw.isspace())
str_hw = "Hello My Name Is Canser"
print(str_hw.istitle())
str_hw = "HELLO MY NAME IS CANSER"
print(str_hw.isupper())
list_hw = ["H", "E", "L", "L", "O"]
str_hw = "".join(list_hw)
print(str_hw)
str_hw = "hello"
str_hw_with_spaces = str_hw.ljust(10)
print(str_hw_with_spaces, "my name is canser")
str_hw_with_b_simbol = str_hw.ljust(10, "b")
print(str_hw_with_b_simbol, "my name is canser")
str_hw = "HELLO MY NAME IS CANSER"
str_hw = str_hw.lower()
print(str_hw)
print(str_hw.lstrip("hello"))  # .lstrip нифига не понял
x = str_hw.maketrans("h", "g") # .lstrip нифига не понял
print(str_hw.translate(x))     # .lstrip нифига не понял
str_hw_partition  = str_hw.partition("name")  # return the tuple
print(str_hw_partition)
str_hw_replace = str_hw.replace("hello", "good buy", 1)
print(str_hw_replace)
str_hw_rfind = str_hw.rfind("is")
print(str_hw_rfind)



