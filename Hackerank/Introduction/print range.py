'''
Read an integer N

Without using any string methods, try to print the following:

123...N
'''

if __name__ == '__main__':
    n = int(input('Enter the number: '))
    # for i in range (1,n+1):
    #     print(i, end="")
    print(*range(1,n+1), sep ='')