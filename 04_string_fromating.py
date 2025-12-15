b=input("Enter your name :")
a="Good Morning {},and he loves {}".format(b,"losmi")#.format operator
print(a)

first_name="shanzid"
last_name="helal"
age=24

c=" i love my {} where i am {first_name} {last_name} and i am {age} years old".format("mother",last_name=last_name,first_name=first_name,age=age)
print(c)
#fstring
d=f"i love my mother where i am {first_name} {last_name} and i am {age} years old"
#shortcut kind of formating where we need to use just f;
print(d)