def isArmstrong(a):
    b=str(a)
    le=len(b)
    sum=0
    for i in b:
        sum += (int(i))**le
    if sum==a:
        print('Number is Armstrong')
    else:
        print('Number is not Armstrong')

        
isArmstrong(153)
