
import asyncio
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ConversationHandler, ContextTypes
#from cogs import ManageBD, Language, Moneda, MainPage, UserAccount, ManageAPI, PricePage, AlertsPage, ManageAlerts
from dotenv import load_dotenv
import os

# Cargar el token desde el archivo .env
#load the token from the .env file
load_dotenv()
token = os.getenv('API_TOKEN_TEST')
app = ApplicationBuilder().token(token).build()


# Define una función para el comando /start con botones en fila
async def start(update: Update, context):
    user_id = update.message.from_user.id
    username = update.message.from_user.name
    await update.message.reply_text("Welcome to coinchat! 🤖")
    context.user_data['current_page'] = 'main'


def main():
    # Crear la aplicación
    app = ApplicationBuilder().token(token).build()

    # Agregar los manejadores de comandos
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))

    print("El bot está en línea y listo para recibir mensajes.")
    app.run_polling()

if __name__ == '__main__':
    main()