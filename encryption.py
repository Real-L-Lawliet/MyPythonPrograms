def my_encryption(x):
    chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ?"
    keys="Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM4"
    inds=[]
    encrypt=''
    for i in x:
                  index=chars.index(i)
                  inds.append(index)
    for i in inds:
        encrypt=encrypt+keys[i]
    return encrypt
x='Python'
print(my_encryption(x))
