import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='./logger/app.log',
    filemode='a'
)

logging.info("Логирование запущено")

from model.model_translate import ModelTranslate
from view.view_translate import ViewTranslate
from config.constants import LANGUAGES_SOURCE, LANGUAGES_TARGET, REVERSED_DICT_LANGUAGE
from config.condition import Condition
from telegram_bot.telegram_bot import send_to_telegram


class PresenterTranslate:

    def __init__(self, model: ModelTranslate, view: ViewTranslate):
        self.model = model
        self.view = view
        self.view.connectSignals(self)

    def translate_text(self):
        text = self.view.current_text()
        current_source_lang = LANGUAGES_SOURCE[self.view.current_source_lang()]
        current_target_lang = LANGUAGES_TARGET[self.view.current_target_lang()]
        translated_object = self.model.translate_text(
            text, current_target_lang, current_source_lang
        )
        text_message = ''
        if translated_object["error"] is not None:
            text_message = 'Приложение не отвечает. Нет интернета.'
            self.view.message(Condition.ERROR, "Проверьте соединение с интернетом")
            logging.info(text_message)
        else:
            translated_text = translated_object["translate"].text
            text_message = f'Текст: {text} ({translated_object["source_lang"]}); Перевод: {translated_text} ({current_target_lang})'
            logging.info(text_message)
            self.view.write_translate_in_browser(translated_text)
        self.get_last_logger()
        
    
    def detected_language(self, text):
        language = self.model.detected_language(text)
        return REVERSED_DICT_LANGUAGE[language.lang]
         
    def get_last_logger(self):
        filename='./logger/app.log'

        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if lines:
                send_to_telegram(lines[-1].strip())
                return
            return None
        