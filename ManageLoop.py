import asyncio
from cogs import CryptoUpdate, ManageBD
from app import send_message
from telegram import Update

async def main_loop():
    while True:
        CryptoUpdate.update() # Descomentar si esta función es síncrona
        
        # Obtiene las notificaciones para los usuarios
        notifications = ManageBD.check_price_alerts()
        # Envía un mensaje a cada usuario que alcanzó su objetivo
        for user_id, crypto_name, current_price, codigo_err in notifications:
            if codigo_err == 1:
                if ManageBD.getLanguage(user_id) == "es":
                    msg = f"Ha ocurrido un error con tu alerta de {crypto_name}, por favor, intenta de nuevo con un numero valido ej: 100.2"
                else:
                    msg = f"An error has occurred with your {crypto_name} alert, please try again with a valid number eg: 100.2"
                await send_message(Update, None, msg, user_id)
            else:
                if ManageBD.getLanguage(user_id) == "es":
                    msg = f"Has alcanzado tu objetivo de {crypto_name} con un precio de {current_price} {ManageBD.getCurrency(user_id)}"
                else:
                    msg = f"You have reached your target of {crypto_name} with a price of {current_price} {ManageBD.getCurrency(user_id)}"
                await send_message(Update, None, msg, user_id)  # await aquí ya que send_message es una corutina
            
        await asyncio.sleep(3)  # asyncio.sleep para no bloquear el bucle asíncrono

# Ejecutar el bucle principal asíncrono
if __name__ == "__main__":
    asyncio.run(main_loop())
