my_fille = open ("bobob.txt","r", encoding = "UTF-8")
text = my_fille.read()
my_fille.close()


words = text.split()

a = []

for x in words:
    a.append(len(x))
    # text[a].replace(text, len(text[a]))
    

print(min(a))    