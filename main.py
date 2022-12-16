# This is a sample Python bot.
# import asyncio
# import telegram

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import telegram.ext
# mastrobot_example.py
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from dotenv import load_dotenv
from os import getenv


def send_url(update):
    with open('urls.csv', mode='a') as f:
        f.write(update.message.text + '\n')


# function to handle the /start command
def start(update, context):
    update.message.reply_text("hi there! it's a simplest bot.\nhere is it can:")
    help(update, context)


# function to handle the /help command
def help(update, context):
    update.message.reply_text('type /url for suggest an interesting URL')


def url(update: telegram.Update, context):
    text_received = update.message.text
    if 'url' in (e.type for e in update.message.entities):
        update.message.reply_text(f'URL "{text_received}" received')
        send_url(update)
    else:
        update.message.reply_text(f"it's not URL: {update.message.entities.pop(1)}")


# function to handle errors occured in the dispatche
def error(update, context):
    update.message.reply_text('an error occured')


# function to handle normal text
def text(update, context):
    text_received = update.message.text
    if 'url' in (e.type for e in update.message.entities):
        update.message.reply_text(f'URL "{text_received}" received')
        send_url(update)
    else:
        update.message.reply_text(f'did you said "{text_received}" ?')


def main():
    # create the updater, that will automatically create also a dispatcher and a queue to
    # make them dialoge
    load_dotenv()
    TOKEN = getenv("TOKEN")
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("url", url))

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    # add an handler for errors
    dispatcher.add_error_handler(error)

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
