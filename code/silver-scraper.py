try:
	import glob
	import pandas as pd
	import requests as re
	from bs4 import BeautifulSoup as bf
except Exception as e:
	print(f'Error Importing: {e}')

#starting with requesting the page, and getting response [200]
#for asia region only: https://www.worldometers.info/coronavirus/#c-asia%22
url = 'https://www.worldometers.info/coronavirus/#countries' 
req = re.get(url)
#seeing the response code
print(f'Response Code: {req}')

#now we gonna start by extracting all page data to start then EDA!
soup = bf(req.content, 'html.parser')
#now we gonna extract only the table its the important thing!
res = soup.find(id="main_table_countries_today")
#let us now extract the columns by just getting data between <td>!
content = res.find_all('td')

#now the fun part starts!
#we gonna inset all needed data into a list[] to start then playing with it!
data = []
for item in content:
  data.append(item.text.strip())

#making interval when new row in table starts
interval = data.index("USA") - data.index("World")
#Populate lists for dictionary
countries    = data[1::interval]
new_cases    = data[3::interval]
new_deaths   = data[5::interval]
total_cases  = data[2::interval]
total_deaths = data[4::interval]
total_recover= data[5::interval]

#now we adding lists to covid_table dictionary
#and we are ready to start manipulating and wrangling data!
covid_tab = {"country/region":countries, "new_cases":new_cases, "new_deaths":new_deaths,
             "total_cases":total_cases, "total_deaths":total_deaths, "total_recovery":total_recover}

#let us now convert the dict to a pandas dataframe,
#then converting the dataframe into csv file!
cov_data = pd.DataFrame.from_dict(covid_tab, orient='index')
cov_data = cov_data.transpose()

#splitting needed countries into two variables,
#and then we converting it into .csv file!
joData  = cov_data.iloc[40:41]
#saving to .csv files
joData.to_csv("../data/joData/jordan4-01.csv", index = True, header=False)

#now we start the concating for all days,
#and lets concat using looping method
path = ('../data/joData/march')
filesList = glob.glob(path + '/*.csv')
with open(path + 'output.csv','w') as wf:
	for file in filesList:
		with open(file) as rf:
			for line in rf:
				if line.strip():
					if not line.endswith("\n"):
						line+="\n"
						wf.write(line)

print('\nProcess Done... \nAll Data Concated to: output.csv')

#removing punctuation from all rows, then converting them all to int()
#and adding columns names
col_names = ['date','country/region', 'new_cases', 'new_deaths', 'total_cases', 'total_deaths', 'total_recovery']

genData = pd.read_csv('../data/joData/output.csv', names=col_names)
genData['new_cases'] = genData['new_cases'].str.replace(r'\W', '', regex=True).astype('int')
genData['new_deaths'] = genData['new_deaths'].replace(r'\W', '', regex=True).astype('int')
genData['total_cases'] = genData['total_cases'].str.replace(r'\W', '', regex=True).astype('int')
genData['total_deaths'] = genData['total_deaths'].str.replace(r'\W', '', regex=True).astype('int')
genData['total_recovery'] = genData['total_recovery'].str.replace(r'\W', '', regex=True).astype('int')

print(f'\n{genData.head()}')