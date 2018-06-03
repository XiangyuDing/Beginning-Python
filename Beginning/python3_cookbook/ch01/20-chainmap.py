# 1.20 合并多个字典或映射

a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

from collections import ChainMap
c = ChainMap(a,b)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)

print(len(c))
print(list(c.keys()))
print(list(c.values()))
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
##del c['y']
##print(c)

values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
# Discard last mapping
values = values.parents
print(values['x'])
# Discard last mapping
values = values.parents
print(values['x'])
print(values)

a = {'x':1, 'z':3}
b = {'y':2, 'z':4}
merged = dict(b)
merged.update(a)
print(merged['x'], merged['y'], merged['z'])
a['x'] = 13
print(merged['x'])

a = {'x':1, 'z':3}
b = {'y':2, 'z':4}
merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 42
print(merged['x']) # Notice change to merged dicts
