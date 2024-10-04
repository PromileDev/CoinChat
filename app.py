import json
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from cogs import ManageBD, Language, Moneda, ManageAPI, MainPage, Config

# Cargar el token desde el archivo config.json
with open('config.json') as file:
    data = json.load(file)
    token = data['token']


# Define una función para el comando /start con botones en fila
async def start(update: Update, context):
    user_id = update.message.from_user.id
    username = update.message.from_user.name
    
    if not ManageBD.checkUser(user_id):
        ManageBD.add_user(user_id, username, None, None)

    if not ManageBD.checkLanguage(user_id):
        await Language.selectLanguage(update, context)
        return

    if not ManageBD.checkCurrency(user_id):
        await Moneda.selectCurrency(update, context)

    if ManageBD.getLanguage(user_id) == 'es':
        await MainPage.MainPageESP(update, context)
    else:
        await MainPage.MainPageENG(update, context)


    

# Define una función que maneje los mensajes de texto
async def echo(update: Update, context):
    message_text = update.message.text
    user_id = update.message.from_user.id
    username = update.message.from_user.name


    # seleccionar Idioma
    if message_text == "Español 🇪🇸":
        ManageBD.upDateLanguage(user_id, 'es')
        await update.message.reply_text('Idioma actualizado a Español 🇪🇸')
        if not ManageBD.checkCurrency(user_id):
            await Moneda.selectCurrency(update, context)
    elif message_text == "English 🏴󠁧󠁢󠁥󠁮󠁧󠁿":
        ManageBD.upDateLanguage(user_id, 'en')
        await update.message.reply_text('Lenguage update to English 🏴󠁧󠁢󠁥󠁮󠁧󠁿')
        if not ManageBD.checkCurrency(user_id):
            await Moneda.selectCurrency(update, context)
    
    
 # Selección de moneda
    elif message_text == "EUR €":
        ManageBD.upDateCurrency(user_id, 'EUR')
        await update.message.reply_text('Currency updated to EUR €.')
        
        # Verifica si ya tiene un idioma seleccionado
        if not ManageBD.checkLanguage(user_id):
            await Language.selectLanguage(update, context)
        else:
            # Si ya tiene un idioma, muestra la página principal en ese idioma
            if ManageBD.getLanguage(user_id) == 'es':
                await MainPage.MainPageESP(update, context)
            else:
                await MainPage.MainPageENG(update, context)
    
    elif message_text == "USD $":
        ManageBD.upDateCurrency(user_id, 'USD')
        await update.message.reply_text('Currency updated to USD $.')
        
        # Verifica si ya tiene un idioma seleccionado
        if not ManageBD.checkLanguage(user_id):
            await Language.selectLanguage(update, context)
        else:
            # Si ya tiene un idioma, muestra la página principal en ese idioma
            if ManageBD.getLanguage(user_id) == 'es':
                await MainPage.MainPageESP(update, context)
            else:
                await MainPage.MainPageENG(update, context)
    
    elif message_text == "Cuenta" or message_text == "Account":
        await Config.userProfile(update, context)
        if ManageBD.getLanguage(user_id) == 'es':
            await Config.configPageESP(update, context)
        else:
            await Config.configPageENG(update, context)

    elif message_text == "Idioma" or message_text == "Language":
        await Language.selectLanguage(update, context)





#Ejecucion del bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(token).build()
    #slash commands
    app.add_handler(CommandHandler('start', start))
    #botones
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("El bot está en línea y listo para recibir mensajes.")

    #job_queue = app.job_queue
    #job_queue.run_repeating(Alerts.check_alerts, interval=10, first=0)

    app.run_polling()

