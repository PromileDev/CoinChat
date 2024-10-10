from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from cogs import ManageBD

# Comando /languaje

async def selectLanguage(update: Update, context):
    user_id = update.message.from_user.id
    # Crear botones en fila (Reply Keyboard)
    keyboard = [
        [KeyboardButton("Español 🇪🇸"), KeyboardButton("English 🇬🇧")]
    ]
    # Envuelve los botones en un teclado que aparece encima del campo de texto
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "seleectLen_msg"), reply_markup=reply_markup)