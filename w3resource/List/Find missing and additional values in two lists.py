list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
print('Missing values in second list: ', set(list1) - set(list2))
print('Additional values in second list: ',set(list2) - set(list1) )