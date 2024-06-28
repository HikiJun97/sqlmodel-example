import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER", "sgn04088")
DB_PW = os.getenv("DB_PW", "whgudwns1997")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "sqlmodel")
DB_URL = f"mysql+aiomysql://{DB_USER}:{DB_PW}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
