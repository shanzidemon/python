#setn is define as {}
#unordered --> we can not ger value by indexing
#immutable --> we can not update or insert value
#no duplicate item
#set()

a=[2,3,3,4,5,5,6,7,7]
b=set(a)#we can make list to set with set function
print(b)
c={2,3,4,5,6,7,8,7,7,7,}
print(c)
#print(c[1])
#we can not get value by indexing

#Now we will se union and intersection of two set
#union
d={2,3,4,5,6,7}
e={4,5,6,7,8,9}
f=d.union(e)
print(f)
#intersection
g=d.intersection(e)
print(g)

