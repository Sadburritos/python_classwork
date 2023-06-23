black = "#"
white = " "
field = 0
line = 0
num = 1
line_num = 1
while True:
    num += 1
    if field >= 64:
        break
    if num % 2 == 0:
        while line < 4: 
            print(white,"", black, end="")   #  #  #  #  #  #  #  #  #
            line += 1
            field += 2
        else:
            line = 0
            print(" ", line_num, end="")
            print("")
    #if num % 2 != 0:
    else:
        while line < 4: 
            print (black,"",white, end="")   #  #  #  #  #  #  #  #  #
            line += 1
            field += 2
        else:
            line = 0 
            print(" ", line_num, end="")
            print("")
    line_num += 1
print(" a b c d e f g h")

