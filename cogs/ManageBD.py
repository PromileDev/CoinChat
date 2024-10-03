import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('telegram_bot.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id TEXT NOT NULL primary key,
    username TEXT NOT NULL,
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
    current_price REAL NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(cryptocurrency_id) REFERENCES cryptocurrencies(id)
    FOREIGN KEY(currency_preference) REFERENCES users(currency_preference) ON UPDATE CASCADE
    FOREIGN KEY(current_price) REFERENCES cryptocurrencies(current_price) ON UPDATE CASCADE
)
''')

#Tabla de idiomas
cursor.execute('''
CREATE TABLE IF NOT EXISTS languages (
    prompt TEXT NOT NULL,
    language TEXT NOT NULL,
    id_text TEXT NOT NULL
)
''')

# Ejecutar los cambios y cerrar la conexión
conn.commit()
conn.close()

# funcion para añadir un usuario
def add_user(id, username, currency_preference, language_preference):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (id, username ,currency_preference, language_preference)
    VALUES (?, ?, ?, ?)
    ''', (id, username, currency_preference, language_preference))
    conn.commit()
    conn.close()

#funcion para cambiar el idioma
def upDateLanguage(user_id, language_preference):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE users
    SET language_preference = ?
    WHERE id = ?
    ''', (language_preference, user_id))
    conn.commit()
    conn.close()

#funcion para cambiar la moneda
def upDateCurrency(user_id, currency_preference):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE users
    SET currency_preference = ?
    WHERE id = ?
    ''', (currency_preference, user_id))
    conn.commit()
    conn.close()


#
# pendiente de ver
#
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


#
# pendiente de ver
#
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




#print all users
def print_all_users():
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM users
    ''')
    for row in cursor.fetchall():
        print(row)
    conn.close()

# Funcion para ver si existe un usuario
def checkUser(user_id):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE id = ?
    ''', (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return True
    else:
        return False

#delete all usaers
def delete_all_user():
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM users
    ''')
    conn.commit()
    conn.close()
def delete_user(user_id):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM users WHERE id = ?
    ''', (user_id,))
    conn.commit()
    conn.close()

#drop table users
def drop_table_users():
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    DROP TABLE users
    ''')
    conn.commit()
    conn.close()


print_all_users()