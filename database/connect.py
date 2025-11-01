import sqlite3

DB_NAME = "online_shop.db"

def get_connect():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")  
    return conn

def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        phone TEXT UNIQUE NOT NULL,
        address TEXT,
        chat_id INTEGER UNIQUE NOT NULL,
        gender TEXT,
        is_admin INTEGER DEFAULT 0,
        is_block INTEGER DEFAULT 0
    );

    CREATE TABLE IF NOT EXISTS category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        is_active INTEGER DEFAULT 1
    );

    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        image TEXT,
        price INTEGER NOT NULL,
        quantity INTEGER DEFAULT 0,
        size TEXT,
        season TEXT,
        gender_type TEXT,
        brand TEXT,
        category_id INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES category(id)
    );

    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        price INTEGER NOT NULL,
        quantity INTEGER DEFAULT 1,
        status TEXT DEFAULT 'new',
        FOREIGN KEY (chat_id) REFERENCES users(chat_id),
        FOREIGN KEY (product_id) REFERENCES product(id)
    );
    """

    with get_connect() as db:
        db.executescript(sql)  
        db.commit()

create_table()

# import os
# print(os.path.abspath(DB_NAME))


