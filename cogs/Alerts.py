from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
import sqlite3
from app import send_message_to_user
from cogs import ManageBD

# Comando addAlert
async def alertsPageESP(update: Update, context):
    keyboard = [
        [KeyboardButton("Mis alertas"), KeyboardButton("Nueva Alerta")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text('Elige una opcion:', reply_markup=reply_markup)

async def alertsPageENG(update: Update, context):
    keyboard = [
        [KeyboardButton("Manage alerts"), KeyboardButton("New Alert")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text('Choose an option:', reply_markup=reply_markup)


async def showAlerts(update: Update, context):
    user_id = update.message.from_user.id