import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='./logger/app.log',
    filemode='a'
)
from telegram import Bot
from telegram.error import TelegramError
from tokens.tokens import TOKEN, CHAT_ID

bot = Bot(token=TOKEN)

def send_to_telegram(message: str):
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
        logging.info("Сообщение отправлено в Telegram.")
    except TelegramError as e:
        logging.error(f"Ошибка при отправке сообщения в Telegram: {e}")
