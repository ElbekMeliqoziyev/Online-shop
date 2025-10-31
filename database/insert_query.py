from .connect import get_connect

def insert_user(fullname, phone, gender, address, chat_id):
    try:
        with get_connect() as db:
            dbc = db.cursor()
            dbc.execute("""
                INSERT INTO users(fullname, phone, gender, address, chat_id)
                VALUES (?, ?, ?, ?, ?)
            """, (fullname, phone, gender, address, chat_id))
            db.commit()
            return True
    except Exception as err:
        print(f"User Saving Error: {err}")
        return False
