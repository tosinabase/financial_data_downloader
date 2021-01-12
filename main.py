import os

import yfinance as yf
from config import TICKERS, DATA_PATH

if __name__ == '__main__':
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)

    for ticker in TICKERS:
        df = yf.download(tickers=ticker)
        df.to_csv(f"{os.path.join(DATA_PATH, ticker)}.csv")
