from random import *
a = 10,20

def get_random_int(max, min):
    result = random() * (max - min)
    result += min
    return int(result)

num = get_random_int(15,20)
print(num)