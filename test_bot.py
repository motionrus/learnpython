from telegram.ext import Updater
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='bot.log')

updater = Updater(token='453036603:AAHyXYs4bS2IDAozukdfazzAwIwdulawt6Q')
dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
    print(args)
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text= 'unknown command')

from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

from telegram.ext import MessageHandler, Filters
unknown = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown)

updater.start_polling()
updater.idle()
