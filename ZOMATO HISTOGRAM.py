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
                name = i['restaurants'][j]['restaurant']['name']
                city = i['restaurants'][j]['restaurant']['location']['city']
                
                if city not in d:
                    d[city] = {}
                if name not in d[city]:
                    d[city][name] = aggre
                    
                
            except:
                continue

lis = []
for i in d:
    lis.append(len(i))
lis.sort(reverse=True)
print(lis)
plt.hist(lis,bins=100)
plt.show()
plt.savefig('grp.png')