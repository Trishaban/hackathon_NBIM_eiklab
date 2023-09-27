import pandas as pd
import pandas_datareader as pdr
import datetime
import yfinance as yfin


yfin.pdr_override()


# Define the stock symbol and date range
stock_symbol = "AAPL"
start_date = datetime.datetime(2020, 1, 1)
end_date = datetime.datetime(2021, 12, 31)
print(start_date)
# Fetch the data from Yahoo Finance
stock_data = pdr.get_data_yahoo(stock_symbol, start=start_date, end=end_date)

# Display the first few rows of the data
print(stock_data.head())

# You can perform various data analysis tasks here using Pandas
# For example, calculate the daily returns
stock_data['Daily_Return'] = stock_data['Adj Close'].pct_change()

# Calculate the mean daily return
mean_daily_return = stock_data['Daily_Return'].mean()
print(f"Mean Daily Return: {mean_daily_return}")

# Calculate the standard deviation of daily returns
std_daily_return = stock_data['Daily_Return'].std()
print(f"Standard Deviation of Daily Returns: {std_daily_return}")
