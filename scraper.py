from bs4 import BeautifulSoup

import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}

def get_article_header_list(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}/news'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.status_code)
        exit(1)
    print('Successful')

    soup = BeautifulSoup(response.content, 'html.parser')
    headline_links = soup.find_all('a', {'class': 'subtle-link fin-size-small titles noUnderline svelte-wdkn18'})
    headline_text = []
    for header in headline_links:
        headline_text.append(header.text)
    return headline_text

def new_file_info(textfile, ticker):
    f = open(textfile, 'w')
    num = 1
    for header in get_article_header_list(ticker):
        f.write(f'{num}. {header}\n\n')
        num += 1
    f.close()

ticker = input('Enter a ticker symbol: ')

new_file_info('articleheadline.txt', ticker)