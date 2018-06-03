# 1.19 转换并同时计算数据

nums = [1,2,3,4,5]
s = sum(x * x for x in nums)
print(s)

# Determine if any .py files exist in a directory
##import os
##files = os.listdir('dirname')
##if any(name.endswith('.py') for name in files):
##    print('There be python!')
##else:
##    print('Sorry, no python.')
# Output a tuple as CSV
s = ('ACME',50,123.45)
print(','.join(str(x) for x in s))
# Data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares1 = min(s['shares'] for s in portfolio)
min_shares2 = min(portfolio, key=lambda s:s['shares'])
print(min_shares1)
print(min_shares2)
