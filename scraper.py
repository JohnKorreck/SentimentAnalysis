from bs4 import BeautifulSoup

import requests
response = requests.get('https://finance.yahoo.com/quote/KO/news', allow_redirects=True)
if response.status_code != 200:
   print(response.status_code)
   exit(1)
print('Successful')

soup = BeautifulSoup(response.content, 'html.parser')
# tickers = soup.find_all('td')
# tickerlist = []
headline_link = soup.find('a', {'class': 'subtle-link fin-size-small titles noUnderline svelte-wdkn18'})

print(headline_link.text)
