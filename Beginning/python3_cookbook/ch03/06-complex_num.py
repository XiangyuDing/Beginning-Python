# 3.6 复数的数学运算

a = complex(2, 4)
b = 3 -5j
print(a)
print(b)

print(a.real)
print(a.imag)
print(a.conjugate())

print(a + b)
print(a * b)
print(a / b)
print(abs(a))

import cmath
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

import math
#print(math.sqrt(-1))
print(cmath.sqrt(-1))
