import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters


# Cargar el token desde el archivo config.json
with open('config.json') as file:
    data = json.load(file)
    token = data['token']


# Define una función para el comando /start con botones flotantes
async def start(update: Update, context):
    # Crear botones flotantes (inline keyboard)
    keyboard = [
        [InlineKeyboardButton("Botón 1", callback_data='1')],
        [InlineKeyboardButton("Botón 2", callback_data='2')],
        [InlineKeyboardButton("Abrir enlace", url='https://example.com')]
    ]
    
    # Envuelve los botones en un teclado en línea
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Envía un mensaje con los botones flotantes
    await update.message.reply_text('Elige una opción:', reply_markup=reply_markup)

# Define una función para el comando /help
async def help(update: Update, context):
    await update.message.reply_text('¡Hola! Soy tu bot de Telegram. Puedes enviarme mensajes y los repetiré.')

# Define una función que maneje los mensajes
async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

# Función para manejar las interacciones con los botones flotantes
async def button(update: Update, context):
    query = update.callback_query
    await query.answer()  # Confirma la interacción con el botón

    # Envía una respuesta diferente según el botón que se pulse
    if query.data == '1':
        await query.edit_message_text(text="Has elegido el Botón 1")
    elif query.data == '2':
        await query.edit_message_text(text="Has elegido el Botón 2")

async def onready(app):
    print("El bot está en línea y listo para recibir mensajes.")

if __name__ == '__main__':
    # Crea la aplicación del bot con el token
    app = ApplicationBuilder().token(token).build()

    # Añade el manejador del comando /start
    app.add_handler(CommandHandler('start', start))

    # Añade el manejador del comando /help
    app.add_handler(CommandHandler('help', help))

    # Añade un manejador para mensajes de texto
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Añade el manejador para las interacciones con los botones flotantes
    app.add_handler(CallbackQueryHandler(button))
    
    # Ejecuta la función onready cuando el bot esté listo
    app.post_init(onready) 

    # Ejecuta el bot
    app.run_polling()
