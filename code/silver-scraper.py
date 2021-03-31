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
joData  = cov_data.iloc[40:41]
#saving to .csv files
joData.to_csv("../data/joData/jordan31.csv", index = True, header=False)

#now we start the concating for all days
col_names = ['date','country/region','new_cases','new_deaths','total_cases','total_deaths','total_recovery']
day01 = pd.read_csv('../data/joData/jordan01.csv', names=col_names)
day02 = pd.read_csv('../data/joData/jordan02.csv', names=col_names)
day03 = pd.read_csv('../data/joData/jordan03.csv', names=col_names)
day04 = pd.read_csv('../data/joData/jordan04.csv', names=col_names)
day05 = pd.read_csv('../data/joData/jordan05.csv', names=col_names)
day06 = pd.read_csv('../data/joData/jordan06.csv', names=col_names)
day07 = pd.read_csv('../data/joData/jordan07.csv', names=col_names)
day08 = pd.read_csv('../data/joData/jordan08.csv', names=col_names)
day09 = pd.read_csv('../data/joData/jordan09.csv', names=col_names)
day10 = pd.read_csv('../data/joData/jordan10.csv', names=col_names)
day11 = pd.read_csv('../data/joData/jordan11.csv', names=col_names)
day12 = pd.read_csv('../data/joData/jordan12.csv', names=col_names)
day13 = pd.read_csv('../data/joData/jordan13.csv', names=col_names)
day14 = pd.read_csv('../data/joData/jordan14.csv', names=col_names)
day15 = pd.read_csv('../data/joData/jordan15.csv', names=col_names)
day16 = pd.read_csv('../data/joData/jordan16.csv', names=col_names)
day17 = pd.read_csv('../data/joData/jordan17.csv', names=col_names)
day18 = pd.read_csv('../data/joData/jordan18.csv', names=col_names)
day19 = pd.read_csv('../data/joData/jordan19.csv', names=col_names)
day20 = pd.read_csv('../data/joData/jordan20.csv', names=col_names)
day21 = pd.read_csv('../data/joData/jordan21.csv', names=col_names)
day22 = pd.read_csv('../data/joData/jordan22.csv', names=col_names)
day23 = pd.read_csv('../data/joData/jordan23.csv', names=col_names)
day24 = pd.read_csv('../data/joData/jordan24.csv', names=col_names)
day25 = pd.read_csv('../data/joData/jordan25.csv', names=col_names)
day26 = pd.read_csv('../data/joData/jordan26.csv', names=col_names)
day27 = pd.read_csv('../data/joData/jordan27.csv', names=col_names)
day28 = pd.read_csv('../data/joData/jordan28.csv', names=col_names)
day29 = pd.read_csv('../data/joData/jordan29.csv', names=col_names)
day30 = pd.read_csv('../data/joData/jordan30.csv', names=col_names)
day31 = pd.read_csv('../data/joData/jordan31.csv', names=col_names)

#lets concat using pd.concat() method
data = pd.concat([day01,day02,day03,day04,day05,day06,day07,
	day08,day09,day10,day11,day12,day13,day14,day15,day16,
	day17,day18,day19,day20,day21,day22,day23,day24,day25,
	day26,day27,day28,day29,day30,day31])

data.to_csv('../data/joData/gen.csv', index=False)

#removing punctuation from all rows, then converting them all to int()
genData = pd.read_csv('../data/joData/gen.csv')
genData['new_cases'] = genData['new_cases'].str.replace(r'\W', '', regex=True).astype('int')
genData['new_deaths'] = genData['new_deaths'].replace(r'\W', '', regex=True).astype('int')
genData['total_cases'] = genData['total_cases'].str.replace(r'\W', '', regex=True).astype('int')
genData['total_deaths'] = genData['total_deaths'].str.replace(r'\W', '', regex=True).astype('int')
genData['total_recovery'] = genData['total_recovery'].str.replace(r'\W', '', regex=True).astype('int')

print(genData)