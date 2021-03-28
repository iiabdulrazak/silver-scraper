try:
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
joData  = cov_data.iloc[43:44]

#saving to .csv files
joData.to_csv("../data/joData/jordan8.csv", index = True, header=False)

#now we start the concating for all days
col_names = ['date','country/region','new_cases','new_deaths','total_cases','total_deaths','total_recovery']
day1 = pd.read_csv('../data/joData/jordan1.csv', names=col_names)
day2 = pd.read_csv('../data/joData/jordan2.csv', names=col_names)
day3 = pd.read_csv('../data/joData/jordan3.csv', names=col_names)
day4 = pd.read_csv('../data/joData/jordan4.csv', names=col_names)
day5 = pd.read_csv('../data/joData/jordan5.csv', names=col_names)
day6 = pd.read_csv('../data/joData/jordan6.csv', names=col_names)
day7 = pd.read_csv('../data/joData/jordan7.csv', names=col_names)
day8 = pd.read_csv('../data/joData/jordan8.csv', names=col_names)
day9 = pd.read_csv('../data/joData/jordan9.csv', names=col_names)

#lets concat using pd.concat() method
data = pd.concat([day1,day2,day3,day4,day5,day6,day7,day8,day9])
data.to_csv('../data/joData/gen.csv', index=False)

#removing punctuation from all rows, then converting them all to int()
genData = pd.read_csv('../data/joData/gen.csv')
genData['new_cases'] = genData['new_cases'].str.replace(r'\W', '', regex=True).astype('int')
genData['new_deaths'] = genData['new_deaths'].replace(r'\W', '', regex=True).astype('int')
genData['total_cases'] = genData['total_cases'].str.replace(r'\W', '', regex=True).astype('int')
genData['total_deaths'] = genData['total_deaths'].str.replace(r'\W', '', regex=True).astype('int')
genData['total_recovery'] = genData['total_recovery'].str.replace(r'\W', '', regex=True).astype('int')

# print(genData)