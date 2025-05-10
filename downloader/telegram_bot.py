from telegram.ext import Application, MessageHandler, filters
from telegram import Update
from django.conf import settings
import os
from downloader.utils import download_instagram_video

async def handle_message(update: Update, context):
    chat_id = update.message.chat_id
    text = update.message.text

    if "instagram.com" in text:
        await update.message.reply_text("Downloading...")

        file_path = download_instagram_video(text)

        if file_path:
            await context.bot.send_video(chat_id=chat_id, video=open(file_path, 'rb'))
            os.remove(file_path)
        else:
            await update.message.reply_text("Failed to download the video.")

def run_bot():
    app = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
