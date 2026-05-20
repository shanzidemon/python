class Employes:
    company_name="Shanzid Company"
    def __init__ (self,name,salary):
        self.name=name
        self.salary=salary
    def display_information(self):#instance Method
        print(f"Name is {self.name}\nSalary is {self.salary} \nConpany name is {self.company_name}")

    @classmethod #class method.have to use @classmethod
    def change_company_name(cls,name): #have to use cls to change class method
        cls.company_name=name
o1=Employes("Shanzid",10000000)
o1.display_information()
Employes.change_company_name("Tech")
o1.display_information()
