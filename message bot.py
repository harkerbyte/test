

import os 
import time
import telebot

API_KEY = os.getenv('1969279863:AAF-4vEZjTW-j2sGyYyyOLuYDaO2NoFqphO')
bot =telebot.Telebot('1969279863:AAF-4vEZjTW-j2sGyYyyOLuYDaO2NoFqphO')

@bot.message_handler(commands=["start"])
def = start(message):    
    bot.reply_to(message, "hey im glad you are here")

@bot.message_handler(commands=["test"])
def = test(message):    
    bot.reply_to(message, "hey im glad you are here")

bot.polling()