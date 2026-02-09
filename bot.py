import telebot

BOT_TOKEN = "8327314498:AAHtqV2n9TQzhjj0UTgYNHqdMRbHuCvkKeg"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'id'])
def send_id(message):
    bot.reply_to(message, f"Your Chat ID:\n{message.chat.id}")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"Chat ID: {message.chat.id}")

print("Bot starting...")
bot.polling()
