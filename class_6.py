# b = "hello world"
# a = b
# print('id b: ', id(b))
# print('id a: ', id(a))
# c = 1
# d = 2
# c,d = d,c
# print(c,d)
# print(b.index("h"))

"""
lists
"""

fruts = ["apple", "banana", "cherry"]
# print(fruts)
# fruts.append('pineapple')
# print(fruts)
# x = fruts.pop(-1)
# print(fruts, x)
#
# print(id(fruts))
# print(id(fruts[0]))
# print(id(fruts[1]))
# print(id(fruts[2]))
#
# # duplication
#
# fruts.append('banana')
#
# print(fruts, id(fruts[1]), id(fruts[3]))
# print(fruts.index('banana'))
# for frut in fruts:
#     print(frut)
# dfg = [1,2.3,"apple", [1,2,3], None, True, {1:2, 3:4}]
# print(dfg)
fruts.append('cherry')
fruts.append('pineapple')
print(fruts)
print(fruts[1:3])
if "apple" in fruts:
    print("apple is exist")
else:
    print("apple is not exist")
