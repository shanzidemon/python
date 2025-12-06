def my_function(f_name,l_name,age):
    print(f"My name is {f_name} and my last name is {l_name} and i am {age} years old")
my_function("shanzid","Helal",25)

#when we pass value through parameter and forget the sequence like
#where first name,where last name,where age
#then we can use keyword argument which mean we will set argument name in parameter like
my_function(age=25,l_name="helal",f_name="shanzid")#we tell compiler which vlaue is what

#arbitary Number of keyword argument
#arbitary means we don't know the number of keyword argument.
def my_function(**kwargs):
    print(kwargs)
my_function(f_name="Shanzid",marks=40,l_name="helal")
#it store parameter in dictionary format
#{'f_name': 'Shanzid', 'marks': 40, 'l_name': 'helal'}

def my_function2(**kwargs):
    print(f"My name is {kwargs["f_name"]} and i am {kwargs["age"]} old.I mostly love {kwargs["prgraming_language"]}")
my_function2(f_name="shanzid",age=23,prgraming_language="c++")
#we have to formating like this to use arbitary keyword argument.
