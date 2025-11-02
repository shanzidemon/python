name1='Shanzid Helal Emon'#String in single quation
name2="Shanzid Helal Emon"#String in double quation
#Both are same and.

name3="Shanzid Helal 'Emon'"#single quation under double quation
name4='Shanzid Helal Emon have "MacBook"'
#if we want to quation under quation.we can not use same quatation.
#we can add String with '+' an ','
#but there is a difference of white space with that.For exammple,
print("Shanzid"+"Helal"+"Emon")#ShanzidHelalEmon
print("Shanzid","Helal","Emon")#Shanzid Helal Emon

#we can access array with index Number.
name5=("Shanzid Helal Emon")
#       012345  #it is the sequance of index Number
print(name5[5])#Here we can get latter of Index Number 5 #Thats mean i
#we can instract where Letter will start and where the letter will be stop. For example
name6="Shanzid Helal Emon"
print(name6[2:])#its mean it will start from the index the 2 and output will last letter of Name6
print(name6[2:5])#its mean it will start with index number 2 and finish with index number 4
#always excluse index Number 5
print(name6[:5])#its mean start with index Number 0 and end with index Number 4.Always exclude last index Number.
#There in a option for negative index Number.For example
name7="Shanzid"
#neg index   -7-6-5-4-3-2-1
print(name7[-1])#here negative index start with  the last number and that is -1 index
print(name7[0:-1])#it will just exclude last degit thats mean last index Number
print(name7[-4:-1])

#here is another option for Multi String which is define by triple quation
name8='''Hello
I am shanzid Helal Emon
I am a engineer.
'''
print(name8)

#There is another thing is formatting.Formating Start with f.For example,
fn1="Shanzid"
fn2="Helal"
fn3="Emon"
fullName=f'{fn1} {fn2} ({fn3}) is a good boy'
print(fullName)
#here we can use f'' to formating text and add other texts,parenthesis, or cube brackets in f'Here'.
#loop in string
#doubt
print("List of banana using for loop")
for x in "Banana":
    print(x)

z="Banana"
print(len(z))#here we can check the length of a string with len() buildin function

#bollean check using in operator
h="Hello guys i'm Shanzid Helal Emon.And i wan to be an AI engineer."
print("faild" in h)

#check in string using if/else
if("free" in h):
    print("Free in the H")
else:
    print("free is not in H")

#using not in operator in string statement.
z="Hello World"
if("free" not in z):
    print("free is not in h")
