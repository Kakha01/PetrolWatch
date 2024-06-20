CREATE TABLE IF NOT EXISTS
    fuel (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT NOT NULL,
        fuel_name TEXT NOT NULL,
        fuel_type TEXT NOT NULL,
        fuel_price TEXT NOT NULL
    );