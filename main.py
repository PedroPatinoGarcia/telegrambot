import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from modules.api.tablas import *
from modules.api.meteorologica import *
from modules.api.apod import *
from modules.api.chucknorris import *
from modules.api.perro import *
from modules.convert.csvORjson import *
from modules.scrapping.diario import *
from modules.scrapping.cartelera import *
from modules.bbdd.inferno import *


# Authentication to manage the bot
import os

token_file_path = "docs/token.txt"

try:
    with open(token_file_path, "r") as file:
        TOKEN = file.read().strip()
except FileNotFoundError:
    print(f'No se encontró el archivo {token_file_path}. Proporcione el archivo de token adecuado.')
    exit(1)

if not TOKEN:
    print('Indica la variable TOKEN')
    print('docker run --rm -e TOKEN=tu_token "nombrebot"')
    exit(1)

    
# Show logs in terminal
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# This function responds to start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Que tal amigo, estamos funcionando!")

# This function responds to echo handler
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    
async def table7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=tabla_del_7()) 

async def informe_tiempo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ciudad_predefinida = 'A Coruña'
    api_key_openweather = 'da045a14d2569ca4174024534a757ed8'
    informe_meteorologico = obtener_informe_meteorologico(ciudad_predefinida, api_key_openweather)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=informe_meteorologico)

async def obtener_apod(update: Update, context: ContextTypes.DEFAULT_TYPE):
    api_key_nasa = 'lt6l5JzgNDqzuR6M8ZYNpJSUEUdYG9BAuV3eAoZF'      
    apod = obtener_apod_nasa(api_key_nasa)

    if apod:
        titulo, descripcion, url_imagen = apod
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Título: {titulo}\nDescripción: {descripcion}')

        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=url_imagen)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Error al obtener la APOD')

async def chistecito(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chiste_buenisimo = obtener_chiste()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=chiste_buenisimo)

async def perro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    imagen_perro = obtener_imagen_perro()

    if imagen_perro is not None:
        mensaje = f"Un colega: {imagen_perro}"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=mensaje)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No se pudo obtener una imagen de perro.")


async def csv2json(update, context):
    try:
        file = await context.bot.get_file(update.message.document.file_id)
        filename = update.message.document.file_name
        downloaded_file_path = os.path.join(os.getcwd(), filename)
        await file.download_to_drive(custom_path=downloaded_file_path)
        tipo, response, converted_file_path = csv_file(downloaded_file_path)

        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

        if os.path.isfile(converted_file_path):
            converted_file = open(converted_file_path, "rb")
            await context.bot.send_document(chat_id=update.effective_chat.id, document=converted_file)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Error al enviar el documento.")

    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Error: {str(e)}")

        
async def diario(update: Update, context: ContextTypes.DEFAULT_TYPE):
    titulares_diario = obtener_diario()

    if titulares_diario:
        mensaje = '\n\n'.join(titulares_diario)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=mensaje, parse_mode='HTML')
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No se encontraron titulares.")


async def cartelera(update: Update, context: ContextTypes.DEFAULT_TYPE):
    YelmoCines = obtener_cartelera()
    
    if YelmoCines:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=YelmoCines, parse_mode='HTML')
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No se encontraron películas.")



async def inferno(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=destino('Pedro'))


if __name__ == '__main__':
    # Start the application to operate the bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Handler to manage the start command
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    # Handler to manage text messages
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    
    table7_handler = CommandHandler('table7', table7)
    application.add_handler(table7_handler)

    informe_tiempo_handler = CommandHandler('tiempo', informe_tiempo)
    application.add_handler(informe_tiempo_handler)

    obtener_apod_handler = CommandHandler('apod', obtener_apod)
    application.add_handler(obtener_apod_handler)

    chistecito_handler = CommandHandler('txistaco', chistecito)
    application.add_handler(chistecito_handler)

    perro_handler = CommandHandler('perro', perro)
    application.add_handler(perro_handler)

    application.add_handler(MessageHandler(filters.Document.ALL, csv2json))

    dxt_handler = CommandHandler('diario', diario)
    application.add_handler(dxt_handler)

    cartelera_handler = CommandHandler('cartelera', cartelera)
    application.add_handler(cartelera_handler)

    bbdd_handler = CommandHandler('inferno', inferno)
    application.add_handler(bbdd_handler)
    
    # Keeps the application running
    application.run_polling()