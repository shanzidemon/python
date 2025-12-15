# Scope ---->a region where a variable is accessible
x=10# Global variable
print(x)
def func():
    y=33# local varible
    print(y)
    x=100# we can modify global variable in block
    # but it will not effect outside of block

func()
print(x)
# print(y)..it can not be print because it is under scope.
# principle of scope

# LEGB
# L-local
# E-Enclosing
# G-Global
# B-Build in Scope
n="Global Variable"#Global Variable

def outer():
    n="Enclosing Variable" #Enclosing variable
    def inner():
        n="Local Variable"#Local Variable
        print(n)
    print(n)# output -->Enclosing cz here inner variable not calling
    inner()# here output -->Local variable because here inner function is called
outer()# output 1st Enclosing
# 2nd output Local Variable
print(n)# Here n=Glbal cause no function apply on here


# Change the Enclosing variable value to Enclosing.


