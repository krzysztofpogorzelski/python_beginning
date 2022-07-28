import pickle

class Contact:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.phones=[]
        self.mails=[]

    def __str__(self):
        return f"\nName: {self.name} Surname: {self.surname} \nPhones: {self.phones} \nmails: {self.mails}"


class ContactController:

    def __init__(self):
        self.contactList = []

    def addContact(self, name, surname):
        contact= Contact( name, surname)
        self.contactList.append(contact)
        self.save()

    def addPhone(self, surname, phone):
        l=False
        for i in self.contactList:
            if surname == i.surname:
                i.phones.append(phone)
                print(f"Phone '{phone}' added")
                l=True
        if l==False:
            print(f"There is no contact of surname  '{surname}'\n")
        self.save()

    def addMail(self, surname, mail):
        l=False
        for i in self.contactList:
            if surname == i.surname:
                i.mails.append(mail)
                print(f"Email '{mail}'added")
                l=True
        if l==False:
            print(f"There is no contact of surname  '{surname}'\n")
        self.save()

    def showContacts(self):
        for i in self.contactList:
            print(i)
        self.save()

    def deleteContact(self, surname):
        l=False
        for i in self.contactList:
            if surname == i.surname:
                self.contactList.remove(i)
                l=True
        if l==False:
            print(f"There is no contact of surname  '{surname}'\n")
        else:
            print(f"Contact '{surname}' deleted!")
        self.save()

    def deletePhone(self, surname, phone):
        l=False
        for i in self.contactList:
            if surname==i.surname:
                l=True
                k=False
                for j in i.phones:
                    if phone==j:
                        i.phones.remove(j)
                        print(f"Phone '{phone}' deleted")
                    k = True

                if k==False:
                    print(f"There is not such phone number\n")
        if l==False:
            print(f"There is no contact of surname  '{surname}'")
        self.save()

    def deleteEmail(self, surname, mail):
        l=False
        for i in self.contactList:
            if surname==i.surname:
                l=True
                k=False
                for j in i.mails:
                    if mail==j:
                        i.mails.remove(j)
                        print(f"Email '{mail}' deleted")
                        k=True
                if k==False:
                    print(f"There's not such email adress\n")
        if l==False:
            print(f"There is no contact of surname  '{surname}'\n")
        self.save()

    def save(self):
        file= open("HR_saving.dat", "wb")
        pickle.dump(self.contactList, file)
        file.close()


class App(ContactController):

    def __init__(self):
        super().__init__()
        try:
            file = open("HR_saving.dat", "rb")
            self.contactList = pickle.load(file)
            file.close()
        except:
            file = open("HR_saving.dat", "wb")
            pickle.dump([], file)
            file.close()

        self.menu()

    def menu(self):

        while(True):
            try:
                menu = int(input("\n1-add contact, 2-add phone, 3-add email, "
                                 "\n4- show contacts with phones and emails,"
                                 "\n5-delete contact, 6-delete phone, 7-delete email, 0-end program"
                                 "\n========================================================  "))

                if menu == 1:
                    name = input(f"enter name: ").lower()
                    surname = input(f"enter surname: ").lower()
                    self.addContact(name, surname)

                elif menu == 2:
                    surname = input(f"enter surname: ").lower()
                    phone= int(input(f"enter phone number: "))
                    self.addPhone(surname, phone)

                elif menu == 3:
                    surname = input(f"enter surname: ").lower()
                    mail = input(f"enter email: ")
                    self.addMail(surname, mail)

                elif menu == 4:
                   self.showContacts()

                elif menu == 5:
                    surname = input(f"enter surname of contact to delete: ").lower()
                    self.deleteContact(surname)

                elif menu == 6:
                    surname = input(f"enter surname: ").lower()
                    phone = int(input(f"enter phone: "))
                    self.deletePhone(surname, phone)

                elif menu == 7:
                    surname = input(f"enter surname: ").lower()
                    mail = input(f"enter mail: ").lower()
                    self.deleteEmail(surname, mail)

                elif menu == 0:
                    break
                else:
                    print(f"incorrect menu selection")
            except ValueError:
                print(f"invalid format of the entered value")



app = App()
