# 3.11 随机选择

import random
values = [1,2,3,4,5,6]
for i in range(0, 4):
    print(random.choice(values))
for i in range(0, 4):
    print(random.sample(values, 2))
random.shuffle(values)
print(values)
for i in range(0, 10):
    print(random.randint(0, 10))
for i in range(0, 3):
    print(random.random())
print(random.getrandbits(200))

random.seed() # Seed based on system time or os.urandom()
random.seed(12345) # Seed based on integer given
random.seed(b'bytedata') # Seed based on byte data
