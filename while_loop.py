#while loop use when we don't know how many time the loop will be exicute;
a=[1,2,3,4,5,6,7,8,8]
#we will determine the summation of this list;
result=0
i=0
n=len(a)
while i<n:
    result+=a[i]
    i+=1
print(result)
#we can replace 0 to the minus value
b=[1,2,-5,6,-8,-9,10]
i =0
while i<len(b):
    if b[i]<0:
        b[i]=0
    i+=1
print(b)