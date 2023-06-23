from random import *

def get_random_int(max, min):
    result = random() * (max - min)
    result += min
    return int(result)


def game(my_random, min, max):
    user_in = input("Угадай число от %s до %s: "% (min, max))
    try:
        user_num = int(user_in)
    except ValueError:
        print("error")
        game(my_random, min, max)
    else:
        if my_random > user_num:
            print("Больше")
        elif my_random < user_num:
            print("Меньше")
        else:
            print("WIN")
            return
    game(my_random, min, max)
 
num = get_random_int(10, 100)
game(num, min, max)