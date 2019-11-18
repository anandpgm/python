# Remove the characters which have odd index values of a given string

def remove(s1):
   result = ""
   for i in range(len(s1)):
       if i % 2 == 0:
          result = result + s1[i]
   print(result)



remove('abcdefg')