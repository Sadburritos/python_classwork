user_in = input()

user_list = user_in.split(',')
numbers = []

# for x in user_list:
#     numbers.append(int(x))

print(user_list)

def get_last_digit(num):
    return num % 10


for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

print(sorted(user_list, key = get_last_digit, reverse=True))