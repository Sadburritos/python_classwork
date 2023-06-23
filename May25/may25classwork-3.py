user_program = input("Введите обьём в программы ")
user_flash = input("Введите обьём в флешки ")

try:
    mb = int(user_program)
    flach = int(user_flash)
    
    flach *= 1024

except ValueError:
    massage = "Error"




massage = flach / mb

print(massage)
