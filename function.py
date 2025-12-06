#function 2 type
#1.Builin Function-->Its already made by developer.
#print(),input(),sum().
print("Shanzid")#juice under box which can not be modified and don't return value.
input("Value please")#which can be modified and return value
x=input("Enter a value")
print(f"The entered value is {x}")
mx=max([1,2,3,4,5])
print(mx*3)
2.User Define function.---->Programer make it at the time of work.
#input,No return
def my_function():
    a=10
    b=20
    print(a+b)
my_function()
#input,No return
def add_two_number(a,b): #argument
    print(a+b)
add_two_number(16,17)#parameters
#input,return
def multiply_two_number(a,b):
    return a*b
print(multiply_two_number(13,16))
multiply=multiply_two_number(15,76)
print(multiply)
#No Input,Return
def Hello():
    return "Hello"
Hello()
print(Hello())


