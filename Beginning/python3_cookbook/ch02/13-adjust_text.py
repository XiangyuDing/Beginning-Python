# 2.13 字符串对齐

text = 'Hello World'
left = text.ljust(20)
right = text.rjust(20)
center = text.center(20)
print(left)
print(right)
print(center)
right = text.rjust(20,'=')
print(right)
center = text.center(20,'*')
print(center)

print(format(text,'>20'))
print(format(text,'<20'))
print(format(text,'^20'))
print(format(text,'=>20s'))
print(format(text,'*^20s'))

print('{:>10s}{:>10s}'.format('Hello','World'))
x = 1.2345
print(format(x,'>10'))
print(format(x,'^10.2f'))
print('%-20s' % text)
print('%20s' % text)

# https://docs.python.org/3/library/string.html#formatspec
