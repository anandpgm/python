'''
Program that accept an integer (n) and computes the value of n+nn+nnn....
'''

num = input('Enter the number: ')

n1 = int(num)
n2 = int("%s%s" % (num,num))
n3 = int("%s%s%s" % (num,num,num))
print(n1, "", n2, "", n3)
print("Sum is", (n1+n2+n3))