import sqlite3
from telegram import Bot

# Inicializa el bot de Telegram con el token
bot_token = 'TU_TOKEN_DE_BOT'
bot = Bot(token=bot_token)

def check_price_alerts():
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()

    # Seleccionar todas las alertas y comparar con los precios actuales
    cursor.execute('''
    SELECT a.user_id, c.name, c.current_price, a.target_price
    FROM alerts a
    JOIN cryptocurrencies c ON a.cryptocurrency_id = c.id
    ''')

    alerts = cursor.fetchall()

    # Itera sobre las alertas y verifica si el precio actual cumple la condición
    for alert in alerts:
        user_id = alert[0]
        crypto_name = alert[1]
        current_price = alert[2]
        target_price = alert[3]

        # Compara el precio actual con el precio objetivo
        if current_price >= target_price:
            # Envía un mensaje de alerta al usuario
            message = f"¡Alerta! El precio de {crypto_name} ha alcanzado o superado tu precio objetivo de {target_price}. El precio actual es {current_price}."
            send_message_to_user(user_id, message)

    conn.close()

def send_message_to_user(user_id, message):
    try:
        # Enviar mensaje usando el bot de Telegram
        bot.send_message(chat_id=user_id, text=message)
        print(f"Mensaje enviado a {user_id}: {message}")
    except Exception as e:
        print(f"Error al enviar mensaje a {user_id}: {e}")

# Llama a esta función cada cierto intervalo para verificar las alertas
check_price_alerts()
