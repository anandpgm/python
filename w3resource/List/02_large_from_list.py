# Find a large number from a list

def count(items):
    result = 0
    for i in items:
        print(i)
        if len(i) > 2 and i[1:] eq i[:-1]:
            result = result + 1
    print(result)


input = ['aba','abcd','cac', 'bb']
# print(input)
