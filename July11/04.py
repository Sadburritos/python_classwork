my_fille = open ("04.txt","r", encoding = "UTF-8")
text = my_fille.readline()
my_fille.close()

def first_and_last(letter, st):
    idk = []
    # if st.find(letter) == -1:
    #     print("[-1,-1]")
    # else:
    idk.append(st.find(letter))
    idk.append(st.rfind(letter))
    return idk
    

result = first_and_last(input(), text)
print(result)
    