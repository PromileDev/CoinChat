import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('telegram_bot.db')
cursor = conn.cursor()

#insert datos de idiomas
cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES ('👋 ¡Bienvenido a nuestro bot de Telegram! Este bot ofrece dos funciones principales para ayudarte a seguir el mercado de criptomonedas: Consulta de precios en tiempo real: Puedes solicitar el precio actual de las criptomonedas con mas volumen de marcado como lo es el Bitcoin (BTC), Ethereum (ETH) o Litecoin (LIT), y el bot te mostrará el valor en monedas populares como USD o EUR. Alertas automáticas de precios: Configura alertas para tu criptomoneda preferida. Solo necesitas establecer un precio objetivo, y te enviaremos una notificación cuando se alcance. Comienza ahora eligiendo cuál de las dos funciones principales quieres hacer.', 'es', 'help_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text) VALUES ('👋 Welcome to our Telegram bot! This bot offers two main features to help you track the cryptocurrency market: Real-time price check: You can request the current price of the most market cap cryptocurrencies like Bitcoin (BTC), Ethereum (ETH), or Litecoin (LIT), and the bot will show you the value in popular currencies like USD or EUR. Automatic price alerts: Set up alerts for your preferred cryptocurrency. Just choose a target price, and we''ll notify you when it''s reached. Start now by choosing which of the two main features you''d like to use.', 'en', 'help_msg');
''')   


conn.commit()
conn.close()