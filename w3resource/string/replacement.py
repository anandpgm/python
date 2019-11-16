'''
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
'''

str1 = 'The lyrics is not that poor!'
index1 = str1.find('not')
index2 = str1.find('poor')
if index1 < index2:
   print(str1[:index1] + 'poor')
else:
   print(str1.replace('good', 'poor'))


