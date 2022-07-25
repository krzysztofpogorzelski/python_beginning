#prosty program ksiązka telefoniczna
print(f"\nWitaj w  programie książka telefoniczna. Z menu poniżej wybierz działanie dotyczące kontaktu")
kontakty = []

while(True):

    menu = input("\nD-dodaj, P-pokaz, U-usun, Z-zmien, S-szukaj, K-koniec  \n").upper()

    if menu == "D":
        imie= input("podaj imię: ").upper()
        nazwisko= input("podaj nazwisko: ").upper()
        telefon= input("podaj telefon: ")
        kontakt=[imie, nazwisko, telefon]
        kontakty.append(kontakt)
        print("====Nowy kontakt dodany====")

    elif menu == "P":
        for i in range(len(kontakty)):
            print(f"============================================"
                  f"\nImię: {kontakty[i][0]}, Nazwisko: {kontakty[i][1]}, Telefon: {kontakty[i][2]}")

    elif menu == "U":
        delete= input("\npodaj nazwisko do usunięcia kontaktu: ").upper()
        znaleziono= False
        for i in kontakty:
            if i[1]==delete:
                znaleziono=True
                kontakty.remove(i)
                print(f"\npomyślnie usunięto {delete}")
                break
        if znaleziono==False:
            print(f"\nnie zaleziono kontaktu {delete}")

    elif menu == "Z":
        zm_nazw= input(f"\npodaj nazwisko kontaktu który chcesz zmienic: ").upper()
        n_zmiana= False
        for i in range(len(kontakty)):
            if kontakty[i][1]==zm_nazw:
                n_zmiana=True
                n_nazwisko= input(f"Podaj nowe nazwisko: ").upper()
                kontakty[i][1]=n_nazwisko
                n_imie = input(f"Podaj nowe imie: ").upper()
                kontakty[i][0] = n_imie
                n_telefon = input(f"Podaj nowy telefon: ")
                kontakty[i][2] = n_telefon
                break
        if n_zmiana==False:
            print(f"\nnie znalezionow osoby o nazwisku {zm_nazw}")

    elif menu == "S":
        szukanie = input("wprowadź szukaną frazę imienia lub nazwiska: ").upper()
        szuk_tf=False
        for i in range(len(kontakty)):
            if szukanie in kontakty[i][0] or szukanie in kontakty[i][1]:
                szuk_tf=True
                print(f"========znaleziono kontakt======== \nImię: {kontakty[i][0]}, Nazwisko: {kontakty[i][1]}, Telefon: {kontakty[i][2]}")
        if szuk_tf==False:
            print(f"nie znaleziono szukanej frazy {szukanie}")
    elif menu == "K":
        print("Koniec programu")
        break
