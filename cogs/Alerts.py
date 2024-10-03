from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import sqlite3
import ManageBD

# Comando addAlert
async def addAlertESP(update: Update, context):
    keyboard = [
        [KeyboardButton("Alertas"), KeyboardButton("Nueva Alerta")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text('Elige una opcion:', reply_markup=reply_markup)

async def addAlertENG(update: Update, context):
    keyboard = [
        [KeyboardButton("Alerts"), KeyboardButton("New Alert")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text('Choose an option:', reply_markup=reply_markup)