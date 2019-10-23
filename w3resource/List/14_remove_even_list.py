#Write a Python program to print the numbers of a specified list after removing even numbers from it.

a = [2,4,3,67]
shuff
b = []

for i, j in enumerate(a):
    if j % 2 != 0:
        b.append(j)

print(b)

