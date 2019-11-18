'''
Write a Python program to remove the nth index character from a nonempty string
'''

def remove_char(s,n):
    return ((s[:n] + s[n+1:]))

print(remove_char("anand", 2))
print(remove_char("hello world", 8))
