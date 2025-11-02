"""fruits=["apple","banana","strawberry"]
#Triple
x,y,z=fruits
print(x)
print(y)
print(z)
print(2)
fruits=["apple","banana", "strawberry"]
print(fruits)
print(3)
x=fruits
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x+y+z)
x,y,z=2,3,4
print(x,y,z)
print(x+y+z)
"""
#global variable
"""
x="Awsome"
def my_func():
    print("I am",x)
print(my_func())
"""
#global variable and local variable with same name.
"""x="awsome"
def my_function():
    x="fantastic"
    print("Python is",x)
print(my_function())
print("Python is",x)
"""
#use local variable as global variable
"""
x="Fantastic"
def my_function():
    global x
    x="amaging"
    print("I am",x)
my_function()
print("I am",x)
"""
