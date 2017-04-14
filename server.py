#!/usr/bin/env python
import os
import sys
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

if __name__ == "__main__":
    # logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # updater
    updater = Updater(token='TOKEN')
    dispatcher = updater.dispatcher

    # handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

    def start(bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")