import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import io
from dotenv import load_dotenv
import os
from datetime import datetime
from cogs import ManageBD

async def chart_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Datos de ejemplo
    x_values = []
    y_values = []
    for i in ManageBD.get_history_price("XBTEUR"):
        x_values.append(i[1])
        y_values.append(i[0])
    x_dates = [datetime.strptime(date, '%d/%m/%Y:%H:%M') for date in x_values]


    # Crear gráfico
    plt.figure()
    plt.plot(x_dates, y_values, marker='o', linestyle='-', color='b')  # Gráfico de línea
    plt.title('Valor del bitcoin en los últimos 4 dias')
    plt.xlabel('Horas')
    plt.ylabel('Valor en EUR')

    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y:%H:%M'))
    plt.tight_layout()

    # Guardar el gráfico en un buffer de memoria
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Enviar el gráfico al usuario
    await update.message.reply_photo(photo=buf)

if __name__ == '__main__':
    token = os.getenv('API_TOKEN')
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("chart", chart_command))
    app.run_polling()
