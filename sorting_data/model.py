from transformers import BertTokenizer, BertForSequenceClassification
import numpy as np
import pandas as pd


finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')

df = pd.read_csv(r'..\No_sync\analyst_ratings_processed_filtered.csv')