import os
# from sqlalchemy import create_engine

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

DB_CREDENTIALS = {
    'host': os.getenv('db_host'),
    'database': os.getenv('db_name'),
    'port': os.getenv('db_port'),
    'user': os.getenv('db_username'),
    'password': os.getenv('db_password'),
}

ENGINE_STR = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(**DB_CREDENTIALS)
# SQL_ENGINE = create_engine(ENGINE_STR)
