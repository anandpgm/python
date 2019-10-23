def myfun(li,min,max):
    ctr = 0
    for i in li:
        if i >= min and i <= max:
            ctr += 1
    return ctr



a = [10,20,30,40,50,60,70,80,90]
print(myfun(a,20,80))