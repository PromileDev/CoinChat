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
    currency TEXT NOT NULL,
    current_price REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    cryptocurrency_id INTEGER NOT NULL,
    target_price REAL NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(cryptocurrency_id) REFERENCES cryptocurrencies(id)
)
''')

#Tabla de idiomas
cursor.execute('''
CREATE TABLE IF NOT EXISTS languages (
    prompt TEXT NOT NULL,
    language TEXT NOT NULL,
    id_text TEXT NOT NULL,
    PRIMARY KEY (language, id_text)
)
''')

cursor.execute('''
INSERT OR IGNORE INTO cryptocurrencies (id, name, currency ,current_price) VALUES
('LTCEUR', 'Litecoin', 'EUR' ,0),
('ETHEUR', 'Ethereum', 'EUR' ,0),
('XBTEUR', 'Bitcoin', 'EUR' ,0),
('LTCUSD', 'Litecoin', 'USD' ,0),
('ETHUSD', 'Ethereum', 'USD' ,0),
('XBTUSD', 'Bitcoin', 'USD' ,0);
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
def updateLanguage(user_id, language_preference):
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
def updateCurrency(user_id, currency_preference):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE users
    SET currency_preference = ?
    WHERE id = ?
    ''', (currency_preference, user_id))
    conn.commit()
    conn.close()





#get all alerts from user
def getAlerts(user_id):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT a.id, a.user_id, a.target_price, c.name, c.id
    FROM alerts as a join cryptocurrencies as c on c.id = a.cryptocurrency_id
    WHERE user_id = ?
    ''', (user_id,))
    alerts = cursor.fetchall()
    conn.close()
    return alerts
# add alert
def addAlert(user_id, cryptocurrency_id, target_price):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO alerts (user_id, cryptocurrency_id, target_price)
    VALUES (?, ?, ?)
    ''', (user_id, cryptocurrency_id, target_price))
    conn.commit()
    conn.close()
def check_price_alerts():
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT a.id, a.user_id, c.name, c.current_price, a.target_price
    FROM alerts a
    JOIN cryptocurrencies c ON a.cryptocurrency_id = c.id
    ''')
    alerts = cursor.fetchall()
    
    # Lista para guardar los usuarios que deben recibir un mensaje
    notifications = []
    
    for alert in alerts:
        id, user_id, crypto_name, current_price, target_price = alert
        if current_price >= target_price:  # Verifica si se ha alcanzado el objetivo
            notifications.append((user_id, crypto_name, current_price))
            cursor.execute('DELETE FROM alerts WHERE id = ?', (id,))
            conn.commit()
    
    conn.close()
    return notifications

def deleteAlert(alert_id):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM alerts WHERE id = ?
    ''', (alert_id,))
    conn.commit()
    conn.close()

# update cryptocurrency price
def update_cryptocurrency_price(cryptocurrency_id, current_price):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE cryptocurrencies
    SET current_price = ?
    WHERE id = ?
    ''', (current_price, cryptocurrency_id))
    conn.commit()
    conn.close()
# get cryptocurrency price
def get_cryptocurrency_price():
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT id,current_price FROM cryptocurrencies
    ''')
    cryptocurrency = cursor.fetchall()
    conn.close()
    return cryptocurrency



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

def getPrompt(language, id_text):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        SELECT prompt FROM languages WHERE language = ? AND id_text = ?
        ''', (language, id_text))
        
        user = cursor.fetchone()  # Obtiene la fila resultante
        
        if user is None:
            # Manejo del caso donde no se encuentra el mensaje
            return "Mensaje no encontrado."  # Mensaje por defecto si no existe el esperado
        
        return user[0]  # Devuelve el primer elemento si existe

    except sqlite3.Error as e:
        # Manejo de errores de la base de datos
        print(f"Error al acceder a la base de datos: {e}")
        return "Error al acceder al mensaje."  # Mensaje por defecto en caso de error



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
#drop table 
def drop_table(table):
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute(f'''
    DROP TABLE {table}
    ''')
    conn.commit()
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

print_all_users()