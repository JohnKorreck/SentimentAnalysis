from bs4 import BeautifulSoup
import torch
import requests
import numpy as np
import pandas as pd
from transformers import pipeline
from transformers import AutoTokenizer,AutoModelForSequenceClassification

def get_article_header_list(ticker):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
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
        f.write(f'{header}\n')
        num += 1
    f.close()

def ticker_sentiment(textfile):
    model_name = "mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis"
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    f = open(textfile, 'r')
    lines = f.readlines()
    score = 0
    for header in lines:
        res = classifier(header)
        if res[0]['label'] == 'positive':
            score += 1
        elif res[0]['label'] == 'negative':
            score -= 1
        else:
            pass
    f.close()
    return score

ticker = input('Enter a ticker symbol: ')

new_file_info(f'{ticker}-headlines.txt', ticker)

print(ticker_sentiment(f'{ticker}-headlines.txt'))
