from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from cogs import ManageBD

async def printAlerts(update: Update, context):
    user_id = update.message.from_user.id
    alerts = ManageBD.getAlerts(user_id)

    if alerts:
        keyboard = []  # Lista para almacenar los botones
        for alert in alerts:
            id_alerts = alert[0]
            crypto = alert[3]
            target = alert[2]
            crypto_id = alert[4]
            currency = crypto_id[-3:]
            
            if currency == 'USD':
                keyboard.append([InlineKeyboardButton(f"{crypto}: {target}$", callback_data=f'{id_alerts}')])
            else:
                keyboard.append([InlineKeyboardButton(f"{crypto}: {target}€", callback_data=f'{id_alerts}')])

        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('Tus alertas:', reply_markup=reply_markup)
    else:
        await update.message.reply_text('No tienes alertas.')
