# Make an iterator that drops elements from the iterable as long as the predicate is true; afterwards, returns every element.( that's why 3 also printed

import itertools
a = [1,2,3,4,5,6,7,8,9,3]
result = itertools.dropwhile(lambda x: x<5, a)

for i in result:
    print(i)

print("=========")
def is_even(x):
    return x % 2 == 0


lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]
result = list(itertools.dropwhile(is_even, lst))

print(result)