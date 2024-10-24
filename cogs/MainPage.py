from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from cogs import ManageBD


async def MainPageESP(update: Update, context):
    # Crear botones en fila (Reply Keyboard)
    keyboard = [
        [KeyboardButton("Precio"), KeyboardButton("Alertas")],
        [KeyboardButton("Cuenta")],
    ]
    # Envuelve los botones en un teclado que aparece encima del campo de texto
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta

    await update.message.reply_text((ManageBD.getPrompt("es", "start_msg")))
    await update.message.reply_text(ManageBD.getPrompt("es", "option_msg"),reply_markup=reply_markup)



async def MainPageENG(update: Update, context):
    # Crear botones en fila (Reply Keyboard)
    keyboard = [
        [KeyboardButton("Price"), KeyboardButton("Alerts")],
        [KeyboardButton("Account")],
    ]
    # Envuelve los botones en un teclado que aparece encima del campo de texto
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text((ManageBD.getPrompt("en", "start_msg")))
    await update.message.reply_text(ManageBD.getPrompt("en", "option_msg"), reply_markup=reply_markup)