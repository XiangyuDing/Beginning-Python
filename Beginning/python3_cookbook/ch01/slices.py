items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2,4)
print(items[2:4])
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)

a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

s = 'HelloWorld'
print(a.indices(len(s))) # shrink start and stop into a workable range
for i in range(*a.indices(len(s))):
    print(s[i])
