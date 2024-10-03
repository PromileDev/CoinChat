from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters



async def MainPageESP(update: Update, context):
    # Crear botones en fila (Reply Keyboard)
    keyboard = [
        [KeyboardButton("Español 🇪🇸"), KeyboardButton("English 🏴󠁧󠁢󠁥󠁮󠁧󠁿")]
    ]
    # Envuelve los botones en un teclado que aparece encima del campo de texto
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text('Elige un idioma:', reply_markup=reply_markup)


async def MainPageENG(update: Update, context):
    # Crear botones en fila (Reply Keyboard)
    keyboard = [
        [KeyboardButton("Español 🇪🇸"), KeyboardButton("English 🏴󠁧󠁢󠁥󠁮󠁧󠁿")]
    ]
    # Envuelve los botones en un teclado que aparece encima del campo de texto
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text('Elige un idioma:', reply_markup=reply_markup)