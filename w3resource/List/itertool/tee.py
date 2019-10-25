# Return n independent iterators from a single iterable.   itertools.tee(iterable, n=2)

import itertools
colors = ['red', 'orange', 'yellow', 'green', 'blue']
alpha_colors, beta_colors = itertools.tee(colors)
for each in alpha_colors:
    print(each)
print('..')
for each in beta_colors:
    print(each)