import json
def zomato(x):
    a = open('G:/zomato-restaurants-data/'+x,'r',encoding='utf-8')
    zomato = json.load(a)
    a.close()
    d={}
    c = 0
    top = []
    maxs = 0
    for i in zomato:
        for j in range(20):
            try:
                names = i['restaurants'][j]['restaurant']['name']
                votes = i['restaurants'][j]['restaurant']['user_rating']['votes']
                aggre = i['restaurants'][j]['restaurant']['user_rating']['aggregate_rating']
                city = i['restaurants'][j]['restaurant']['location']['city']
                c+=1
                d[float(aggre)*int(votes)] = names+','+city
                if float(aggre)*int(votes)>maxs:
                    maxs = float(aggre)*int(votes)
                    best = names
                    becity = city = i['restaurants'][j]['restaurant']['location']['city']
                    
                
            except:
                continue
        
        
    resto = zomato[0]['restaurants']
    #print(d)

    print('\nTotal Restaurants: ',c)
    print('Best Restaurant: ',best,',',becity)

    #----------------------------------------------------------------------
    #list_of_keys = list(d.keys())
    #print(max(list_of_keys))

    #TOP 5
    list_of_keys = list(d.keys())
    while len(top)!=5:
        m = max(list_of_keys)
        top.append(d[m])
        list_of_keys.remove(m)

    print('\nTop 5 Restaurants in order of Rank:\n',top)








while True:
    y = input('\nEnter Filename\n->')
    zomato(y)



z = input()


