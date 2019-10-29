import operator

prices = {'Apple': 1.99, 'Banana': 0.99, 'Orange': 1.49, 'Cantaloupe': 3.99, 'Grapes': 0.39}

sorted_d = sorted(prices.items())
new =  dict(sorted(prices.items(), key=operator.itemgetter(0)))
print(sorted_d)
print(new)


