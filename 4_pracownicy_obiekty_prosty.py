#program przechowujący dane pracowników w postaci obiektów
class Pracownik:

    def __init__(self, _imie, _nazwisko, _email, _telefon):
        self.imie = _imie
        self.nazwisko = _nazwisko
        self.email = _email
        self.telefon = _telefon

lista_pracownikow=[]

while (True):
    try:
        menu = int(input("\n1-dodaj pracownika, 2-pokaz dane pracowników, 3-usun pracownika, "
                         "4-zmien dane pracownika, 5-zakończ program "))

        if menu == 1:
            imie= input(f"podaj imie: ").upper()
            nazwisko= input(f"podaj nazwisko: ").upper()
            email= input(f"podaj email: ")
            telefon= input(f"podaj telefon: ")

            pracownik = Pracownik(imie, nazwisko, email, telefon)
            lista_pracownikow.append(pracownik)

        elif menu == 2:
            for i in range(len(lista_pracownikow)):
                print(f" imię: {lista_pracownikow[i].imie}, nazwisko: {lista_pracownikow[i].nazwisko}, "
                      f"email: {lista_pracownikow[i].email}, telefon: {lista_pracownikow[i].telefon}")

        elif menu == 3:
            usun= input(f"podaj nazwisko pracownika ktorego chcesz usunac: ").upper()
            licznik=0
            for i in lista_pracownikow:
                if usun==i.nazwisko:
                    lista_pracownikow.remove(i)
                    licznik+=1
                    print(f"pracownik {usun} został usuniety!")
                    break
            if licznik==0:
                print("nie ma takiego pracownika")
        elif menu == 4:
            zmien= input(f"podaj nazwisko pracownika ktorego dane chcesz zmienic: ").upper()
            licznik=0
            for i in lista_pracownikow:
                if zmien==i.nazwisko:
                    n_imie = input(f"podaj nowe imie: ").upper()
                    n_nazwisko = input(f"podaj nowe nazwisko: ").upper()
                    n_email = input(f"podaj nowy email: ")
                    n_telefon = input(f"podaj nowy telefon: ")
                    i.imie, i.nazwisko, i.email, i.telefon = n_imie, n_nazwisko, n_email, n_telefon
                    licznik+=1
            if licznik == 0:
                print("nie ma takiego pracownika")

        elif menu == 5:
            print(f"Nastąpiło zamknięcie programu")
            exit()
        else:
            print("nierozpoznana opcja menu")
    except ValueError:
        print("Podaj cyfrę przy wyborze z menu")
