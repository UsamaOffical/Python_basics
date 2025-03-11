_list = []

for i in range(1,11):
    _list.append(i ** 2)
# print(_list)

#      experision    looping            condition
sqaure = [ i ** 2 for i in range(1,11) if i%2 == 0] # compact method
print(sqaure)