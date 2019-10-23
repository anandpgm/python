# This function makes an iterator that filters elements from iterable returning only those for which the predicate is False
import itertools
a = [1,2,3,4,5,6,7,8,9,3]
result = itertools.filterfalse(lambda x: x<5, a)

for i in result:
    print(i)