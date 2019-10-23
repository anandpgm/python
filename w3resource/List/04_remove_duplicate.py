def duplicate(my_list):
    final_list = []
    for num in my_list:
        if num not in final_list:
            final_list.append(num)
    return (final_list)


myinput = [1,2,3,1,4]
print(duplicate(myinput))