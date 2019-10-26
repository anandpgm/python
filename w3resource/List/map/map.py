'''
map functions expect a function object and any number of iterables, such as list, dictionary, etc.
It executes the function_object for each element in the sequence and returns a list of the elements modified by the function object.
map(function_object, iterable1, iterable2,...)
'''

def multi(a):
    return a * 2

print(multi(4))

# map function

print(list((map(multi, [5]))))

print(list((map(lambda x: x *2, [6]))))

# Multpiple iterations
list_a = [1, 2, 3]
list_b = [10, 20, 30]

print(list(map(lambda x, y: x + y, list_a, list_b) ) )# Output: [11, 22, 33]