import os
from config import DATA_PATH, ONE_MINUTE_DATA_PATH, ONE_DAY_DATA_PATH


def init_data_dirs():
    for dir_path in [DATA_PATH, ONE_MINUTE_DATA_PATH, ONE_DAY_DATA_PATH]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
