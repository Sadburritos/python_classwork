from random import *

def get_random_int(max, min):
    result = random() * (max - min)
    result += min
    return int(result)


def game(my_random, attempt = 20):
    print("Попытки = ", attempt)
    if attempt == 0:
        return
        print("Game over")
    else:
        user_in = input("Угадай число от 0 до 100: ")
        try:
            user_num = int(user_in)
        except TypeError:
            print("error")
            game(my_random)
        else:
            if my_random > user_num:
                print("Больше")
                attempt -= 1
            elif my_random < user_num:
                print("Меньше")
                attempt -= 1
            else:
                print("WIN")
                return

        game(my_random)
 
my_random = get_random_int(0,100)
game(my_random)