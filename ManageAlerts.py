from cogs import CryptoUpdate, ManageDB
import msgbot
import time

while True:
    CryptoUpdate.update()
    
    # Obtiene las notificaciones para los usuarios
    notifications = ManageDB.check_price_alerts()
    
    # Envía un mensaje a cada usuario que alcanzó su objetivo
    for user_id, crypto_name, current_price in notifications:
        message = f"¡Alerta de precio! {crypto_name} ha alcanzado el precio objetivo de {current_price}."
    
    time.sleep(20)
