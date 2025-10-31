from .connect import get_connect

def register_by_id(chat_id):
    try:
        with get_connect() as db:
            with db.cursor() as dbc:
                dbc.execute("select * from users where chat_id = %s", (chat_id,))
                return dbc.fetchone()
    except Exception as err:
        print(f"Register: {err}")



def get_filter_products(category_id,season,gender):
    try:
        with get_connect() as db:
            with db.cursor() as dbc:
                dbc.execute("select * from product where category_id = %s and season = %s and gender_type = %s", (category_id,season,gender))
                return dbc.fetchall()
    except Exception as err:
        print(f"Product: {err}")


def get_category_by_name(category_name):
    try:
        with get_connect() as db:
            with db.cursor() as dbc:
                dbc.execute("select * from category where name = %s", (category_name))
                return dbc.fetchone()
    except Exception as err:
        print(f"Filter Category: {err}")



def get_category():
    try:
        with get_connect() as db:
            with db.cursor() as dbc:
                dbc.execute("select id, name from category where is_active = true")
                return dbc.fetchone()
    except Exception as err:
        print(f"Get Category: {err}")