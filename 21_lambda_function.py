#Anonymus Function
#can't be print anything
#it can only return something
#Normal Function
import functools

def square(x):
    return x*x
print(square(5))

#lamda function comprase The function
square= lambda x:x*x
print(square(10))
#sorted with Lmbda functions:
students=[("Rahim",90),("Karim",30),("Shanzid",45)]
sorted_students=sorted(students,key=lambda x:x[1])
print(sorted_students)

#map(),filter(),reduce();

#map=function apply to every element of list,truple,set etc
nums=[3,4,1,5,6,4,3,2]
#nums_square=list(map(square korte catchi,kar upor korte catchi))
nums_square=list(map(lambda x:x*x,nums))
print(nums_square)

#filter:
even_number=list(filter(lambda x: x%2==0,nums))
print(even_number)

sum=functools.reduce(lambda x,y:x+y,nums)
print(sum)