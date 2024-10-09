from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from cogs import ManageBD, MainPage



async def printAlerts(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        await update.message.reply_text('Selecciona una alerta para borrar:', reply_markup=reply_markup)
        
    else:
        await update.message.reply_text('No tienes alertas. Puedes añadir una en el menú principal')
        if ManageBD.getLanguage(user_id) == 'ENG':
            await MainPage.MainPageENG(update, context)
        else:
            await MainPage.MainPageESP(update, context) 
    
async def newAlertPage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if ManageBD.getLanguage(user_id) == 'ENG':
        await update.message.reply_text('Select the crypto:')
    else:
        await update.message.reply_text(':')

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    button_id = query.data
    ManageBD.deleteAlert(button_id)
    await query.edit_message_text(text=f"Has eliminado correctamente la alerta")
    
    if ManageBD.getLanguage(query.from_user.id) == 'es':
        await MainPage.MainPageESP(query, context)
    else:
        await MainPage.MainPageENG(query, context)