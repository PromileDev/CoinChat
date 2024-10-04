import json
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from cogs import ManageBD, Language, Moneda, ManageAPI, MainPage, UserAccount

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
        await update.message.reply_text('''
👋 ¡Bienvenido a nuestro bot de Telegram!
Este bot ofrece dos funciones principales para ayudarte a seguir el mercado de criptomonedas:

Consulta de precios en tiempo real: Puedes solicitar el precio actual de estas criptomoneda: Bitcoin (BTC) o Ethereum (ETH), y el bot te mostrará el valor en monedas populares como USD o EUR.

Alertas automáticas de precios: Configura alertas para tu criptomoneda preferida. Solo necesitas establecer un precio objetivo, y te enviaremos una notificación cuando se alcance.

Comienza ahora eligiendo cuál de las dos funciones principales quieres hacer.
''')

    else:
        await update.message.reply_text('''
👋 Welcome to our Telegram bot!
This bot offers two main features to help you track the cryptocurrency market:

Real-time price check: You can request the current price of this cryptocurrency: Bitcoin (BTC) or Ethereum (ETH), and the bot will show you the value in popular currencies like USD or EUR.

Automatic price alerts: Set up alerts for your preferred cryptocurrency. Just choose a target price, and we'll notify you when it's reached.

Start now by choosing which of the two main features you'd like to use.
 ''')
                                        
# Define una función que maneje los mensajes de texto
async def echo(update: Update, context):
    # Obtener el texto del mensaje, el ID de usuario y el nombre de usuario
    message_text = update.message.text
    user_id = update.message.from_user.id
    username = update.message.from_user.name

    # seleccionar Idioma
    if message_text == "Español 🇪🇸":
        ManageBD.upDateLanguage(user_id, 'es')
        await update.message.reply_text('Idioma actualizado a Español 🇪🇸')
        # Verifica si ya tiene una moneda seleccionada y si no, muestra la selección de moneda
        if not ManageBD.checkCurrency(user_id):
            await Moneda.selectCurrency(update, context)
        else:
            await MainPage.MainPageESP(update, context)
    elif message_text == "English 🏴󠁧󠁢󠁥󠁮󠁧󠁿":
        ManageBD.upDateLanguage(user_id, 'en')
        await update.message.reply_text('Language update to English 🏴󠁧󠁢󠁥󠁮󠁧󠁿')
        # Verifica si ya tiene una moneda seleccionada y si no, muestra la selección de moneda
        if not ManageBD.checkCurrency(user_id):
            await Moneda.selectCurrency(update, context)
        else:
            await MainPage.MainPageENG(update, context)
    
    
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




#Ejecucion del bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(token).build()
    #slash commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    #botones
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("El bot está en línea y listo para recibir mensajes.")
    #Ejecutar el bot
    app.run_polling()