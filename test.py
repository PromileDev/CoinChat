from PIL import Image, ImageDraw, ImageFont
from telegram import InputFile
from telegram.ext import ApplicationBuilder, CommandHandler
from dotenv import load_dotenv
import os
from io import BytesIO  # Importar BytesIO para manejar imágenes en memoria

# Función para generar la imagen con texto
def generate_image():
    # Abre la plantilla
    image_path = "plantilla/btc_price.jpg"
    image = Image.open(image_path)

    # Configuración del texto
    text = "10.000€"
    font_size = 300  # Ajusta el tamaño según tu imagen y preferencias
    font = ImageFont.truetype("font/Geist-Regular.ttf", font_size)  # Asegúrate de tener la fuente o cambia a otra

    # Dibuja el texto en el centro
    draw = ImageDraw.Draw(image)
    # Usa textbbox() en lugar de textsize()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = ((image.width - text_width) / 2) - 450
    y = ((image.height - text_height) / 2) - 100
    draw.text((x, y), text, font=font, fill="#f2c158")  # Cambia el color de texto si deseas

    # Guarda la imagen en memoria (en lugar de guardarla en el disco)
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format="PNG")  # Guarda en formato PNG
    img_byte_arr.seek(0)  # Reposiciona el puntero al inicio del archivo en memoria

    return img_byte_arr

# Función para enviar la imagen por el bot de Telegram
async def send_image(update, context):
    # Genera la imagen en memoria
    img_byte_arr = generate_image()

    # Envía la imagen al usuario
    chat_id = update.message.chat_id
    await context.bot.send_photo(chat_id=chat_id, photo=InputFile(img_byte_arr, filename="btc_price_with_text.png"))

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
