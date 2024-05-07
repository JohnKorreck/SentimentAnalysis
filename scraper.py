from bs4 import BeautifulSoup

import requests
response = requests.get('https://finance.yahoo.com/trending-tickers/')
if response.status_code != 200:
   print('Could not fetch the page')
   exit(1)
print('Successful')

soup = BeautifulSoup(response.content, 'html.parser')
# tickers = soup.find_all('td')
# tickerlist = []
for child in soup.descendants:
    # name = td.a.attrs['title']
    # tickerlist.append(name)
    # print(name)
    if child.td:
            print(child.td)
