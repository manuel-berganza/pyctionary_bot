import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import mainEn
import mainEs

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)


logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Bienvenido a Pyctionary,\n Ejemplo de búqueda: \n Inglés: /s <palabra> \n /s automobile \n ------ \n Español: /b <palabra> \n /b luz \n\n Bot Created By: Gustavo Barboza B. y Manuel Berganza")


def get_en(update: Update, context: CallbackContext):
    update.message.reply_text(mainEn.get_req(context.args[0]))

def get_es(update: Update, context: CallbackContext):
    update.message.reply_text(mainEs.get_req(context.args[0]))


def main():

    updater = Updater("1449579824:AAGBBvapLkt0u3oQbqyedGBxUnLYYWOCGkk", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("s", get_en))
    dispatcher.add_handler(CommandHandler("b", get_es))

    updater.start_polling()

    updater.idle()



if __name__ == '__main__':
    main()
