# Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

s = "anand"
print((set(s)))
new = set(s)
dict1 = {}
for i in new:
    dict1[i] = s.count(i)
print(dict1)

