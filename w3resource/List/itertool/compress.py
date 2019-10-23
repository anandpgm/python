# itertools.compress(data, selectors)
import itertools
shapes = ['circle', 'triangle', 'square', 'pentagon']
selections = [True, False, True, True]
result = itertools.compress(shapes, selections)
for each in result:
    print(each)