#we can store multiple type of data in a single variable
 #tthat is list
 #list io mutable,thats mean we cann modify value with index number like string
shanzid=[3,4,5.5,"losmi",7.8]
print(shanzid)
shanzid[2]="Losmi"
print(shanzid)
helal="Shanzid Helal Emon"
print(list(helal))#with list function we can convert string to list
#apend is a function where we can add value in list
shanzid.append("Shanzid")
print(shanzid)

#reverse is a function where we can reverse list
shanzid.reverse()
print(shanzid)
#list example
list1=[3,4,5,6,7,7,8,8]
print("List 1 is :",list1)

#tupple is immutable.
#we can not change or modify value in tupple.
#tupple value store in first bracket.
a=(100,400,5000.58777,"losmi",74.84445)
print(a)
#a[3]="Shanzid" #can not change
print(a)
#we can use list function in tupple but can not modify it.
t_reverse=list(reversed(a))
print(t_reverse)