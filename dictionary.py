#define as {}
#key value pair like {1:"Rahim"}
#indexing not available
#key must be immutable
a={1:"Rahim",2:"Karim",3:"Losmi",4:[2,3,4,5,6,7],5:{2,3,3,3,4,5,6}}
print(a,type(a))
print("-----------------------")
#for loop like this will give the key of a dictionary;
for i in a:
    print(i)

print("--------")

#if we want value we should use a.values()
for i in a.values():
    print(i)
print("--------")
#if we want keys and value withshortcut we want
print(a.keys(),a.values())
print("--------")
#if we want value in items then we should use items
for k,v in a.items():
    print(f"Key name is {k} and value is {v}")
print("--------")
#we can marze to list with dictionary;
b=[1,2,3,4,5,6]
c=["Rahim","Karim","Loami","Janvi","Nishat","Maisha"]
d=zip(b,c)
print(dict(d))
print("-----------")
print(b[1])#it will show the key of a dictionary

#we can get key of a dictionary with indexing.

