'''
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
'''

s1 = 'abc'
s2 = 'xyz'
new1 = s1[:2]
new2 = s2[:2]
print(new2 + s1[2::], new1 + s2[2::])
