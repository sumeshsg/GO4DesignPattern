# what actually happens is that the new default list is created only once when the function is defined,
# and that same list is then used subsequently
# This is because expressions in default arguments are calculated when the function is defined, not when it’s called
def extend_list(val, def_list=[]):
    def_list.append(val)
    return def_list


list_1 = extend_list(10)
list_2 = extend_list(123, def_list=[])
list_3 = extend_list('a')

print(list_1)
print(list_2)
print(list_3)



