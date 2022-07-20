tries= 5
tries_2= tries
word= input("podaj słowo do odgadnięcia: ")
print(f"================START================\nmasz {tries_2} prób na odgadniecie wyrazu")
word_l=list(word.upper())
word_l_empty=[]
for i in range(len(word_l)):
    word_l_empty.append('_')
    i+=1
print(f"twoje słowo do odgadnięcia to: \n {word_l_empty}")

while word_l_empty.count("_")!=0:
    for i in range(len(word_l)):
        leter = input("podaj litere lub cały wyraz : ").upper()
        for i in range(len(word_l)):
            if word_l[i]==leter:
                word_l_empty[i]=word_l[i]
        if leter.upper()== word.upper():
            print(f"BRAWO ODGADŁES HASŁO: =={word.upper()}==")
            exit()

        if tries == 1:
            print(f"\nnie udało sie, miałes {tries_2} prób"
                  f"\n==========twój wyraz to:========== \n\t\t\t{word.upper()}")
            exit()
        if leter not in word_l:
            tries-=1
            print(f"nie ma litery {leter} w wyrazie")

        print(f"\nodgadywany wyraz: \n {word_l_empty}")
        print(f"pozostało {tries} prób")

