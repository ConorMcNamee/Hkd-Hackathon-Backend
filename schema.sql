DROP TABLE IF EXISTS transaction;

CREATE TABLE transaction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trans_date_trans_time TEXT,
    cc_num INTEGER,
    merchant TEXT,
    category TEXT,
    amt REAL,
    first TEXT,
    second TEXT,
    gender TEXT,
    street TEXT,
    city TEXT,
    zip TEXT,
    lat REAL,
    long REAL,
    citi_pop INTEGER,
    job TEXT,
    dob TEXT,
    trans_num TEXT,
    unix_time INTEGER,
    merch_lat REAL,
    merch_long REAL,
    is_fraud INTEGER,
);
