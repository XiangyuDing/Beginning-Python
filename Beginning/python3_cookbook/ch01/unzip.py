# decompression of object
p = (4,5)
x, y = p
print(x)
print(y)
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(date)
name, shares, price, (year, mon, day) = data
print(year)
print(mon)
print(day)
##p = (4,5)
##x, y, z = p

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1222')
name, email, *phone_numbers = record
print(phone_numbers)
