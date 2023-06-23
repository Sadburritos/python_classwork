user_m = input("Введите сколько минут ")
user_h = input("Введите сколько часов ")
user_s = input("Введите сколько секунд ")
total_sec = 24 * 60 * 60

try:
    min = int(user_m)
    hour = int(user_h)
    sec = int(user_s)

except ValueError:
    massage = "вы ввели не чимла"
else:
    second_passed = hour * 60 * 60 + min * 60 + sec
    second_left = total_sec - second_passed
    massage = "остлось %s секунд" % second_left

    print(massage)