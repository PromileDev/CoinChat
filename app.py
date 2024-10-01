import json
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from cogs import Languaje

# Cargar el token desde el archivo config.json
with open('config.json') as file:
    data = json.load(file)
    token = data['token']


# Define una función para el comando /start con botones en fila
async def start(update: Update, context):
    user_first_name = update.message.from_user.first_name

    # Crear botones en fila (Reply Keyboard)
    keyboard = [

        [KeyboardButton("Idioma/Languaje")],
    ]
    
    # Envuelve los botones en un teclado que aparece encima del campo de texto
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text('Elige una opción / Select option:', reply_markup=reply_markup)


# Define una función que maneje los mensajes de texto
async def echo(update: Update, context):
    message_text = update.message.text
    # Idioma
    if message_text == "Idioma/Languaje":
        await Languaje.selectLanguaje(update, context)


    else:
        # Responder con el texto que envió el usuario si no es un botón
        await update.message.reply_text(f"Lo siento no entiendo que quieres decir con: {message_text}")

# Función que se ejecuta al presionar el Botón 1
async def handle_button1(update: Update, context):
    await update.message.reply_text("Has presionado el Botón 1, ejecutando la función.")

# Función que se ejecuta al presionar el Botón 2
async def handle_button2(update: Update, context):
    await update.message.reply_text("Has presionado el Botón 2, ejecutando la función.")





#Ejecucion del bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(token).build()
    #slash commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    #botones
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("El bot está en línea y listo para recibir mensajes.")
    app.run_polling()
