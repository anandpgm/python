
color_dict = {'red':'#FF0000', 'green':'#008000', 'black':'#000000', 'white':'#FFFFFF'}
for i in sorted(color_dict.keys()):
   print(i, color_dict[i])

# or

result = sorted(color_dict.items())
print(result)

'''
Sorting list of dictionaries 
Having a knowledge to sort dictionaries according to its values can prove useful in such cases.
There are 2 ways to achieve this sorting, namely by

    Using lambda functions
    Using itemgetter

'''
# Initializing list of dictionaries
lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

# Using lambda
print("The list printed sorting by age: ")
print(sorted(lis, key = lambda i: i['age']))

print("The list printed sorting by age and name: ")
print(sorted(lis, key = lambda i: (i['age'], i['name'])))

#using itemgetter
from operator import itemgetter
print("The list printed sorting by age: ")
print(sorted(lis, key = itemgetter('age')))

print("The list printed sorting by age and name: ")
print(sorted(lis, key = itemgetter('age', 'name')))