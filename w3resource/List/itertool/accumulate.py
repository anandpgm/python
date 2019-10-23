import itertools
import operator

#accumate function

a = [1,2,3,4,5]
result = itertools.accumulate(a, operator.mul)
for i in result:
    print(i)
"""
operator.mul(1, 2)
2
operator.mul(2, 3)
6
operator.mul(6, 4)
24
operator.mul(24, 5)
120
"""

print("==============")
a = [5, 2, 6, 4, 5, 9, 1]
result = itertools.accumulate(a, max)
for i in result:
    print(i)

print("==============")