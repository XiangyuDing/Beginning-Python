d = {
    'a': [1,2,3]
    'b': [4,5]
    }
e = {
    'a':{1,2,3}
    'b':{4,5}
    }

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(4)

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
