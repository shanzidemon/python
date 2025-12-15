def name(f_name,l_name):
    print(f_name,l_name)#it is procedural function
name("Shanzid","Helal")
#we have to pass 2 value.cz we set 2 parameter fuction.

#we can fixed argument.
def name2(f_name,l_name="Helal"):
    print(f_name,l_name)
name2("Shanzid")#Shanzid Helal
#but we can get value by 1 parameter cz we set out default parameter.
name2("Shanzid","Emon")#Shanzid Emon
#it will overwrite the secod parameter.
