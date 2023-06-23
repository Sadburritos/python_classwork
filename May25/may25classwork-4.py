user_money = input("Введите сумму денег ")
user_choco = input("Сколько нынче школоад? ")

try:
    mon = int(user_money)
    choco = int(user_choco)

    

except ValueError:
    massage = "Error"
else:
    massage = mon / choco

print(massage)
