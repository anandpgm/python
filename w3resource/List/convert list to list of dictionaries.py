list1 = ['name','age']
list2 = ['anand',30]

print("First list is", str(list1))
print("Second list is", str(list2))
result = {list1[i]: list2[i] for i in range(len(list1))}
print("Result dict is", str(result))

"""
Another pgm 

["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
"""
color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
for f,c in zip(color_name,color_code):
    print(f)
    print(c)
print([{'colour_name':f, 'clour_code':c } for f,c in zip(color_name,color_code)])

