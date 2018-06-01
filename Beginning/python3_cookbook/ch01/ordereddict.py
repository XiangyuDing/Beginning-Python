from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 6
d['spam'] = 3
d['grok'] = 4
print(d)

e = {}
e['foo'] = 1
e['bar'] = 6
e['spam'] = 3
e['grok'] = 4
print(e)

for key in d:
    print(key, d[key])
