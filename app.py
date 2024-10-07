import json
import asyncio
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from cogs import ManageBD, Language, Moneda, MainPage, UserAccount

# Cargar el token desde el archivo config.json
with open('config.json') as file:
    data = json.load(file)
    token = data['token']
app = ApplicationBuilder().token(token).build()

# Define una función para el comando /start con botones en fila
async def start(update: Update, context):
    user_id = update.message.from_user.id
    username = update.message.from_user.name

    # Verifica si el usuario ya está en la base de datos
    if not ManageBD.checkUser(user_id):
        ManageBD.add_user(user_id, username, None, None)

    # Verifica si ya tiene un idioma seleccionado y si no, muestra la selección de idioma
    if not ManageBD.checkLanguage(user_id):
        await Language.selectLanguage(update, context)
        return

    # Verifica si ya tiene una moneda seleccionada y si no, muestra la selección de moneda
    if not ManageBD.checkCurrency(user_id):
        await Moneda.selectCurrency(update, context)

    # Si ya tiene un idioma, muestra la página principal en ese idioma
    if ManageBD.getLanguage(user_id) == 'es':
        await MainPage.MainPageESP(update, context)
    else:
        await MainPage.MainPageENG(update, context)


async def help(update: Update, context):
    user_id = update.message.from_user.id
    if ManageBD.getLanguage(user_id) == 'es':
        await update.message.reply_text(ManageBD.getPrompt("es", "help_msg"))
    else:
        await update.message.reply_text(ManageBD.getPrompt("en", "help_msg"))

                                        
# Define una función que maneje los mensajes de texto
async def echo(update: Update, context):
    message_text = update.message.text
    user_id = update.message.from_user.id
    username = update.message.from_user.name

    if message_text == "Español 🇪🇸":
        ManageBD.updateLanguage(user_id, 'es')
        await update.message.reply_text('Idioma actualizado a Español 🇪🇸')
        if not ManageBD.checkCurrency(user_id):
            await Moneda.selectCurrency(update, context)
        else:
            await MainPage.MainPageESP(update, context)
    elif message_text == "English 🇬🇧":
        ManageBD.updateLanguage(user_id, 'en')
        await update.message.reply_text('Language updated to English 🇬🇧')
        if not ManageBD.checkCurrency(user_id):
            await Moneda.selectCurrency(update, context)
        else:
            await MainPage.MainPageENG(update, context)
    
    elif message_text == "EUR €":
        ManageBD.updateCurrency(user_id, 'EUR')
        await update.message.reply_text('Currency updated to EUR €.')
        if not ManageBD.checkLanguage(user_id):
            await Language.selectLanguage(update, context)
        else:
            if ManageBD.getLanguage(user_id) == 'es':
                await MainPage.MainPageESP(update, context)
            else:
                await MainPage.MainPageENG(update, context)

    elif message_text == "USD $":
        ManageBD.updateCurrency(user_id, 'USD')
        await update.message.reply_text('Currency updated to USD $.')
        if not ManageBD.checkLanguage(user_id):
            await Language.selectLanguage(update, context)
        else:
            if ManageBD.getLanguage(user_id) == 'es':
                await MainPage.MainPageESP(update, context)
            else:
                await MainPage.MainPageENG(update, context)


    # User configuration
    elif message_text == "Cuenta" or message_text == "Account":
        await UserAccount.userProfile(update, context)
        if ManageBD.getLanguage(user_id) == 'es':
            await UserAccount.configPageESP(update, context)
        else:
            await UserAccount.configPageENG(update, context)
    elif message_text == "Idioma" or message_text == "Language":
        await Language.selectLanguage(update, context)
    elif message_text == "Divisa" or message_text == "Currency":
        await Moneda.selectCurrency(update, context)
    elif message_text == "Volver" or message_text == "Back":
        await start(update, context)
    
    # # Alerts
    # elif message_text == "Alertas" or message_text == "Alerts":
    #     await UserAccount.userProfile(update, context)
    #     if ManageBD.getLanguage(user_id) == 'es':
    #         await Alerts.alertsPageESP(update, context)
    #     else:
    #         await Alerts.AlertsPageENG(update, context)

app.bot.send_message

#Ejecucion del bot
if __name__ == '__main__':
    
    #slash commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    #botones
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("El bot está en línea y listo para recibir mensajes.")
    #Ejecutar el bot
    app.run_polling(close_loop=False)