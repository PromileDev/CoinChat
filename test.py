from PIL import Image, ImageDraw, ImageFont
from telegram import InputFile
from telegram.ext import ApplicationBuilder, CommandHandler
from dotenv import load_dotenv
import os

# Función para generar la imagen con texto
def generate_image():
    # Abre la plantilla
    image_path = "btc_price.png"
    image = Image.open(image_path)

    # Configuración del texto
    text = "10.000€"
    font_size = 100  # Ajusta el tamaño según tu imagen y preferencias
    font = ImageFont.truetype("arial.ttf", font_size)  # Asegúrate de tener la fuente Arial o cambia a otra

    # Dibuja el texto en el centro
    draw = ImageDraw.Draw(image)
    # Usa textbbox() en lugar de textsize()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (image.width - text_width) / 2
    y = (image.height - text_height) / 2
    draw.text((x, y), text, font=font, fill="black")  # Cambia el color de texto si deseas

    # Guarda la imagen
    image.save("btc_price_with_text.png")
    return "btc_price_with_text.png"

# Función para enviar la imagen por el bot de Telegram
async def send_image(update, context):
    # Genera la imagen
    image_path = generate_image()

    # Envía la imagen al usuario
    chat_id = update.message.chat_id
    with open(image_path, 'rb') as image_file:
        await context.bot.send_photo(chat_id=chat_id, photo=image_file)

# Inicializa el bot
def main():
    # Cargar el token del archivo .env
    load_dotenv()  # Cargar las variables de entorno del archivo .env
    bot_token = os.getenv('API_TOKEN')

    # Crea la aplicación de Telegram usando ApplicationBuilder
    application = ApplicationBuilder().token(bot_token).build()

    # Comando para enviar la imagen
    application.add_handler(CommandHandler("sendimage", send_image))

    # Inicia el bot
    application.run_polling()

if __name__ == '__main__':
    main()
