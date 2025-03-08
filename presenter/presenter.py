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
from config.constants import LANGUAGES_SOURCE, LANGUAGES_TARGET
from config.condition import Condition


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
        if translated_object["error"] is not None:
            self.view.message(Condition.ERROR, "Проверьте соединение с интернетом")
            logging.info('Приложение не отвечает. Нет интернета.')
        else:
            translated_text = translated_object["translate"].text
            logging.info(f'Текст: {text} ({translated_object["source_lang"]}); Перевод: {translated_text} ({current_target_lang})')
            self.view.write_translate_in_browser(translated_text)
