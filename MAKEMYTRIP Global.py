import csv
d = {}
i=0
c=0
with open('G:/hotels-on-makemytrip/makemytrip_com-travel_sample.csv','r',encoding='utf-8') as csvfile:
	read = csv.reader(csvfile,delimiter=',',quotechar='"')
	for row in list(read):
		try:
			c+=1
			city = row[1]
			#area = row[0]
			name = row[22]
			mmt = row[16]
			trip = row[18]
			#site_rev = row[28]
			rating = int(trip)*float(mmt)
			if name in list(d.values()):
				continue
			else:
				d[rating] = name
		except:
			continue



#print("\nTotal Hotels: ",c)
top =[]
keys = list(d.keys())
keys = sorted(keys,reverse=True)
print('\nBest Hotel:',d[keys[0]])


for j in range(5):
    top.append(d[keys[j]])
#print('\nTop 5 Hotels in order of their ranks:\n',top)
print('\nTop 5 Hotels in order of their ranks:')
for i in range(5):
	print(i+1,' - ',top[i])
z=input()