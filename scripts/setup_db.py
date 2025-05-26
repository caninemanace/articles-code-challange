from lib.db.connection import get_connection

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    
    with open("lib/db/schema.sql", "r") as schema_file:
        schema = schema_file.read()
        cursor.executescript(schema)

    conn.commit()
    conn.close()
    print(" Database and tables created successfully!")

if __name__ == "__main__":
    setup_database()

