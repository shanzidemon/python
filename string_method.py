#python is a immutable so we can't change string
#but we can modify string.
a="banana"
print(a.title())#1st letter uppercase
print(a.lower())
print(a.upper())
b="apPle"
print(b.swapcase())#capitale will be smalll
                    #small will be capitall
print(b.replace('a','b'))     
#print(b.replace('where will be change','what will be change'))   
print(b.count('a'))      

#we can't change string content string 
#but we can modify it.
c=b.replace('p','l')
print(c)