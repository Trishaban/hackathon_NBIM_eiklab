import pandas as pd


df_left = pd.read_csv(r"data\analyst_ratings_processed_filtered.csv")
df_right = pd.read_csv(r"data\AAPL.csv")
df_right = df_right[['Date', 'Adjusted Close']]

#Merge on the common column of date
df_merged = pd.merge(df_left, df_right, how="outer", left_on="converted_date", right_on="Date")

print(df_merged.columns)
df_merged = df_merged[["title", "Adjusted Close", "Date"]]
df_merged.to_csv(r"data\date_price_tick.csv", index=False)
print(len(df_merged["Date"].unique()))
print(df_merged.head())