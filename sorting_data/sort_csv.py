import pandas as pd

df = pd.read_csv(r"C:\Source\EikLab\hackathon_NBIM_eiklab\no_sync\analyst_ratings_processed.csv")

ticks = ["AAPL", "AMZN", "GOOG", "TSLA", "NVDA"]
mask = df['stock'].isin(ticks)

df_filtered = df[mask]


df_filtered.to_csv(r"C:\Source\EikLab\hackathon_NBIM_eiklab\no_sync\analyst_ratings_processed_filtered.csv", index=False)

print(df_filtered.shape)
print(df.shape)