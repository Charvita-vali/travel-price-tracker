import sqlite3
import pandas as pd

conn = sqlite3.connect("flights.db")

df = pd.read_sql_query("""
    SELECT dep_airport, arr_airport,
           COUNT(*) as total_flights,
           AVG(dep_delay) as avg_departure_delay,
           MAX(dep_delay) as worst_departure_delay,
           SUM(CASE WHEN flight_status = 'landed' THEN 1 ELSE 0 END) as landed_count
    FROM flight_snapshots
    GROUP BY dep_airport, arr_airport
""", conn)

print(df)
df.to_csv("flight_summary.csv", index=False)
conn.close()
print("Saved summary to flight_summary.csv")