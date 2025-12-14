import os # os library help to do access hardware
import pathlib
# Code use for read from a file
file=open("name.txt","r")
content=file.read()
print(content)
file.close
print("---------------------")

with open("name.txt","r") as file:
    content=file.read()
print(content)

# code use for write a code in file
with open('name2.txt','w') as file:
    file.write('Hello,I am Shanzid Helal Emon\n')
    file.write('I will be crack google,In-Sha-Allah')
# Upper code override the previous text.

# But if need to add some text then programmer should use Append
with open('name3.txt','a') as file:
    file.write('Hello,I am Shanzid Helal Emon\n')
    file.write('I will be crack google,In-Sha-Allah\n')
    file.write('-------------------------\n')

with open('name3.txt','r')as file:
    container=file.read()
print(container)

# if programmer want to add value in list ->
lines=['I lova python\n','I am new to python programing\n','I will go to abroad in-sha-allah']
with open('name4.txt','a') as file:
    file.writelines(lines)

# more on file handeling


if os.path.exists('name.txt'):
    print('File found')
else:
    print('file not found')
# os.path.exists() function check that file is existing or not

file_path=pathlib.Path('name.txt') # This function is for check file
if file_path.exists():
    print('File found')

# check for the absoulute path of a file:
print(os.path.abspath('name.txt')) # It will show the location of a file
print(os.path.getsize('name.txt')) #it will show the size of a file in byte

