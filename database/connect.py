from psycopg2 import connect
from environs import Env

env = Env()
env.read_env()

def get_connect():
    return connect(
        user = env.str("DB_USER"),
        database = env.str("DATABASE"),
        password = env.str("PASSWORD"),
        host = env.str("HOST"),
        port = env.str("PORT")
    )

def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS users (
        id BIGINT PRIMARY KEY NOT NULL,
        fullname VARCHAR(200) NOT NULL,
        phone VARCHAR(50) UNIQUE NOT NULL,
        address TEXT,
        chat_id BIGINT UNIQUE NOT NULL,
        gender VARCHAR(50),
        is_admin BOOLEAN DEFAULT FALSE,
        is_block BOOLEAN DEFAULT FALSE
    );

    CREATE TABLE IF NOT EXISTS category (
        id BIGINT PRIMARY KEY NOT NULL,
        name VARCHAR(50) NOT NULL,
        is_active BOOLEAN DEFAULT TRUE
    );

    CREATE TABLE IF NOT EXISTS product (
        id BIGINT PRIMARY KEY NOT NULL,
        name VARCHAR(200) NOT NULL,
        image TEXT,
        price BIGINT NOT NULL,
        quantity BIGINT DEFAULT 0,
        size VARCHAR(20),
        season VARCHAR(20),
        gender_type VARCHAR(20),
        brand VARCHAR(50),
        category_id BIGINT REFERENCES category(id) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS orders (
        id BIGINT PRIMARY KEY NOT NULL,
        chat_id BIGINT REFERENCES users(chat_id) NOT NULL,
        product_id BIGINT REFERENCES product(id) NOT NULL,
        price BIGINT NOT NULL,
        quantity BIGINT DEFAULT 1,
        status VARCHAR(50) DEFAULT 'new'
    );

    """

    with get_connect() as db:
        with db.cursor() as dbc:
            dbc.execute(sql)
            db.commit()

create_table()