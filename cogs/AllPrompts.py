import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('telegram_bot.db')
cursor = conn.cursor()

#insert datos de idiomas
cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Ejecuta /help para ver los comandos y obtener información del bot.'', 'es', 'start_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Execute /help to see the commands or get information about the bot.'', 'en', 'start_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Elige una opción:'', 'es', 'option_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Choose an option:'', 'en', 'option_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Precio de Bitcoin:'', 'es', 'priceB_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Price of Bitcoin:'', 'en', 'priceB_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Precio de Ethereum:'', 'es', 'priceE_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Price of Ethereum:'', 'en', 'priceE_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Precio de Litecoin:'', 'es', 'priceL_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Price of Litecoin:'', 'en', 'priceL_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Error al obtener el precio:'', 'es', 'errorP_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Error in obtaining the price:'', 'en', 'errorP_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Nombre:'', 'es', 'name_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Name:'', 'en', 'name_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Idioma:'', 'es', 'len_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Language:'', 'en', 'len_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Divisa:'', 'es', 'curren_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Currency:'', 'en', 'curren_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Elige un idioma:'', 'es', 'seleectLen_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Choose a language:'', 'en', 'seleectLen_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Idioma actualizado.'', 'es', 'updateL_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Language updated.'', 'en', 'updateL_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Divisa actualizada a'', 'es', 'updateC_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Currency updated to'', 'en', 'updateC_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Introduce la cantidad objetivo:'', 'es', 'inputTarget_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Enter the target amount:'', 'en', 'inputTarget_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Alerta añadida correctamente.'', 'es', 'alertConfirm_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Alert added successfully.'', 'en', 'alertConfirm_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Selecciona una alerta para eliminar:'', 'es', 'selecAlert_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Select an alert to delete:'', 'en', 'selecAlert_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Alerta eliminada correctamente.'', 'es', 'deleteAlert_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Alert deleted successfully.'', 'en', 'deleteAlert_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''No tienes alertas. Puedes añadir una en el menú principal.'', 'es', 'emptyAlert_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''You don''t have any alerts. You can add one from the main menu.'', 'en', 'emptyAlert_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Currency updated to'', 'es', 'updateD_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Divisa actualizada a'', 'en', 'updateD_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Selecciona la criptomoneda:'', 'es', 'selectCrypto_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text)
VALUES (''Select the crypto:'', 'en', 'selectCrypto_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text) 
VALUES ('Selecciona la divisa:', 'es', 'selectCurren_msg');
''')

cursor.execute('''
INSERT OR REPLACE INTO languages (prompt, language, id_text) 
VALUES ('Select the currency:', 'en', 'selectCurren_msg');
''')




conn.commit()
conn.close()