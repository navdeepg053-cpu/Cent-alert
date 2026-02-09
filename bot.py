import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8327314498:AAHtqV2n9TQzhjj0UTgYNHqdMRbHuCvkKeg"

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    name = update.effective_user.first_name
    await update.message.reply_html(f"👋 <b>Welcome, {name}!</b>\n\n🔑 Your Chat ID:\n<code>{chat_id}</code>\n\n👆 Tap to copy!")
    logger.info(f"User {chat_id} started")

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_html(f"🔑 <code>{chat_id}</code>")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("🤖 <b>Commands:</b>\n/start - Get Chat ID\n/id - Show ID\n/help - Help")

async def handle_any(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_html(f"Your Chat ID: <code>{chat_id}</code>")

def main():
    logger.info("Starting bot...")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("id", get_id))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_any))
    logger.info("Bot running with polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
