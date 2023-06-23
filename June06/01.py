def is_simple(num,div = 2):
    if num < 2:
        return False
    if num == div:
        return True
    if num  % div == 0:
        return False
    else:
        return is_simple(num,div + 1)
    
print (is_simple(9))