a = open("C:\\Users\Sourav\Downloads\datafile.xls - Worksheet.csv",'r')

b = a.readlines()
a.close()

d={}
#print(b)
for i in b:
    #print(i)
    d[i.split(',')[0]] = i.split(',')[3]
    #print(i.split(','))

uin = (input('Enter the State name--> '))
'''for i in c:
        d[i[0]]=i[3]'''

#avg=[d.values()].split(',')
#print(avg)

#count=0
#print(len(avg))
#for i in range(1,len(avg)+1):
               #print(i)
    
#print(d)
print(d[uin])
z = input()



#average of 3rd column
