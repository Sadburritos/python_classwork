my_fille = open ("02.txt","r", encoding = "UTF-8")
text = my_fille.read()
my_fille.close()

num = 0


for x in text:
    if x.isdigit():
        num += 1
       
print(num)