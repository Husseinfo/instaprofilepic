#!/usr/bin/env python3

import time

from telepot import Bot, glance
from instgram_photo import get_profile_pic


def handle(msg):
    content_type, chat_type, chat_id = glance(msg)

    # refuse non-text inputs
    if content_type != 'text':
        bot.sendMessage(chat_id, 'Only text is allowed!')
        return

    # reply to start command
    if msg['text'] == START_COMMAND:
        bot.sendMessage(chat_id, 'Enter an Instagram username to fetch the full resolution profile picture! \n\n\nBy: @Husseinfo')
        return

    # return profile picture
    result = get_profile_pic(msg['text'])
    bot.sendMessage(chat_id, result if result else 'Error occurred!')


if __name__ == "__main__":
    TOKEN = 'TELEGRAM_BOT_TOKEN'
    START_COMMAND = '/start'
    bot = Bot(TOKEN)
    bot.message_loop(handle)

    # Keep the program running
    while True:
        time.sleep(10)
