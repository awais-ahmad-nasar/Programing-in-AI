class Employee:
    def __init__(self,first,last):
        self.fname=first
        self.lname=last

    @property
    def fulname(self):
        return f'{self.fname} {self.lname}'

    # @fulname.setter
    # def fulname(self,name):
    #     self.fname,self.lname=name.split(' ')
    #     return name

    @property
    def email(self):
        return f'{self.fname}{self.lname}@gamil.com'
    def __str__(self):
        return f' Name : {self.fulname} \nEmail :{self.email}'



class Developer(Employee):
    def __init__(self,first,last,pgrm):
        super().__init__(first,last)
        self.languages=pgrm

    def __str__(self):
        return f'NAME : {self.fulname} \nEmail :  {self.email} \nLanguage : {self.languages}'
    # def display(self):
    #     super().display()
    #     print(self.languages)

d1=Developer("Awais","Ahmad","Java")
d2=Developer("Aina","Omer","Python")
# print(d1)
# print(d2)

class Manager(Employee):
    def __init__(self,first,last,employees=None):
        super().__init__(first,last)

        if employees==None:
            self.employees=[]
        else:
            self.employees=employees

m1=Manager("Shazaib","Khan")
m2=Manager("Ali","Hassan")
m3=Manager("Jawad","Changeez")
print(m1)
print(m2)
print(m3)
