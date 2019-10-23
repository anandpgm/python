#Print a list after removing specified elements

my_list = ['apple', 'orange','mango','banana','rice']

for counter, value in enumerate(my_list):
    print(counter,value)
for counter, value in enumerate(my_list):
    if counter in (0,3,4):
        print(value)