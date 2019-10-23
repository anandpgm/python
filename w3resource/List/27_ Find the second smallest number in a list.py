a = [0,0,45,31,0]
a.sort()
print(a)

result = a[1]

j = 1
while a[0] == a[j]:
    j = j + 1
    result = a[j]

print(result)
