# itertools.count(start=0, step=1)
import itertools
for i in itertools.count(2,3):
    print(i)
    if i > 20:
        break