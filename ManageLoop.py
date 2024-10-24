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
        for user_id, crypto_name, current_price in notifications:
            msg = f"Has alcanzado tu objetivo de {crypto_name} con un precio de {current_price}"
            await send_message(Update, None, msg, user_id)  # await aquí ya que send_message es una corutina
        
        await asyncio.sleep(3)  # asyncio.sleep para no bloquear el bucle asíncrono

# Ejecutar el bucle principal asíncrono
if __name__ == "__main__":
    asyncio.run(main_loop())
