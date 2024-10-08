from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters



async def MainPageESP(update: Update, context):
    # Crear botones en fila (Reply Keyboard)
    keyboard = [
        [KeyboardButton("Precio"), KeyboardButton("Alertas")],
        [KeyboardButton("Cuenta")],
    ]
    # Envuelve los botones en un teclado que aparece encima del campo de texto
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text('Ejecuta /help para ver los comandos y la información del bot.')
    await update.message.reply_text("Elije una opcion",reply_markup=reply_markup)



async def MainPageENG(update: Update, context):
    # Crear botones en fila (Reply Keyboard)
    keyboard = [
        [KeyboardButton("Price"), KeyboardButton("Alerts")],
        [KeyboardButton("Account")],
    ]
    # Envuelve los botones en un teclado que aparece encima del campo de texto
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text('Execute /help if you need to know the commands or getting info of our bot.')
    await update.message.reply_text('Choose an option:', reply_markup=reply_markup)