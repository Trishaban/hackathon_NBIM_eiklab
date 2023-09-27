import pandas as pd
import re

df = pd.read_csv(r"no_sync\analyst_ratings_processed.csv")
df.shape
df = df.dropna()
df.shape
ticks = ["AAPL", "AMZN", "GOOG", "TSLA", "NVDA"]
mask = df['stock'].isin(ticks)

df_filtered = df[mask]

df_filtered.to_csv(r"data\analyst_ratings_processed_filtered.csv", index=False)

print(df_filtered.shape)


def convert_date(input_date):
    try:
        # Create a regular expression pattern to match the input date format
        pattern = r"(\d{4})-(\d{2})-(\d{2}) \d{2}:\d{2}:\d{2}-\d{2}:\d{2}"

        # Use re.match to find matches in the input date
        match = re.match(pattern, input_date)

        if match:
            # Extract year, month, and day from the matched groups
            year = match.group(1)
            month = match.group(2)
            day = match.group(3)

            # Create the desired output date format
            output_date = f"{day}-{month}-{year}"
            return output_date
        else:
            return "Input date does not match the expected format."
    except TypeError:
        pass

# Apply the function to each row in the date column and create a new column
df['converted_date'] = df['date'].apply(lambda x: convert_date(x))

print(df.head())
