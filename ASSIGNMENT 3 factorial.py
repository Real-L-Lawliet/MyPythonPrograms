def factorialFor(x):
    p=1
    for i in range(x,0,-1):
        p*=i
    print(p)


def factoRecursive(x,p=1):
    if x!=0:
        factoRecursive(x-1,p*x)
    else:
        print(p)

factorialFor(3)
    
factoRecursive(3)
