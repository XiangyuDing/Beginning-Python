# 2.7 最短匹配模式

import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says"no." Phone says "yes."'
print(str_pat.findall(text2))

str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
