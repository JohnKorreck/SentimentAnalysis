from transformers import pipeline
from transformers import AutoTokenizer,AutoModelForSequenceClassification

model_name = "mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

res = classifier("10. Disney's Future Is Brighter Than It Appears Investors sold off Disney's stock, but the company is still growing in the right places. ")



print (res)