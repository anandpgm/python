
color_dict = {'red':'#FF0000', 'green':'#008000', 'black':'#000000', 'white':'#FFFFFF'}
for i in sorted(color_dict.keys()):
   print(i, color_dict[i])

# or

result = sorted(color_dict.items())
print(result)