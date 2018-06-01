# delete duplicate elements in hashable object
def dedupe(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(dedupe(a))

# delete duplicate elements in non-hashable object
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

b = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(b, key=lambda d: (d['x'], d['y']))))
print(list(dedupe(b, key=lambda d: d['x'])))

print(set(a))
