# 2.20 字节字符串上的字符串操作

data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

data = b'FOO:BAR,SPAM'
import re
# print(re.split('[:,]',data))
print(re.split(b'[:,]',data)) # Notice: pattern as bytes

a = 'Hello World' # Text string
print(a[0])
print(a[1])
b = b'Hello World'
print(b[0])
print(b[1])

s = b'Hello World'
print(s) # Observe b'...'
print(s.decode('ascii'))
print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))

# Write a UTF-8 filename
# Get a directory listing
