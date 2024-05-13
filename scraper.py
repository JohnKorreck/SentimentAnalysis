from bs4 import BeautifulSoup
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from scipy.special import softmax
import torch
import requests



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

def headliners(ticker):

    response = requests.get(f'https://finance.yahoo.com/quote/{ticker}/news', headers=headers)
    
    if response.status_code != 200:
        print(response.status_code)
        exit(1)
    print('Request successful')

    soup = BeautifulSoup(response.content, 'html.parser')

    headline_links = soup.find_all('a', {'class': 'subtle-link fin-size-small titles noUnderline svelte-wdkn18'})

    num = 1
    if headline_links:
        for headline in headline_links:
            print(f"{num}. {headline.text}")
            num += 1
    else:
        print("No headlines found")

headliners('KO')

classifier = pipeline("sentiment-analysis")

res = classifier("I've been waiting for ")

print(res)