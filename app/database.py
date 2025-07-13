import sqlite3
from contextlib import contextmanager
import atexit


def close_db_connection():
    with get_db_connection() as conn:
        conn.close()

atexit.register(close_db_connection)
@contextmanager
def get_db_connection():
    conn = sqlite3.connect('urls.db', check_same_thread=False)
    try:
        yield conn
    finally:
        conn.close()

def insert_url(original_url, shortened_url):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO urls (original_url, shortened_url) VALUES (?, ?)', (original_url, shortened_url))
        conn.commit()

def get_url(shortened_url):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT original_url FROM urls WHERE shortened_url = ?', (shortened_url,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None