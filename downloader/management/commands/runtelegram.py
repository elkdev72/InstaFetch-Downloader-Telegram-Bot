from django.core.management.base import BaseCommand
from downloader.telegram_bot import run_bot

class Command(BaseCommand):
    help = 'Runs the Telegram bot'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting Telegram bot...")
        run_bot()
