import sqlite3
import pandas as pd

conn = sqlite3.connect("flights.db")

df = pd.read_sql_query("""
    SELECT flight_number, airline, dep_delay, arr_delay, flight_status, checked_at
    FROM flight_snapshots
    ORDER BY checked_at
""", conn)

df.to_csv("flight_details.csv", index=False)
conn.close()
print(f"Exported {len(df)} rows to flight_details.csv")