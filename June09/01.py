num = 1

if num < 10:
    print("Меньше")
else: 
    print("Больше или равно")


while num < 10:
    num += 1
    if num == 5:
        continue
    print("Меньше", num)

else:
    print("Больше или равно")

print("Конец")
