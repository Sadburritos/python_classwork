import math

user_catan1 = input("Введите катет 1 ")
user_catan2 = input("Введите катет 2 ")

try:
    cat1 = int(user_catan1)
    cat2 = int(user_catan2)


except ValueError:
    massage = "Error"
else:
    cat1 **= 2
    cat2 **= 2

    cat_sum = cat1 + cat2
    massage = cat_sum ** 0.5

print(massage)
