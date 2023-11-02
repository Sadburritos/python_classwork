import random

def random_number_generator(min, max):
    while True:
        yield random.randint(min, max)


generator = random_number_generator(1, 100)
for i in range(10):
    print(next(generator))
