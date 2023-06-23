x = float(input('Введите точку Х '))
y = float(input('Введите точку У '))



if x >= 0 and y >= 0:
    print("1 Четверть") 
elif x <= 0 and y <= 0:
    print("3 Четверть")
elif x <= 0 and y >= 0:
    print("2 Четверть")
else:
    print("4 Четверть")
