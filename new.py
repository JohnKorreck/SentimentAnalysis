from huggingface_hub import hf_hub_download
import joblib

REPO_ID = "mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis"
FILENAME = "sklearn_model.joblib"

model = joblib.load(
    hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
)