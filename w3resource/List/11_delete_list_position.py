#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
a = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

for i, j in enumerate(a):
    if i in (0,4,5):
       a.remove(a[i])

print(a)
