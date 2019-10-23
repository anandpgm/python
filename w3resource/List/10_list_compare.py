#Takes two lists and returns True if they have at least one common member

def list_compare(a,b):
    result = False
    for i in a:
        for j in b:
            if i == j:
                result = True
                break
    print(result)

list_compare(['a','b','c'],['a','e','f'])