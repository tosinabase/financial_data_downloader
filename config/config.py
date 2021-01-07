import os

from dotenv import load_dotenv
env_file_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_file_path):
    load_dotenv(env_file_path)

TICKERS = os.getenv('tickers').split()

DATA_PATH = os.getenv('data_filepath')
ONE_DAY_DATA_PATH = os.path.join(DATA_PATH,
                                 os.getenv('one_day_interval_data_dirname'))

ONE_MINUTE_DATA_PATH = os.path.join(DATA_PATH,
                                    os.getenv('one_minute_interval_data_dirname'))

