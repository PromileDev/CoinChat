from telegram import Update, KeyboardButton, ReplyKeyboardMarkup

# Comando addAlert
async def alertsPageESP(update: Update, context):
    keyboard = [
        [KeyboardButton("Mis alertas"), KeyboardButton("Nueva Alerta")],
        [KeyboardButton("Volver")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text('Elige una opcion:', reply_markup=reply_markup)

async def alertsPageENG(update: Update, context):
    keyboard = [
        [KeyboardButton("Manage alerts"), KeyboardButton("New Alert")],
        [KeyboardButton("Back")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Envía un mensaje con el teclado de respuesta
    await update.message.reply_text('Choose an option:', reply_markup=reply_markup)


async def newAlertPage(update: Update, context):
    # Asigna un estado para controlar la función que deben ejecutar los botones
    context.user_data['current_page'] = 'new_alert'
    
    await update.message.reply_text('Selecciona la criptomoneda:')
    keyboard = [
        [KeyboardButton("Bitcoin"), KeyboardButton("Ethereum"), KeyboardButton("Litecoin")],
        [KeyboardButton("Volver")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text('Elige una opción:', reply_markup=reply_markup)
