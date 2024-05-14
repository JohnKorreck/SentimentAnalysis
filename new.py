from bs4 import BeautifulSoup
import torch
import requests
import numpy as np
import pandas as pd
from transformers import pipeline
from transformers import AutoTokenizer,AutoModelForSequenceClassification

def get_article_header_list():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
    url = f'https://www.slickcharts.com/sp500'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.status_code)
        exit(1)
    print('Successful')

    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('tr')

    # Iterate through each row and extract the symbol and percentage
    data = []
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 2:
            symbol_link = cells[0].find('a')
            symbol = cells[2].text
            
            percentage = cells[3].text
            data.append((symbol, percentage))

    # Print the extracted data
    for symbol, percentage in data:
        print(f'Symbol: {symbol}, Percentage: {percentage}')



def new_file_info(textfile):
    f = open(textfile, 'w')
    num = 1
    for header in get_article_header_list():
        f.write(f'{header}\n')
        num += 1
    f.close()

new_file_info('slickcharts.txt')

