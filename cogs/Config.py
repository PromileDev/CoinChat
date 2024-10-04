from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from cogs import ManageBD, Language, Moneda, ManageAPI, MainPage

async def userConfig(update: Update, context):
    user_id = update.message.from_user.id
    username = update.message.from_user.name
    lenguage = ManageBD.getLanguage(user_id)
    lenguage = 'Español' if lenguage == 'es' else 'English'
    currency = ManageBD.getCurrency(user_id)

    await update.message.reply_text(f'ID: {user_id} | Nombre: {username}')
    await update.message.reply_text(f'Lengua: {lenguage} | Divisa: {currency}')