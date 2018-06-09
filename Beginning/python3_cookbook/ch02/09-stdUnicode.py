# 2.9 将Unicode文本标准化

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spice Jalapen\u0303o'
print(s1)
print(s2)
print(s1 == s2)
print(len(s1))
print(len(s2))

import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2) # False but in guidebook it should be True
print(ascii(t1))
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4) # False but in guidebook it should be True
print(ascii(t3))

s = '\ufb01' # A single character
print(s)
print(unicodedata.normalize('NFD', s))
# Notice how the combined letters are broken apart here
print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))

t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
