import os

import yfinance as yf
from config import TICKERS, DATA_PATH


def download_1_day_data(tickers_list, data_path):
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    for ticker in tickers_list:
        df = yf.download(tickers=ticker)
        df.to_csv(f"{os.path.join(DATA_PATH, ticker)}.csv")


if __name__ == '__main__':
    download_1_day_data(TICKERS, DATA_PATH)
