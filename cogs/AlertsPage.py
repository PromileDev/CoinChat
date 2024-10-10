from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from cogs import ManageBD

# Comando addAlert
async def alertsPageESP(update: Update, context):
    keyboard = [
        [KeyboardButton("Mis alertas"), KeyboardButton("Nueva Alerta")],
        [KeyboardButton("Volver")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text(ManageBD.getPrompt("es", "option_msg"), reply_markup=reply_markup)

async def alertsPageENG(update: Update, context):
    user_id = update.message.from_user.id

    keyboard = [
        [KeyboardButton("Manage alerts"), KeyboardButton("New Alert")],
        [KeyboardButton("Back")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text(ManageBD.getPrompt("en", "option_msg"), reply_markup=reply_markup)


async def newAlertPage(update: Update, context):
    user_id = update.message.from_user.id

    # Asigna un estado para controlar la función que deben ejecutar los botones
    context.user_data['current_page'] = 'new_alert'
    
    await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "selectCrypto_msg"))
    keyboard = [
        [KeyboardButton("Bitcoin"), KeyboardButton("Ethereum"), KeyboardButton("Litecoin")],
        [KeyboardButton("Volver")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "option_msg"), reply_markup=reply_markup)
