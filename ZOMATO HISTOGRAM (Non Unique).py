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
                city = i['restaurants'][j]['restaurant']['location']['city']
                if city not in d:
                    d[city] = 0
                d[city]+=1
                    
                
            except:
                continue

keys = d.values()
print(keys)

plt.hist(keys,bins=100)
plt.show()
plt.savefig('grp.png')