import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from tablas import *
from meteorologica import *


# Authentication to manage the bot
import os
# TOKEN = os.getenv('TOKEN')
TOKEN = ('6669467366:AAHzFN8k4CEIJW4SxLwz8j-83Xqk0AhPvMY')

if TOKEN==None:
    print('Indica la variable TOKEN')
    print('docker run --rm -e TOKEN-tu_token "nombrebot"')
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

# Agrega el nuevo manejador al código principal


    
# function
async def afirmador(update, context):
    file = await context.bot.get_file(update.message.document)
    filename = update.message.document.file_name
    await file.download_to_drive(filename)
  
   # envía ficheiro de resposta
    answer = open('resposta.txt', "rb")
    await context.bot.send_document(chat_id=update.effective_chat.id, document=answer)

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
    
    #handler
    application.add_handler(MessageHandler(filters.Document.ALL, afirmador))
    
    # Keeps the application running
    application.run_polling()