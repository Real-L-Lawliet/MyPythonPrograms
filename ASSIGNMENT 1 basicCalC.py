def basic(x,y):
    a=x+y
    s=x-y
    m=x*y
    if y==0:
        d='Infinity or Undefined'
    else:
        d=x/y
    
    print('Sum of',x,'&',y,'is->',a)
    print('Subtraction of',x,'by',y,'is->',s)
    print('Product of',x,'&',y,'is->',m)
    print('Division of',x,'by',y,'is->',d)


basic(58,0)
