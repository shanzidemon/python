a=[3,4,5,6,7,8,9,22,34,56,77]
#procedural method
result=[]
for i in a:
    if i%2==0:
        result.append(i)
print(result)

new_result=[i for i in a if i%2==0]
print(new_result)

#Now we do which number is even number,that will be multiply and store at result update
result_update=[i**2 for i in a if i%2==0]

#now if we want to use if,else both in a single line then
for i in a:
    if i%2==0:
        i**2
    else:
        i
                #result of if
                #   !              else statement
                #                       !
result_update_new=[i**2 if i %2==0 else i for i in a]
                #   !   if statement            loop
print(result_update_new)
