# 2.14 合并拼接字符串

parts = ['Is','Chicago','Not','Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))
a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)
print('{} {}'.format(a,b))
print(a + ' ' + b)
a = 'Hello' 'World'
print(a)

data = ['ACME',50,91.1]
print(','.join(str(d) for d in data))
# Version 1 (string concatenation, when string is small)
f.write(chunk1 + chunk2)
# Version 2 (separate I/O operations, when string is big)
f.write(chunk1)
f.write(chunk2)

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

text = ''.join(sample())

for part in sample():
    f.wirte(part)

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)

# combine with files operations
with open('filename','w') as f:
    for part in combine(sample(), 32768):
        f.wirte(part)
