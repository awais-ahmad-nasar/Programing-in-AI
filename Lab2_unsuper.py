# class Employee:
#     def __init__(self,name,eid,salary):
#         self.fname=name
#         self.Eid=eid
#         self.Salary=salary
#
#     @property
#     def fullname(self):
#         return f'{self.fname}'
#     @fullname.setter
#     def fullname(self,name):
#         self.fname=name.split(" ")
#
# class Developer(Employee):
#     def __init__(self,name,eid,salary,pgrm,exp):
#         super().__init__(name,eid,salary)
#         self.program=pgrm
#         self.experience=exp
#
#     def add_developer(self):
#         self.fname =eval(input("Enter Name Of Developer : "))
#         self.Eid =input("Enter the Developer ID : ")
#         self.Salary =input("Enter the Salary of the Developer : ")
#         self.program=eval(input("Enter the Programing language of Developer : "))
#         self.experience=eval(input("Enter the Experience of Developer : "))
#         dev_list = []
#         new_Developer = Developer(self.fname, self.Eid, self.Salary, self.program, self.experience)
#         dev_list = new_Developer.append()
#
#
#
#
#
#     def most_Experienced(self):
#
#
#
#
#     def menu(self,choice=0):
#         print("Press 1 of Add Developer",
#               "Press 2 for most Experince Developer",
#               "Press 3 for displaying all Developers",
#               "Press 4 for low paid Dev




##########################################################################################################

class Employee:
    def __init__(self, name, eid, salary):
        self.name = name
        self.eid = eid
        self.salary = salary


class Developer(Employee):
    def __init__(self, name, eid, salary, programming_language, experience):
        super().__init__(name, eid, salary)
        self.programming_language = programming_language
        self.experience = experience

developers = []

while True:
    print("\nEmployee Management System")
    print("1. Add Developer")
    print("2. Display Most Experienced Developer")
    print("3. Display All Developers")
    print("4. Display Low-Paid Developer")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter Name: ")
        eid = input("Enter Employee ID: ")
        salary = float(input("Enter salary: "))
        programming_language = input("Enter programming language: ")
        experience = int(input("Enter Experience of Developer: "))
        developer = Developer(name, eid, salary, programming_language, experience)
        developers.append(developer)

    elif choice == '2':
           if developers:
             most_experienced_dev = max(developers)
             print(f"Most Experienced Developer:");
             print(f"Name: {most_experienced_dev.name}");
             print(f"Experience: {most_experienced_dev.experience} years");
           else:
             print("No developers added yet.");

    elif choice == '3':
         if developers:
            print("List of Developers:");
         for developer in developers:
            print(f"Name: {developer.name}, ID: {developer.eid}, Salary: {developer.salary}");
         else:
            print("No Developers Added");

    elif choice == '4':
          if developers:
            low_paid_dev = min(developers)
            print(f"Lowest Paid Developer:");
            print(f"Name: {low_paid_dev.name}");
            print(f"Salary: {low_paid_dev.salary}");
          else:
            print("No developers added yet.")

    elif choice=='5':
         print("Exiting the program.");
         break;

    else:
        print("Wrong choice.")

























