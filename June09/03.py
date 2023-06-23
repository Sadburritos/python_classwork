user_num = input("")

num = 1
dif = int(user_num)

while num <= 100:
    num += 1
    if num % dif == 0:
        print (num)
    