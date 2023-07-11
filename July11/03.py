my_fille = open ("03.txt","r", encoding = "UTF-8")
text = my_fille.read()
my_fille.close()


text1 = text[0]

for i in range(1, len(text)):
    if text[i-1] != text[i]:
        text1 += text[i]

print(text1)