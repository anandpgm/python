'''
 Write a Python program to create a dictionary from a string.

Note: Track the count of the letters from the string.
'''
from collections import defaultdict, Counter
str1 = 'w3resource'
mod = Counter(str1)
print(dict(mod))
