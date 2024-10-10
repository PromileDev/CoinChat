from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from cogs import ManageBD



async def pagePrice(update: Update, context):
    context.user_data['current_page'] = 'price'
    user_id = update.message.from_user.id

    # Crear botones en fila (Reply Keyboard)
    keyboard = [
        [KeyboardButton("Bitcoin"), KeyboardButton("Ethereum"),KeyboardButton("Litecoin") ],
        [KeyboardButton("Volver")],
    ]
    # Envuelve los botones en un teclado que aparece encima del campo de texto
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "option_msg"),reply_markup=reply_markup)

