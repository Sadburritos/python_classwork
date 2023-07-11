my_fille = open ("bibib.txt","r", encoding = "UTF-8")
text = my_fille.readline()
my_fille.close()

if text.startswith("abc"):
    text = text.replace("abc", "www.", 1)
else:
    text = text + ".com"

print (text)
