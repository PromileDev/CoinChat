import json
import asyncio
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from cogs import ManageBD, Language, Moneda, ManageAPI, MainPage, UserAccount, CryptoUpdate

# Cargar el token desde el archivo config.json
with open('config.json') as file:
    data = json.load(file)
    token = data['token']


# Define una función para el comando /start con botones en fila
async def start(update: Update, context):
    # Obtener el ID y el nombre de usuario del usuario
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
    if (ManageBD.getLanguage(user_id) == 'es'):
        await update.message.reply_text(ManageBD.getPrompt("es", "help_msg"))

    else:
        await update.message.reply_text(ManageBD.getPrompt("en", "help_msg"))
                                        
# Define una función que maneje los mensajes de texto
async def echo(update: Update, context):
    # Obtener el texto del mensaje, el ID de usuario y el nombre de usuario
    message_text = update.message.text
    user_id = update.message.from_user.id
    username = update.message.from_user.name

    # seleccionar Idioma
    if message_text == "Español 🇪🇸":
        ManageBD.updateLanguage(user_id, 'es')
        await update.message.reply_text('Idioma actualizado a Español 🇪🇸')
        # Verifica si ya tiene una moneda seleccionada y si no, muestra la selección de moneda
        if not ManageBD.checkCurrency(user_id):
            await Moneda.selectCurrency(update, context)
        else:
            await MainPage.MainPageESP(update, context)
    elif message_text == "English 🏴󠁧󠁢󠁥󠁮󠁧󠁿":
        ManageBD.updateLanguage(user_id, 'en')
        await update.message.reply_text('Language update to English 🏴󠁧󠁢󠁥󠁮󠁧󠁿')
        # Verifica si ya tiene una moneda seleccionada y si no, muestra la selección de moneda
        if not ManageBD.checkCurrency(user_id):
            await Moneda.selectCurrency(update, context)
        else:
            await MainPage.MainPageENG(update, context)
    
    
 # Selección de moneda
    elif message_text == "EUR €":
        ManageBD.updateCurrency(user_id, 'EUR')
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
        ManageBD.updateCurrency(user_id, 'USD')
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
    

    # Página principal
    elif message_text == "Cuenta" or message_text == "Account":
        await UserAccount.userProfile(update, context)
        if ManageBD.getLanguage(user_id) == 'es':
            await UserAccount.configPageESP(update, context)
        else:
            await UserAccount.configPageENG(update, context)



    # Ajustes de cuenta (configuración de idioma y moneda)
    elif message_text == "Idioma" or message_text == "Language":
        await Language.selectLanguage(update, context)
    elif message_text == "Divisa" or message_text == "Currency":
        await Moneda.selectCurrency(update, context)
    elif message_text == "Volver" or message_text == "Back":
        await start(update, context)


async def custom_loop():
    while True:
        CryptoUpdate.update()
        await asyncio.sleep(10)



async def main():
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("El bot está en línea y listo para recibir mensajes.")
    
    # Inicializa la aplicación
    await app.initialize()

    # Ejecuta ambos bucles en paralelo: el de PTB y el personalizado
    await asyncio.gather(app.start(), custom_loop())

    # Finaliza la aplicación
    await app.stop()
    await app.shutdown()

#Ejecucion del bot
if __name__ == '__main__':
    asyncio.run(main())