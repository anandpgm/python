import itertools
import operator
shapes = ['circle', 'triangle', 'square',]
result = itertools.combinations(shapes, 2)
for i in result:
    print(i)