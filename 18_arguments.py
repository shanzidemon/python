#if we don't know how many para meter we have to pass
#that case we can use args
#args allow to recive multiple parameters and store as a trupple
def Addition(*args):# *args sighn is must
    print(args)
Addition(2,4,5,67,8)

def addition(*args):
    return sum(args)
print(addition(2,4,5,6,7,7,5,4,4,3,2,2,456,7))
