import os
from alpha_vantage.timeseries import TimeSeries

API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

def get_stock_data(symbol):
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    try:
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')
        return data
    except Exception as e:
        print(f"Error getting data for {symbol}: {e}")
        return None

def add_stock_to_portfolio(portfolio, symbol):
    stock_data = get_stock_data(symbol)
    if stock_data is not None:
        portfolio[symbol] = stock_data
        print(f"Added {symbol} to the portfolio.")
    else:
        print(f"Error adding {symbol} to the portfolio.")

def calculate_portfolio_value(portfolio):
    total_value = 0
    for symbol, data in portfolio.items():
        total_value += data['4. close'].iloc[-1]  # Assuming '4. close' is the closing price
    return total_value

if __name__ == "__main__":
    portfolio = {}
    symbols = ['AAPL', 'GOOGL']  # Example list of stock symbols

    for symbol in symbols:
        add_stock_to_portfolio(portfolio, symbol)

    print("Portfolio:")
    for symbol, data in portfolio.items():
        print(f"{symbol}: {data['4. close'].iloc[-1]}")  # Print latest closing price for each stock

    portfolio_value = calculate_portfolio_value(portfolio)
    print(f"Total Portfolio Value: {portfolio_value}")


