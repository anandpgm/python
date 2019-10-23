def sumlist(my_list=[], *args):
    sum = 0
    for i in my_list:
        sum = sum + i
    print(sum)


input = [1, 2, 3, 4]
sumlist(input)

# def sum_list(items):
#     sum_numbers = 0
#     for x in items:
#         sum_numbers += x
#     return sum_numbers
# print(sum_list([1,2,-8]))