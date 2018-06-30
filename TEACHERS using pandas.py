import pandas as pd
import numpy

s = pd.read_csv('C:/Users/Sourav/Downloads/datafile.xls - Worksheet.csv',index_col=0,usecols=['State','Professor and Equivalent - Total'])


loop = True
while loop:
	inp = input('Enter the state-> ')
	print(s.loc[inp,'Professor and Equivalent - Total'])
	check = input('\nWant to know the value for other State?')
	if check=='no' or check=='No':
		print('Ok :)')
		loop = False