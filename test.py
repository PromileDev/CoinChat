import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Define las funciones de los comandos
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hola! El bot ha iniciado.')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Este es un bot de ayuda.')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

async def custom_loop(app):
    while True:
        print("A")
        await asyncio.sleep(10)

async def main():
    token = "7608695401:AAH1BpFdrUKDtKgTvCX2chcr4vm5-qUcUso"
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("El bot está en línea y listo para recibir mensajes.")
    
    # Inicializa la aplicación
    await app.initialize()

    # Corre el custom_loop en segundo plano usando app.create_task() después de iniciar la aplicación
    app.create_task(custom_loop(app))

    # Ejecuta la aplicación hasta que se detenga manualmente
    await app.run_polling()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())