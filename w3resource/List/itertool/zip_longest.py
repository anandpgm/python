'''

itertools.zip_longest(*iterables, fillvalue=None)
This function makes an iterator that aggregates elements from each of the iterables.
If the iterables are of uneven length, missing values are filled-in with fillvalue.
Iteration continues until the longest iterable is exhausted.
'''

import itertools
colors = ['red', 'orange', 'yellow', 'green', 'blue',]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
for each in itertools.zip_longest(colors, data, fillvalue=None):
    print(each)