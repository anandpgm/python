
name_list = ['anand','athira','adhvik']
age     = [30,27,2]
result = list(zip(name_list, age))
print(result)

#unzipping

unzip_name, unzip_age = zip(*result)
print(unzip_age)
print(unzip_name)