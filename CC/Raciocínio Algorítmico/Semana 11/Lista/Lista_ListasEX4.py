import random

num = []

for i in range(0, 10):
    num.append(random.randint(0,100))
print(sorted(num, reverse = True))