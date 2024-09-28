import os
from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import create_engine, text

DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME = os.getenv('DB_USER'), os.getenv('DB_PASS'), os.getenv(
    'DB_HOST'), os.getenv('DB_PORT'), os.getenv('DB_NAME')

engine = create_engine(  # Создание синхронного движка
    url=f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",  # DSN
    echo=True,  # В консоль выводятся все логи работы ORM
    pool_size=5,  # Размер количества соедиений
    max_overflow=10,  # Количество допоолнительных подлючений к БД для выполнения к-л операций
)
with engine.connect() as conn:
    res = conn.execute(text('SELECT VERSION()'))
    print(f"{res=}")
