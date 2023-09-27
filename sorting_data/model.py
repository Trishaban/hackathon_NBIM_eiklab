from transformers import BertTokenizer, BertForSequenceClassification
import numpy as np
import pandas as pd


finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')

df = pd.read_csv(r'..\No_sync\analyst_ratings_processed_filtered.csv')


inputs = tokenizer(sentences, return_tensors="pt", padding=True)
outputs = finbert(**inputs)[0]

# Define a softmax function
def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum(axis=0)

# Define labels for reference
labels = {0: 'neutral', 1: 'positive', 2: 'negative'}

# Create an empty list to store data
data = []

for idx, sent in enumerate(sentences):
    probabilities = softmax(outputs.detach().numpy()[idx])
    row_data = [sent] + [f'{prob * 100:.2f}%' for prob in probabilities]
    data.append(row_data)

# Define column names for the DataFrame
columns = ['title'] + [f'{label} Probability' for label in labels.values()]

# Create a DataFrame
new_df = pd.DataFrame(data, columns=columns)
