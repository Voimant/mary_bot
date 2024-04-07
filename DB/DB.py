import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')
DB_DATABASE = os.getenv('DB_DATABASE')


with psycopg2.connect(user=DB_USER,
                      password=DB_PASSWORD,
                      port=DB_PORT,
                      database=DB_DATABASE) as conn:
    def create_db():
        """
        Функция, создающая структуру БД (таблицы)
        :return: База данных создана
        """
        with conn.cursor() as cur:
            create_query = """ CREATE TABLE IF NOT EXISTS users(
                                user_id VARCHAR(55) PRIMARY KEY);
                                CREATE TABLE IF NOT EXISTS invite(
                                user_id_paty VARCHAR(55),

                                )"""
            cur.execute(create_query)
            return 'База данных создана'


    # print(create_db())
    conn.commit()


    def delete_db():
        """
        Функция, удаляющая таблицы базы данных
        :return: База данных удалена
        """
        with conn.cursor() as cur:
            delete_query = """DROP TABLE order_information;
                DROP TABLE order_number
                CASCADE"""
            cur.execute(delete_query)
            return 'База данных удалена'


    # print(delete_db())
    conn.commit()