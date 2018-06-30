import matplotlib.pyplot as plt
import numpy as np
import json
from collections import Counter
d={}
for files in range(1,6):
    
    a = open('G:/zomato-restaurants-data/file'+str(files)+'.json','r',encoding='utf-8')
    zomato = json.load(a)
    a.close()
    
    
    for i in zomato:
        for j in range(20):
            try:
                
                aggre = i['restaurants'][j]['restaurant']['user_rating']['aggregate_rating']
                city = i['restaurants'][j]['restaurant']['location']['city']
                if float(aggre)>4:
                	if city not in d:
                		d[city] = 0
                	d[city] +=1
                    
                
            except:
                continue

m = {val:key for (key, val) in d.items()}

stars = sorted(m.keys(),reverse=True)
top = []
for i in stars[0:5]:
	top.append(m[i])


plt.plot(top[0:5],stars[0:5])
plt.show()
plt.savefig('grp.png')