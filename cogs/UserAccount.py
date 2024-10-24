from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from cogs import ManageBD, Language, Moneda, ManageAPI, MainPage

async def userProfile(update: Update, context):
    user_id = update.message.from_user.id
    username = update.message.from_user.name
    lenguage = ManageBD.getLanguage(user_id)
    lenguage = 'Español' if lenguage == 'es' else 'English'
    currency = ManageBD.getCurrency(user_id)

    await update.message.reply_text(f'ID: {user_id} | ' +  ManageBD.getPrompt(ManageBD.getLanguage(user_id), "name_msg") + f' {username}')
    await update.message.reply_text( ManageBD.getPrompt(ManageBD.getLanguage(user_id), "len_msg") + f' {lenguage} | ' +  ManageBD.getPrompt(ManageBD.getLanguage(user_id), "curren_msg") + f' {currency}')

async def configPageESP(update: Update, context):
    keyboard = [
        [KeyboardButton("Idioma"), KeyboardButton("Divisa")],
        [KeyboardButton("Volver")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text("Configuración", reply_markup=reply_markup)

async def configPageENG(update: Update, context):
    keyboard = [
        [KeyboardButton("Language"), KeyboardButton("Currency")],
        [KeyboardButton("Back")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text("Settings", reply_markup=reply_markup)