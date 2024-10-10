import json
import asyncio
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ConversationHandler, ContextTypes
from cogs import ManageBD, Language, Moneda, MainPage, UserAccount, ManageAPI, PricePage, AlertsPage, ManageAlerts

file_esp = "docs/Términos y Condiciones de Uso.pdf"
file_eng = "docs/Terms and Conditions of Use.pdf"

# Cargar el token desde el archivo config.json
with open('config.json') as file:
    data = json.load(file)
    token = data['token']
app = ApplicationBuilder().token(token).build()


# Define una función para el comando /start con botones en fila
async def start(update: Update, context):
    user_id = update.message.from_user.id
    username = update.message.from_user.name
    context.user_data['current_page'] = 'main'

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

async def terms(update: Update, context):
    user_id = update.message.from_user.id
    if ManageBD.getLanguage(user_id) == 'es':
        await app.bot.sendDocument(chat_id=user_id, document=open(file_esp, 'rb'))
        await MainPage.MainPageESP(update, context)
    else:
        await app.bot.sendDocument(chat_id=user_id, document=open(file_eng, 'rb'))
        await MainPage.MainPageENG(update, context)

async def send_message(update: Update, context, message, user_id):
    await app.bot.sendMessage(chat_id=user_id, text=message)

async def help(update: Update, context):
    user_id = update.message.from_user.id
    if ManageBD.getLanguage(user_id) == 'es':
        await update.message.reply_text(ManageBD.getPrompt("es", "help_msg"))
        await MainPage.MainPageESP(update, context)
    else:
        await update.message.reply_text(ManageBD.getPrompt("en", "help_msg"))
        await MainPage.MainPageENG(update, context)


                                        
# Define una función que maneje los mensajes de texto
async def echo(update: Update, context):
    message_text = update.message.text
    user_id = update.message.from_user.id
    username = update.message.from_user.name

    #Controlar estado actual del bot
    current_page = context.user_data.get('current_page', 'main')  # 'main' es el estado por defecto

    if message_text == "Español 🇪🇸":
        ManageBD.updateLanguage(user_id, 'es')
        await update.message.reply_text(ManageBD.getPrompt("es", "updateL_msg"))
        if not ManageBD.checkCurrency(user_id):
            await Moneda.selectCurrency(update, context)
        else:
            await MainPage.MainPageESP(update, context)
    elif message_text == "English 🇬🇧":
        ManageBD.updateLanguage(user_id, 'en')
        await update.message.reply_text(ManageBD.getPrompt("en", "updateL_msg"))
        if not ManageBD.checkCurrency(user_id):
            await Moneda.selectCurrency(update, context)
        else:
            await MainPage.MainPageENG(update, context)
    
    elif message_text == "EUR €":
        ManageBD.updateCurrency(user_id, 'EUR')
        await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "updateD_msg") + ' EUR €.')
        if not ManageBD.checkLanguage(user_id):
            await Language.selectLanguage(update, context)
        else:
            if ManageBD.getLanguage(user_id) == 'es':
                await MainPage.MainPageESP(update, context)
            else:
                await MainPage.MainPageENG(update, context)

    elif message_text == "USD $":
        ManageBD.updateCurrency(user_id, 'USD')
        await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "updateD_msg") + ' USD $.')
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

    # User Price
    elif message_text == "Price" or message_text == "Precio":
        await PricePage.pagePrice(update, context)
    elif current_page == 'price':
        # El código que ya tienes para mostrar los precios
        if message_text == "Bitcoin":
            currency = ManageBD.getCurrency(user_id)
            try:
                price = ManageAPI.getPriceEUR("XBT") if currency == 'EUR' else ManageAPI.getPriceUSD("XBT")
                await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "priceB_msg") + f' {price} {currency}')
            except Exception as e:
                await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "errorP_msg") + f'{e}')
            await start(update, context)

        elif message_text == "Ethereum":
            currency = ManageBD.getCurrency(user_id)
            try:
                price = ManageAPI.getPriceEUR("ETH") if currency == 'EUR' else ManageAPI.getPriceUSD("ETH")
                await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "priceE_msg") + f' {price} {currency}')
            except Exception as e:
                await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "errorP_msg") + f'{e}')
            await start(update, context)

        elif message_text == "Litecoin":
            currency = ManageBD.getCurrency(user_id)
            try:
                price = ManageAPI.getPriceEUR("LTC") if currency == 'EUR' else ManageAPI.getPriceUSD("LTC")
                await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "priceL_msg") + f' {price} {currency}')
            except Exception as e:
                await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "errorP_msg") + f'{e}')
            await start(update, context)

        elif message_text == "Volver" or message_text == "Back":
            await start(update, context)
        context.user_data['current_page'] = 'main'

    

    # Alerts
    elif message_text == "Alertas" or message_text == "Alerts":
        if ManageBD.getLanguage(user_id) == 'es':
            await AlertsPage.alertsPageESP(update, context)
        else:
            await AlertsPage.alertsPageENG(update, context)
    elif message_text == "Mis alertas" or message_text == "Manage alerts":
        await ManageAlerts.printAlerts(update, context)
    elif message_text == "Nueva Alerta" or message_text == "New Alert":
        await AlertsPage.newAlertPage(update, context)
    elif current_page == 'new_alert':
        user_currency = ManageBD.getCurrency(user_id)
        if message_text == "Bitcoin":
            if user_currency == 'EUR':
                await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "inputTarget_msg"))
                context.user_data['selected_currency'] = 'XBTEUR'
            else:
                await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "inputTarget_msg"))
                context.user_data['selected_currency'] = 'XBTUSD'
        elif message_text == "Ethereum":
            if user_currency == 'EUR':
                await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "inputTarget_msg"))
                context.user_data['selected_currency'] = 'ETHEUR'
            else:
                await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "inputTarget_msg"))
                context.user_data['selected_currency'] = 'ETHUSD'
        elif message_text == "Litecoin":
            if user_currency == 'EUR':
                await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "inputTarget_msg"))
                context.user_data['selected_currency'] = 'LTCEUR'
            else:
                await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "inputTarget_msg"))
                context.user_data['selected_currency'] = 'LTCUSD'
        context.user_data['current_page'] = 'waiting_for_amount'
        return

    elif current_page == 'waiting_for_amount':
        price = message_text
        selected_currency = context.user_data.get('selected_currency')
        ManageBD.addAlert(user_id, selected_currency, price)
        await update.message.reply_text(ManageBD.getPrompt(ManageBD.getLanguage(user_id), "alertConfirm_msg"))
        context.user_data['current_page'] = 'main'
        if ManageBD.getLanguage(user_id) == 'es':
            await MainPage.MainPageESP(update, context)
        else:
            await MainPage.MainPageENG(update, context)

def main():
    app = ApplicationBuilder().token(token).build()

    # Agregar manejadores
    app.add_handler(CallbackQueryHandler(ManageAlerts.button_callback))
    app.add_handler(CommandHandler('start', start))  # Maneja la pulsación de botones
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('terms' , terms))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("El bot está en línea y listo para recibir mensajes.")
    app.run_polling()

if __name__ == '__main__':
    main()