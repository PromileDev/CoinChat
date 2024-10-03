import json
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from cogs import ManageBD, Language, Moneda

# Cargar el token desde el archivo config.json
with open('config.json') as file:
    data = json.load(file)
    token = data['token']


# Define una función para el comando /start con botones en fila
async def start(update: Update, context):
    user_id = update.message.from_user.id
    username = update.message.from_user.name
    
    if (ManageBD.checkUser(user_id) == False):
        ManageBD.add_user(user_id, username ,'EUR', 'es')

    await Language.selectLanguage(update, context)

    # Envuelve los botones en un teclado que aparece encima del campo de texto
    #reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    
    # Envía un mensaje con el teclado de respuesta
    #await update.message.reply_text('Elige una opción / Select option:', reply_markup=reply_markup)


# Define una función que maneje los mensajes de texto
async def echo(update: Update, context):
    message_text = update.message.text
    user_id = update.message.from_user.id
    username = update.message.from_user.name


    # Idioma
    if message_text == "Español 🇪🇸":
        ManageBD.upDateLanguage(user_id, 'es')
        await update.message.reply_text('Idioma actualizado a Español 🇪🇸')
        await Moneda.selectCurrency(update, context)
    elif message_text == "English 🏴󠁧󠁢󠁥󠁮󠁧󠁿":
        ManageBD.upDateLanguage(user_id, 'en')
        await update.message.reply_text('Lenguage update to English 🏴󠁧󠁢󠁥󠁮󠁧󠁿')
        await Moneda.selectCurrency(update, context)
    # Moneda
    elif message_text == "EUR €":
        ManageBD.upDateCurrency(user_id, 'EUR')
        await update.message.reply_text('Moneda actualizada a EUR €')
    elif message_text == "USD $":
        ManageBD.upDateCurrency(user_id, 'USD')
        await update.message.reply_text('Moneda actualizada a USD $')
    else:
        # Responder con el texto que envió el usuario si no es un botón
        await update.message.reply_text(f"Lo siento no entiendo que quieres decir con: {message_text}")





#Ejecucion del bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(token).build()
    #slash commands
    app.add_handler(CommandHandler('start', start))
    #botones
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("El bot está en línea y listo para recibir mensajes.")

    app.run_polling()

