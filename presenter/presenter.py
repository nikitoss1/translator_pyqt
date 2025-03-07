from model.model_translate import ModelTranslate
from view.view_translate import ViewTranslate
from config.config import LANGUAGES

class PresenterTranslate:

    def __init__(self, model: ModelTranslate, view: ViewTranslate):
        self.model = model
        self.view = view
        self.view.connectSignals(self)  # Подключаем сигналы

    def translate_text(self):
        text = self.view.current_text()
        current_source_lang = LANGUAGES[self.view.current_source_lang()]
        current_target_lang = LANGUAGES[self.view.current_target_lang()]
        translated_text = self.model.translate_text(text, current_target_lang, current_source_lang)
        print(translated_text)
        self.view.write_translate_in_browser(translated_text['translate'].text)
