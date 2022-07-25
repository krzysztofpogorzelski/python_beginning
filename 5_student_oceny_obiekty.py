class Student:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny =[]

    def dodajOceny(self, ocena):
        self.oceny.append(ocena)

    def wypiszOceny(self):
        print(f"posiadasz takie oceny: {self.oceny}")

    def policzSrednia(self):
        print(f"srednia z ocen wynosi: {sum(self.oceny)/len(self.oceny)}")

lista_studentow = []

while(True):
    try:
        menu = int(input(f"\n1-dodaj studenta, 2-pokaz studentow, 3-usun studenta, 4-dodaj ocenę studentowi"
                         f" \n5-wypisz oceny studenta, 6-srednia ocen studenta, 7-zakończ program "))
        if menu == 1:
            imie = input(f"podaj imie: ").upper()
            nazwisko = input(f"podaj nazwisko: ").upper()
            student = Student(imie, nazwisko)
            lista_studentow.append(student)

        elif menu == 2:
            for i in lista_studentow:
                print(f" imię: {i.imie}, nazwisko: {i.nazwisko}")

        elif menu == 3:
            usun= input(f" podaj nazwisko studenta ktorego chcesz usunac: ").upper()
            licznik=0
            for i in lista_studentow:
                if usun==i.nazwisko:
                    lista_studentow.remove(i)
                    licznik+=1
                    break
            if licznik==0:
                print("nie ma takiego studenta")

        elif menu == 4:
            dodaj= input("podaj nazwisko studenta ktoremu chcesz dodac ocene: ").upper()
            try:
                licznik=0
                for i in lista_studentow:
                    if dodaj==i.nazwisko:
                        n_ocena = float(input("podaj ocene: "))
                        i.dodajOceny(n_ocena)
                        print (f"masz nastpujace oceny {i.oceny}")
                        licznik+=1
                if licznik==0:
                    print(f"nie ma studenta o nazwisku {dodaj}")
            except ValueError:
                print(f"podana ocena jest w złym formacie")

        elif menu == 5:
            pokaz= input("podaj nazwisko studenta ktoremu chcesz wypisać oceny: ").upper()
            licznik=0
            for i in lista_studentow:
                if pokaz==i.nazwisko:
                    i.wypiszOceny()
                    licznik+=1
            if licznik==0:
                print(f"nie ma studenta o nazwisku {pokaz}")

        elif menu == 6:
            srednia= input("podaj nazwisko studenta ktoremu chcesz wyswietlic srednia ocen: ").upper()
            licznik=0
            for i in lista_studentow:
                if srednia==i.nazwisko:
                    i.policzSrednia()
                    licznik+=1
            if licznik==0:
                print(f"nie ma studenta o nazwisku {srednia}")

        elif menu == 7:
            exit()
        else:
            print("Nierozpoznana opcja menu")
    except ValueError:
        print(f"podałeś błedny wybór w menu, podaj CYFRĘ jako wybór")

