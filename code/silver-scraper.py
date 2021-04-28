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
joData  = cov_data.iloc[41:42]
#saving to .csv files
joData.to_csv("../data/joData/april/jordan28.csv", index = True, header=False)