a = ['abc', 'xyz', 'aba', '1221']
count = 0
for i in a:
    limit = len(i) - 1
    #print(limit)
    #print(i[:1])
    #print(i[limit:])
    if i[:1] == i[limit:]:
        count = count +1
print(count)
