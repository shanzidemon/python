# Eror vs Exception
# compile time,Run time
# Eror -->compile time eror
#        -->Syntex,Indentation
# Exception -->Run time eror
#           -->indexing,KeyError,ValueError,ZeroDivisionError

try: # J code a exception thakte pare
    with open('name.txt','r') as container:
        print(container.read())
        print(10/10)
        x=int('adfsdaf')
        print(list[100])
except FileNotFoundError:
        print('File not found')
except ZeroDivisionError:
        print('A number can not be devided by zero')
except NameError:
        print('Name Eror Occured')
except ValueError:
        print('String can not convert into integer')
# for example,Here file.txt not exist but syntex is correct .
#so here will come exception.
try:
        list=[1,2,3,4,5,6]
        print(list[100])
except IndexError:
        print('wrong indexing')
try:
        h=zxy
        print(h)
except Exception as e:
        print('Eror Occured |',e)
else:
    print('Code Exicuted Successfully.') # no exception occurs inside this specific try
finally: # It will excute whatever upper code.
       print('Eta exicute hobe.')

# we can manually trigger a exception.
def check_file(filename):
       if not filename.endswith(.txt):
       raise ValueError('Only .tst file is allowed')

