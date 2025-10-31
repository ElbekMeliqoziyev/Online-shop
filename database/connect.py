import sqlite3

DB_NAME = "online_shop"

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




# from sqlite3 import connect
# from environs import Env

# import os

# env = Env()
# env.read_env()

# def get_connect():
#     return connect("database.")

# def create_table():
#     sql = """
#     CREATE TABLE IF NOT EXISTS users (
#         id SERIAL PRIMARY KEY,
#         fullname VARCHAR(200) NOT NULL,
#         phone VARCHAR(50) UNIQUE NOT NULL,
#         address TEXT,
#         chat_id BIGINT UNIQUE NOT NULL,
#         gender VARCHAR(50),
#         is_admin BOOLEAN DEFAULT FALSE,
#         is_block BOOLEAN DEFAULT FALSE
#     );

#     CREATE TABLE IF NOT EXISTS category (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(50) NOT NULL,
#         is_active BOOLEAN DEFAULT TRUE
#     );

#     CREATE TABLE IF NOT EXISTS product (
#         id SERIAL PRIMARY KEY ,
#         name VARCHAR(200) NOT NULL,
#         image TEXT,
#         price BIGINT NOT NULL,
#         quantity BIGINT DEFAULT 0,
#         size VARCHAR(20),
#         season VARCHAR(20),
#         gender_type VARCHAR(20),
#         brand VARCHAR(50),
#         category_id BIGINT REFERENCES category(id) NOT NULL
#     );

#     CREATE TABLE IF NOT EXISTS orders (
#         id SERIAL PRIMARY KEY,
#         chat_id BIGINT REFERENCES users(chat_id) NOT NULL,
#         product_id BIGINT REFERENCES product(id) NOT NULL,
#         price BIGINT NOT NULL,
#         quantity BIGINT DEFAULT 1,
#         status VARCHAR(50) DEFAULT 'new'
#     );

#     """

#     with get_connect() as db:
#         with db.cursor() as dbc:
#             dbc.execute(sql)
#             db.commit()

# create_table()