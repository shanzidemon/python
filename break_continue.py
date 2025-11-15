a=[3,4,5,4,"Sha",9,4,3]
for i in a:
    if type(i)==type("a"):
        break#it will stop the whole loop
    else:
        print(i)
print("-------------------------")
for i in a:
    if type(i)==type('b'):
        continue#it will skip the specific part
    else:
        print(i)



