import pandas as pd
import matplotlib.pyplot as plt
f = pd.read_csv('C:/Users/Sourav/Downloads/train.csv')

#------------------------------------------------------------------------------------------------------------
#1 A MALES AND FEMALES

m=0
fe=0
for i in f['Sex']:
	if i == 'male':
		m+=1
	else:
		fe+=1
l=['Males: 577','Females: 314']

plt.pie([m,fe],labels=l,colors=['r','b'],autopct='%1.1f%%')
plt.title('Males and Females')
plt.legend()
plt.show()

#----------------------------------------------------------------------------------------------------------
#1 B MALES AND FEMALES (NOT SURVIVED)

msur = 0
fsur = 0
for i in range(len(f)):
	if f['Survived'][i]==0 and f['Sex'][i]=='male':
		msur+=1
	elif f['Survived'][i]==0 and f['Sex'][i]=='female':
		fsur+=1


k =['Males: 468','Females: 81']
plt.pie([msur,fsur],explode=[0.1,0.15],labels=k,colors=['b','c'],autopct='%1.1f%%')
plt.title('Males and Females (Not Survived)')
plt.legend()
plt.show()

#-------------------------------------------------------------------------------------------------------------
#2. FARE VS AGE DIFFERED BY GENDER

c=[]
for i in f['Sex']:
	if i=='male':
		c.append('r')
	else:
		c.append('b')

plt.scatter(f['Fare'],f['Age'],c=c)
plt.title('Fare vs Age differed by Gender')
plt.legend()
plt.show()

#-=------------------------------------------------------------------------------------------------------------
#3 AGE , N.SUR.
age = []
for i in range(len(f)):
	if f['Survived'][i] == 0 and f['Age'][i]>0:
		age.append(f['Age'][i])
plt.hist(age,bins=100)
plt.title('Age (Not Survived')
plt.show()

#------------------------------------------------------------------------------------------------------------------
# 4 FARE , N.SUR

fare = []
for i in range(len(f)):
	if f['Survived'][i] == 0 :
		fare.append(f['Fare'][i])

plt.hist(fare,bins=100)
plt.title('Fare (Not Survived')
plt.show()

#------------------------------------------------------------------------------------------------------------------
# 5 CLASS,N.SUR

clas = []
for i in range(len(f)):
	if f['Survived'][i] == 0 :
		clas.append(f['Pclass'][i])
plt.hist(clas,bins=100)
plt.title('Class (Not Survived')
plt.show()

#------------------------------------------------------------------------------------------------------------------
# 6 GENDER, N.SUR
gend = []
for i in range(len(f)):
	if f['Survived'][i] == 0 :
		gend.append(f['Sex'][i])
plt.hist(gend,bins=100)
plt.title('Gender (Not Survived')
plt.show()

#------------------------------------------------------------------------------------------------------------------
# 7 CABIN, N.SUR

cab = []
for i in range(len(f)):
	if f['Survived'][i] == 0  and f['Cabin'][i]!= 0:
		cab.append(f['Cabin'][i])

plt.hist(cab,bins=100)
plt.title('Cabins (Not Survived')
plt.show()

#------------------------------------------------------------------------------------------------------------------
# 8 FARE HISTOGRAM

plt.hist(f['Fare'],bins=100)
plt.title('Fare Histogram')
plt.show()