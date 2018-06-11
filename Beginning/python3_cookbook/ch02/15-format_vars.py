# 2.15 字符串中插入变量

s = '{name} has {n} messages.'
print(s.format(name = 'Guido',n=37))

name = 'Guido'
n = 37
print(s.format_map(vars()))

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
a = Info('Guido',37)
print(s.format_map(vars(a)))

# s.format(name='Guido')
class safesub(dict):
    # prevent lost key
    def __missing__(self, key):
        return '{' + key + '}'
del n # Make sure n is undefined
print(s.format_map(safesub(vars())))

import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You favorite color is {color}'))

# print('%(name) has %(n) messages.' % vars()) doesn't work
import string
s = string.Template('$name has $n messages.')
print(s.substitute(vars()))
