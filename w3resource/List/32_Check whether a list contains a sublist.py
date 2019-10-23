def myfun(master,sub):
    first = sub[0]
    second = sub[1]
    result = "not Present"
    for index, value in enumerate(master):
        if value == first and second == master[index + 1]:
            result = "present"
    print(result)
a = [1,4,6,4,2,4,5]
check = [4,4]
myfun(a,check)