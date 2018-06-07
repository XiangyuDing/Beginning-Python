# 2.2 字符串开头或结尾匹配

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))

filenames = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
print([name for name in filenames if name.endswith(('.c','.h'))])
print(any(name.endswith('.py') for name in filenames))

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['http:','ftp:']
url = 'http://www.python.org'
# print(url.startswith(choices))
print(url.startswith(tuple(choices)))

filename = 'spam.txt'
print(filename[-4:] == '.txt')
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

import re
url = 'http://www.python.org'
print(re.match('http:|https:|ftp:',url))
