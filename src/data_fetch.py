import pandas as pd
import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch stock data for a given ticker symbol between start_date and end_date.
    
    Parameters:
    ticker (str): Stock ticker symbol (e.g., 'AAPL').
    start_date (str): Start date in 'YYYY-MM-DD' format.
    end_date (str): End date in 'YYYY-MM-DD' format.
    
    Returns:
    pd.DataFrame: Stock data with OHLCV columns.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date, repair=True)
    # data = yf.download(ticker, start=start_date, end=end_date, progress=progress)
    data.to_csv(f'data/raw_data/{ticker}_stock_{start_date}_{end_date}.csv')
    return data

#Example use for testing
if __name__ == "__main__":
    ticker = 'AAPL'
    start_date = '2021-03-11'
    end_date = '2021-03-31'
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    print(stock_data.head())