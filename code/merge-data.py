import glob
import pandas as pd

#now we start the concating for all days,
#and lets concat using looping method
path = ('../data/joData/all_months/')
filesList = glob.glob(path + '*.csv')
with open(path + 'all_months.csv','w') as wf:
	wf.write("date,country,new_cases,new_deaths,total_cases,total_deaths,total_recovery")
	for file in filesList:
		with open(file) as rf:
			wf.write(rf.read().strip()+"\n")
			
print('\nProcess Done... \nAll Data Concated to: all_months.csv')

#removing punctuation from all rows, then converting them all to int()
#and adding columns names
genData = pd.read_csv('../data/joData/all_months/all_months.csv')
genData['new_cases'] = genData['new_cases'].str.replace(r'\W', '', regex=True).astype('int')
genData['new_deaths'] = genData['new_deaths'].replace(r'\W', '', regex=True).astype('int')
genData['total_cases'] = genData['total_cases'].str.replace(r'\W', '', regex=True).astype('int')
genData['total_deaths'] = genData['total_deaths'].str.replace(r'\W', '', regex=True).astype('int')
genData['total_recovery'] = genData['total_recovery'].str.replace(r'\W', '', regex=True).astype('int')

print(f'\n{genData.head()}')