km_in = input("введите километры")
hour_in = input("введите время в часах")

try:
    km = int(km_in)
    hour = int(hour_in)

    massage = hour * km
except ValueError:
    massage = "Это не похоже на числа"


print (massage)