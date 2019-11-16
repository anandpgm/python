# Map two lists into a dictionary
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
result = dict(zip(keys,values))
print(result)