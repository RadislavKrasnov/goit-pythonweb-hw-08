import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


class Config:
    DB_URL = DATABASE_URL


config = Config
