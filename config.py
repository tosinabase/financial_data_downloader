import os

from dotenv import load_dotenv
env_file_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_file_path):
    load_dotenv(env_file_path)

TICKERS = os.getenv('tickers').split()

DATA_PATH = os.getenv('data_dir_path')
