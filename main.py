from telegram.ext import Updater, CommandHandler
import logging


token_d = "1449579824:AAGBBvapLkt0u3oQbqyedGBxUnLYYWOCGkk"

# Lo primero que definimos es el manejador de Actualizaciones
updater = Updater(token=token_d , use_context=True)

# Conectamos el Updater con el Dispatcher
dispatcher = updater.dispatcher

# Muestra por pantalla diferentes excepciones, en un formato adaptado
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bienvenido a Pyctionariy Bot ")

def english_search(update, context):
    # context.args 
    # recibira la entrada del usuario despues de /b como lista
    # context.bot.send_message(chat_id=update.effective_chat.id, text = "") 
    # para mostrar el mensaja con la definicion

start_handler = CommandHandler('start', start)
start_handler = CommandHandler('b', spanish_search)
start_handler = CommandHandler('s', english_search)
dispatcher.add_handler(start_handler)

updater.start_polling()

