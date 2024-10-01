import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('telegram_bot.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    currency_preference TEXT,
    language_preference TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS cryptocurrencies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    current_price REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    cryptocurrency_id INTEGER NOT NULL,
    target_price REAL NOT NULL,
    currency_preference TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(cryptocurrency_id) REFERENCES cryptocurrencies(id)
)
''')

# Commit changes and close connection
conn.commit()
conn.close()

# Function to add a user
def add_user(name, currency_preference, language_preference):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (name, currency_preference, language_preference)
    VALUES (?, ?, ?)
    ''', (name, currency_preference, language_preference))
    conn.commit()
    conn.close()

# Function to add a cryptocurrency
def add_cryptocurrency(name, current_price):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO cryptocurrencies (name, current_price)
    VALUES (?, ?)
    ''', (name, current_price))
    conn.commit()
    conn.close()

# Function to add an alert
def add_alert(user_id, cryptocurrency_id, target_price, currency_preference):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO alerts (user_id, cryptocurrency_id, target_price, currency_preference)
    VALUES (?, ?, ?, ?)
    ''', (user_id, cryptocurrency_id, target_price, currency_preference))
    conn.commit()
    conn.close()

# Function to check and send alerts (simplified example)
def check_and_send_alerts():
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT a.id, u.name, c.name, c.current_price, a.target_price, a.currency_preference
    FROM alerts a
    JOIN users u ON a.user_id = u.id
    JOIN cryptocurrencies c ON a.cryptocurrency_id = c.id
    ''')

    conn.close()