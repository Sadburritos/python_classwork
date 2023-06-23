num = int(input())
dif = 2

while dif < num:
    if num % dif != 0:
        message = "Yes"
    else:
        message = "No"    
        break
    dif += 1

print(message)