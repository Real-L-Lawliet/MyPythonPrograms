#FOR ZOMATO BEST AND TOP 5 RESTAURANTS (CITY WISE)
#NOTE: Make sure to change the file location according to your directory where file1.json, file2.json... are saved


import json
def zomato_citywise(x):
    a = open('G:/zomato-restaurants-data/'+x+'.json','r',encoding='utf-8')
    zomato = json.load(a)
    a.close()

    d = {}


    for i in zomato:
        try:
            for j in range(len(i['restaurants'])):
                try:
                    sub_d = {}
                    city = i['restaurants'][j]['restaurant']['location']['city']
                    name = i['restaurants'][j]['restaurant']['name']
                    votes = i['restaurants'][j]['restaurant']['user_rating']['votes']
                    aggre = i['restaurants'][j]['restaurant']['user_rating']['aggregate_rating']
                    rating = int(votes)*float(aggre)
                    if city not in d:
                        d[city] = {}
                    
                    d[city][rating] = name

                except:
                    continue
        except:
            continue
    
    for i in list(d):
        top = []
        keys = list(d[i].keys())
        keys = sorted(keys,reverse=True)
        print('-----------------------------------------\nFor',i,':\n','Best Restaurant:',d[i][keys[0]])

        try:
            for j in range(5):
                top.append(d[i][keys[j]])
            print('\nTop 5 in order of their ranks:\n',top)
        except:
            print('\nTop',len(top),'Restaurant order of their ranks:\n',top)
            continue


    return '\nDone!'

while True:
    x =input('\nEnter Filename\n->')
    zomato_citywise(x)
z = input()
