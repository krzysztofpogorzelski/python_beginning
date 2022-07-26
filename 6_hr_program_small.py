class Employee:

    def __init__(self, name, surname, contract, salary):
        self.__name= name
        self.__surname= surname
        self.__contract= contract
        self.__salary= salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name1):
        self.__name = name1

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname1):
        self.__surname = surname1

    @property
    def contract(self):
        return self.__contract

    @contract.setter
    def contract(self, contract1):
        self.__contract = contract1

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary1):
        self.__salary = salary1

    def __str__(self):
        return f"Name: {self.__name},  Surname: {self.__surname} , Contract: {self.__contract}, Salary: {self.__salary}"

class EmployeeController:

    def __init__(self):
        self.employeeList = []

    def addEmployee(self, name, surname, contract="internship", salary=1000):
        employee=Employee(name, surname, contract, salary)
        self.employeeList.append(employee)

    def showEmployee(self):
        for i in self.employeeList:
            print(i)

    def deleteEmployee(self, surname):
        for i in self.employeeList:
            if surname==i.surname:
                self.employeeList.remove(i)

    def changeContract(self, surname, salary):
        for i in self.employeeList:
            if surname==i.surname:
                i.salary = salary
                i.contract = "fulltime"


    def findEmployee(self, find):
        l=False
        for i in self.employeeList:
            if find in i.surname or find in i.name:
                l=True
                print(f"Employee which you are looking for is: {i}")
        if l==False:
            print(f"Employee not found")




class Company(EmployeeController):

    def __init__(self, companyName):
        super().__init__()
        self.companyName = companyName
        self.menu()

    def menu(self):

        print(f"Welcome in company {self.companyName}")
        while (True):
            try:
                menu = int(input("\n1-Add Employee, 2-Show Employees, 3-Delete Employee,"
                                 " 4-Change contract, 5-Find Employee, 6-Exit the program   "))

                if menu == 1:
                    name = input (f"Enter name: ").lower()
                    surname = input (f"Enter surname: ").lower()
                    contract= input(f"Enter contract   internship / fulltime  :").lower()

                    if contract=="internship":
                        self.addEmployee(name, surname, "internship", 1000)
                    elif contract=="fulltime":
                        salary= int(input("Enter salary: "))
                        self.addEmployee(name, surname, contract, salary)
                    else:
                        print(f"Type of contract not found, Employee not added")
                        #break

                elif menu == 2:
                    self.showEmployee()

                elif menu == 3:
                    surname= input(f"Enter surname of Employee which you want to delete: ").lower()
                    l = False
                    for i in self.employeeList:
                        if i.surname == surname:
                            self.deleteEmployee(surname)
                            print(f"Employee of surname {surname} has been deleted")
                            l = True
                    if l == False:
                        print(f"There is no Employee of surname {surname} ")


                elif menu == 4:
                    surname= input(f"Enter surname of Employee which you want to change contract: ").lower()
                    l=False
                    for i in self.employeeList:
                        if i.surname==surname:
                            salary= input(f"Enter new salary: ")
                            self.changeContract(surname, salary)
                            l=True
                    if l==False:
                        print(f"There is no Employee of surname {surname}")

                elif menu == 5:
                    find= input(f"Enter the phrase you are looking for: ")
                    self.findEmployee(find)


                elif menu == 6:
                    exit()
                else:
                    print(f"Incorrect menu selection")
            except ValueError:
                print(f"Invalid format of the entered value")


ob = Company("==========Company !==========")
