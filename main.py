import os
import telebot

bot = telebot.TeleBot("5953671984:AAG9XaarXNDyM0axBHZVTLjtnjwQ6bpIcTE")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello i'm maliyavpn Bot")

@bot.message_handler(command=['Rajith'])
def send_mesaage(message) :
    bot.send_message(message, "Clash Mobitel ⬇️")
    bot.send_message(message, "https://drive.google.com/uc?export=download&id=1BcVvzqniWc29md6_QnePZSuNqMfb2KjP")

    bot.polling()