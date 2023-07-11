my_fille = open("bub.txt", encoding = "utf-8")

text = my_fille.read()
my_fille.close()

word1 = input("Слово = ")
word2 = input("Что менять? ")

change_word = text.replace(word1.upper(), word2.upper())
change_word = change_word.replace(word1.lower(), word2.lower())
print(change_word)

