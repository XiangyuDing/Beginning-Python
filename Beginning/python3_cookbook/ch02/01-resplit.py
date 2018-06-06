# 2.1 使用多个界定符分割字符串
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print(re.split(r'[;,\s]\s*', line))

fields = re.split(r'(;|,|\s)\s*',line)
print(fields)

values = fields[::2]
delimters = fields[1::2] + ['']
print(values)
print(delimters)
# Reform the line using the same delimiters
print(''.join(v+d for v,d in zip(values, delimters)))
print(re.split(r'(?:,|;|\s)\s*',line))
