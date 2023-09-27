import os

from dotenv import load_dotenv

# погрузка .env
load_dotenv()

# Конфиденциальные данные
DB_NAME = os.getenv("DB_NAME")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB_PORT_OUT = os.getenv("DB_PORT_OUT")
DB_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
DB_ECHO = True
