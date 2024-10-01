from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters


# Comando /languaje

async def selectLanguaje(update: Update, context):
    # Crear botones en fila (Reply Keyboard)
    keyboard = [
        [KeyboardButton("Español 🇪🇸"), KeyboardButton("Inglés 🏴󠁧󠁢󠁥󠁮󠁧󠁿")]
    ]
    # Envuelve los botones en un teclado que aparece encima del campo de texto
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text('Elige un idioma:', reply_markup=reply_markup)