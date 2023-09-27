import pandas as pd
from datetime import datetime, timedelta

# Input date string in the format "10-06-2020"
date_string = "10-06-2020"

# Convert the date string to a datetime object
date_obj = datetime.strptime(date_string, "%d-%m-%Y")

# Add one day to the date
next_day = date_obj + timedelta(days=1)

# Format the next day as a string in the same format
next_day_string = next_day.strftime("%d-%m-%Y")

print(next_day_string)

df = pd.read_csv(r"data\date_price_tick_sentiment.csv")

print(df.head())
df = df.dropna()

threshold = 85
for row in df.iterrows():
    if float(row[1]["positive Probability"][:-1]) > 80:
        date_string = row[1]["Date"]
        price_today = row[1]["Adjusted Close"]
        print(row[1]["positive Probability"][:-1])
        print(date_string)
        print(next_day_string)
        date_obj = datetime.strptime(date_string, "%d-%m-%Y")
        next_day = date_obj + timedelta(days=1)
        next_day_string = next_day.strftime("%d-%m-%Y")
        result = df.loc[df['Date'] == next_day_string, 'Adjusted Close']
        print(price_today)
        print(type(result))
        print(result)
        # Format the next day as a string in the same format
        

    