import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
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

# This function responds to tiempo command handler    
async def informe_tiempo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ciudad_predefinida = 'A Coruña'
    api_key_openweather = 'da045a14d2569ca4174024534a757ed8'
    informe_meteorologico = obtener_informe_meteorologico(ciudad_predefinida, api_key_openweather)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=informe_meteorologico)

# This function responds to apod command handler
async def obtener_apod(update: Update, context: ContextTypes.DEFAULT_TYPE):
    api_key_nasa = 'lt6l5JzgNDqzuR6M8ZYNpJSUEUdYG9BAuV3eAoZF'      
    apod = obtener_apod_nasa(api_key_nasa)
    if apod:
        titulo, descripcion, url_imagen = apod
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Título: {titulo}\nDescripción: {descripcion}')

        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=url_imagen)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Error al obtener la APOD')

# This function responds to txistaco command handler
async def chistecito(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chiste_buenisimo = obtener_chiste()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=chiste_buenisimo)

# This function responds to perro command handler
async def perro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    imagen_perro = obtener_imagen_perro()
    if imagen_perro is not None:
        mensaje = f"Un colega: {imagen_perro}"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=mensaje)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No se pudo obtener una imagen de perro.")

# This function responds to convert command handler
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

# This function responds to diario command handler        
async def diario(update: Update, context: ContextTypes.DEFAULT_TYPE):
    titulares_diario = obtener_diario()
    if titulares_diario:
        mensaje = "📰 **Titulares del día:**\n\n"
        for i, (titulo, enlace) in enumerate(titulares_diario, start=1):
            mensaje += f"{i}. [{titulo}]({enlace})\n"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=mensaje, parse_mode='Markdown')
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No se encontraron titulares.")

# This function responds to cartelera command handler
async def cartelera(update, context):
    cartelera_info = obtener_cartelera()    
    if cartelera_info:
        mensaje = "<b>Cartelera de Películas:</b>\n\n"
        for titulo, enlace in cartelera_info:
            mensaje += f"<a href='{enlace}'>{titulo}</a>\n"        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=mensaje, parse_mode='HTML')
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No se encontraron películas en la cartelera.")

# This function responds to inferno command handler
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
    
    # Handler to manage the tiempo command
    informe_tiempo_handler = CommandHandler('tiempo', informe_tiempo)
    application.add_handler(informe_tiempo_handler)

    # Handler to manage the apod command
    obtener_apod_handler = CommandHandler('apod', obtener_apod)
    application.add_handler(obtener_apod_handler)

    # Handler to manage the txistaco command
    chistecito_handler = CommandHandler('txistaco', chistecito)
    application.add_handler(chistecito_handler)

    # Handler to manage the perro command
    perro_handler = CommandHandler('perro', perro)
    application.add_handler(perro_handler)

    # Handler to manage the csv2json command
    application.add_handler(MessageHandler(filters.Document.ALL, csv2json))

    # Handler to manage the diario command
    diario_handler = CommandHandler('diario', diario)
    application.add_handler(diario_handler)

    # Handler to manage the cartelera command
    cartelera_handler = CommandHandler('cartelera', cartelera)
    application.add_handler(cartelera_handler)

    # Handler to manage the inferno command
    bbdd_handler = CommandHandler('inferno', inferno)
    application.add_handler(bbdd_handler)
    
    # Keeps the application running
    application.run_polling()