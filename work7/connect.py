import psycopg2
from config import load_config


def connect():
    """Connect to PostgreSQL"""
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        print("Connected to PostgreSQL!")
        return conn
    except Exception as error:
        print("Error:", error)



if __name__ == "__main__":
    conn = connect()
    if conn:
        conn.close()
        print("Connection closed.")