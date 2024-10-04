import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('telegram_bot.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL primary key,
    username TEXT NOT NULL,
    currency_preference TEXT,
    language_preference TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS cryptocurrencies (
    id TEXT PRIMARY KEY,
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

#Tabla de idiomas
cursor.execute('''
CREATE TABLE IF NOT EXISTS languages (
    prompt TEXT NOT NULL,
    language TEXT NOT NULL,
    id_text TEXT NOT NULL
)
''')

cursor.execute('''
INSERT OR IGNORE INTO cryptocurrencies (id, name, current_price) VALUES
('LTC', 'Litecoin', 0),
('ETH', 'Ethereum', 0),
('XBT', 'Bitcoin', 0);
''')    

cursor.execute('''
INSERT OR IGNORE INTO languages (prompt, language, id_text) VALUES ('👋 ¡Bienvenido a nuestro bot de Telegram! Este bot ofrece dos funciones principales para ayudarte a seguir el mercado de criptomonedas: Consulta de precios en tiempo real: Puedes solicitar el precio actual de las criptomonedas con mas volumen de marcado como lo es el Bitcoin (BTC), Ethereum (ETH) o Litecoin (LIT), y el bot te mostrará el valor en monedas populares como USD o EUR. Alertas automáticas de precios: Configura alertas para tu criptomoneda preferida. Solo necesitas establecer un precio objetivo, y te enviaremos una notificación cuando se alcance. Comienza ahora eligiendo cuál de las dos funciones principales quieres hacer.', 'es', 'help_msg');
''')

cursor.execute('''
INSERT INTO languages (prompt, language, id_text) VALUES ('👋 Welcome to our Telegram bot! This bot offers two main features to help you track the cryptocurrency market: Real-time price check: You can request the current price of the most market cap cryptocurrencies like Bitcoin (BTC), Ethereum (ETH), or Litecoin (LIT), and the bot will show you the value in popular currencies like USD or EUR. Automatic price alerts: Set up alerts for your preferred cryptocurrency. Just choose a target price, and we''ll notify you when it''s reached. Start now by choosing which of the two main features you''d like to use.', 'en', 'help_msg');

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

# Checks
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
def checkLanguage(user_id):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT language_preference FROM users WHERE id = ?
    ''', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return bool(user and user[0])
def checkCurrency(user_id):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT currency_preference FROM users WHERE id = ?
    ''', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return bool(user and user[0])



# Getters
def getLanguage(user_id):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT language_preference FROM users WHERE id = ?
    ''', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user[0]

def getCurrency(user_id):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT currency_preference FROM users WHERE id = ?
    ''', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user[0]






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