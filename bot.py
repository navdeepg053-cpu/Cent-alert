import os
from telegram.ext import Application

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")   # or os.getenv("TELEGRAM_BOT_TOKEN")
application = Application.builder().token(TOKEN).build()
