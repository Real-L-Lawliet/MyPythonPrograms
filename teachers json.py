import json
teach = open('C:/Users/Sourav/Downloads/teachers.json','r')


a = json.load(teach)
teach.close()

lis = a['data']
d = {}
for i in lis:
    d[i[0]] = int(i[3])

loop = True
while loop:
    inp = input('Enter the State: ')
    print(d[inp])
    keep = input('\nWant to know value for other state?\n')
    if keep=='no' or keep=='No':
        loop= False
        



print('\nAverage: ',sum(d.values())/36)
