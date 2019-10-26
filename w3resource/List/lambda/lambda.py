'''
A lambda operator can have any number of arguments but can have only one expression.
It cannot contain any statements and returns a function object which can be assigned to any variable.
lambda arguments : expression
'''


def add(x, y):
    return x + y


# Call the function
add(2, 3)  # Output: 5

new = lambda x, y: x + y
#print(result)
print(new(2, 3))  # Output: 5