import os

import yfinance as yf
from config import TICKERS, ONE_DAY_DATA_PATH
from utils import init_data_dirs

if __name__ == '__main__':
    init_data_dirs()

    for ticker in TICKERS:
        df = yf.download(tickers=ticker)
        df.to_csv(f"{os.path.join(ONE_DAY_DATA_PATH, ticker)}.csv")
