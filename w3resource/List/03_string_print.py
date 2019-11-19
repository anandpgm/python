'''
Write a Python program to count the number of strings where the string length is 2 or more and
the first and last character are same from a given list of strings
'''
def sumlist(my_list=[], *args):
    count = 0
    for i in my_list:
        if len(i) > 2 and i[0] == i[-1]:
            count += 1
    print(count)



input = ['abc', 'aba', '121', '2552', 'aa', 'ana']
sumlist(input)