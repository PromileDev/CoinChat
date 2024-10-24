from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, ConversationHandler
from telegram.ext import filters  # Importar filters de la manera correcta

# Define los estados
CAPTURANDO_ENTRADA = range(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Ejecutaré una función y luego capturaré tu entrada. Por favor, escríbelo después.")
    # Aquí ejecutas tu función
    await my_function()
    # Cambia al estado CAPTURANDO_ENTRADA
    return CAPTURANDO_ENTRADA

async def my_function():
    # Simula una función que ejecuta algo
    print("Función ejecutada.")

async def capture_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    await update.message.reply_text(f"Has escrito: {user_input}")
    # Termina la conversación
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cancelado.")
    return ConversationHandler.END

def main():
    app = ApplicationBuilder().token("7608695401:AAH1BpFdrUKDtKgTvCX2chcr4vm5-qUcUso").build()

    # Configura el manejador de conversación
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CAPTURANDO_ENTRADA: [MessageHandler(filters.TEXT & ~filters.COMMAND, capture_input)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    app.add_handler(conv_handler)

    app.run_polling()

if __name__ == '__main__':
    main()
