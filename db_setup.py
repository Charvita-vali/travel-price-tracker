import sqlite3

def init_db():
    conn = sqlite3.connect("flights.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS flight_snapshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flight_number TEXT,
            airline TEXT,
            dep_airport TEXT,
            arr_airport TEXT,
            dep_scheduled TEXT,
            dep_delay INTEGER,
            arr_scheduled TEXT,
            arr_delay INTEGER,
            flight_status TEXT,
            checked_at TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()