# Find the list of words that are longer than n from a given list of words


def myfun(n,str):
    str_list = str.split(" ")
    for i in str_list:
        if len(i) > n:
            print(i)


myfun(2,"This is my input string")