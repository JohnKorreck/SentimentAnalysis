from bs4 import BeautifulSoup
import torch
import requests
import numpy as np
import pandas as pd
from transformers import pipeline
from transformers import AutoTokenizer,AutoModelForSequenceClassification

def get_article_header_list(ticker):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
    # URL based on user iput
    url = f'https://finance.yahoo.com/quote/{ticker}/news'
    # Retrieve web info
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.status_code)
        exit(1)
    print('Successful')
    # Parse 
    soup = BeautifulSoup(response.content, 'html.parser')
    headline_links = soup.find_all('a', {'class': 'subtle-link fin-size-small titles noUnderline svelte-wdkn18'})
    headline_list = []
    for header in headline_links:
        headline_list.append(header.text)
    return headline_list

def new_file_info(textfile, ticker):
    f = open(textfile, 'w')
    for header in get_article_header_list(ticker):
        f.write(f'{header}\n')
    f.close()

def sp500info():
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
    data = {}
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 2:
            data[cells[2].text] = float(f'{cells[3].text}'.strip('%'))
    return data

def ticker_sentiment(header_list):
    model_name = "mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis"
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    score = 0
    for header in header_list:
        res = classifier(header)
        if res[0]['label'] == 'positive':
            score += 1
        elif res[0]['label'] == 'negative':
            score -= 1
        else:
            pass
    return score

def main():
    sp500tickers = sp500info()
    sentimentvalue = 0
    x = 1
    for ticker in sp500tickers.keys():
        if x == 504:
            break
        if (0 < len(ticker) < 5):
            header_list = get_article_header_list(ticker)
            sentimentvalue += ticker_sentiment(header_list)*.01*sp500tickers[ticker]
            print(x)
            x += 1
    print(sentimentvalue)

if __name__ == '__main__':
    main()