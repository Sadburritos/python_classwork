# my_fille = open("bobob.txt", encoding="utf-8")
# text = my_fille.read()
# my_fille.close

# print(text)

my_fille = open("bobob.txt","a", encoding = "UTF-8")

for  i in range(10):
    my_fille.write("\nyo")


my_fille.close