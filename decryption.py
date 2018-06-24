def my_decryption(x):
    chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ?"
    keys="Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM*"
    inds=[]
    decrypt=''
    for i in x:
                  index=keys.index(i)
                  inds.append(index)
    for i in inds:
        decrypt=decrypt+chars[i]
    return decrypt

x='wpB2h '
print(my_decryption(x))
