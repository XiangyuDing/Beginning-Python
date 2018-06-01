prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

print(min(prices.values()))
print(max(prices.values()))

print(min(prices, key=lambda k:prices[k]))
print(max(prices, key=lambda k:prices[k]))

prices2 = {'AAA': 45.23, 'ZZZ': 45.23}
print(min(zip(prices2.values(), prices2.keys())))
print(max(zip(prices2.values(), prices2.keys())))

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}
# find keys in common
res1 = a.keys() & b.keys()
print(res1)
# find keys in a which are not in b
res2 = a.keys() - b.keys()
print(res2)
# find (key,value) pairs in common
res3 = a.items() & b.items()
print(res3)
# make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z','w'}}
print(c)
