# Flight Data Pipeline

An end-to-end data pipeline that pulls live flight data from a public API, stores it in a SQL database, analyzes it with Python, and visualizes results in an interactive Tableau dashboard.

## What it does

1. **Extract** — Pulls real-time flight data (schedules, delays, status) from the AviationStack API
2. **Load** — Stores each flight record in a SQLite database
3. **Transform / Analyze** — Uses Python (pandas + SQL) to calculate average departure delays and flight trends
4. **Visualize** — Publishes an interactive chart to Tableau Public

## Live Demo

View the interactive Tableau chart: https://public.tableau.com/app/profile/charvita.vali/viz/FlightDataPipeline-DepartureDelaysbyAirline/AvgDepartureDelaybyAirline_

## Tech Stack

- Python — requests, sqlite3, pandas
- SQL — SQLite for data storage and querying
- API Integration — AviationStack REST API
- Visualization — Tableau Public

## Project Structure

- api_client.py — Handles API authentication and requests
- db_setup.py — Creates the SQLite database schema
- etl.py — Extracts flight data and loads it into SQLite
- analysis.py — Runs SQL aggregations, exports summary CSV
- export_for_viz.py — Exports detailed flight-level data for Tableau
- config.py — Stores API key locally (not committed)

## How to Run

1. Install dependencies: pip3 install requests pandas
2. Add your AviationStack API key to config.py
3. Initialize the database: python3 db_setup.py
4. Pull flight data: python3 etl.py
5. Run analysis: python3 analysis.py
6. Export data for visualization: python3 export_for_viz.py

## Sample Insight

Average departure delay by airline, calculated from live flight data — visualized in the Tableau dashboard linked above.
