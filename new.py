from bs4 import BeautifulSoup
import torch
import requests
import numpy as np
import pandas as pd
from transformers import pipeline
from transformers import AutoTokenizer,AutoModelForSequenceClassification


f = open('-headlines.txt', 'r')
lines = f.readlines()

snptickerlist = []
for ticker in lines:
    snptickerlist.append(ticker)
f.close()

print(snptickerlist)