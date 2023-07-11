my_fille = open("bub.txt", encoding = "utf-8")

fille_text = my_fille.read()
my_fille.close()

text = fille_text.split()

def is_palindrome(word):
    return word == "".join(reversed(word))

a = " ".join(list(filter(is_palindrome, text)))
print(a)

