message="Hey there,How are you?"
#       0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21
#neg index   ........-4-3,-2,-1
#we can print a char of string by index number
print(message[0])#here we print a char from string by index number
print(message[5])
#here we can find the length of a string by len() function;
print(len(message))
#if we watn we can print the last char of a string with some methon
#The long method is
print(message[len(message)-1])
#the short method is negative indexing(only in python)
print(message[-1])
print(message[-8])