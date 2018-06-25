a = 'C:\\Users/Sourav\Downloads\datafile.xls - Worksheet.csv'

b = [line for line in open(a)]
d = {}


for i in b:
    d[i.split(',')[0]] = i.split(',')[3]



con = True
while con:
    print(d[input('Enter the State: ')])
    con = input('\nWant to know the value for other state?\n')
    if con=='No' or con=='no':
        con=False

