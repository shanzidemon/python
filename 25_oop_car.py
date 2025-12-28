# Make a car class and make object
# __init__ :Dandar Method,Constractor and No Return
# Constructor 3 types:
#   Default Constructor
#   Parametarized Constructor
#   Dafult value Constructor
class Car:
# Python does not support method overloading by signature.
# python simply ignore the previous constructo and call the last constructor
# python doest not detect constructor like c++ or java.
    def __init__(self):
        self.brand=''   #Default Constructor
        self.model=''

    def __init__(self,brand,model):# self indicate the object of the class
        self.brand=brand  #Paraametarized Constructor
        self.model=model
    def __init__(self,brand='BmW',model='A17'):
        self.brand=brand   #Dafult value Constructor
        self.model=model
    def Showinfo(self):
        print(f"Car model: {self.model}\nCar Brand:{self.brand}")
car0=Car()
car0.model='Lambo'
car0.brand='A12'
print(car0.model)
print(car0.brand)


car1 = Car('Marcedez','F20')
print(car1.brand)
print(car1.model)

car2=Car()
print(car2.brand)
print(car2.model)
car1.Showinfo()