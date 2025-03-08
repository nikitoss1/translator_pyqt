from model.model_translate import ModelTranslate
from view.view_translate import ViewTranslate
from config.constants import LANGUAGES
from config.condition import Condition


class PresenterTranslate:

    def __init__(self, model: ModelTranslate, view: ViewTranslate):
        self.model = model
        self.view = view
        self.view.connectSignals(self)

    def translate_text(self):
        text = self.view.current_text()
        current_source_lang = LANGUAGES[self.view.current_source_lang()]
        current_target_lang = LANGUAGES[self.view.current_target_lang()]
        translated_text = self.model.translate_text(
            text, current_target_lang, current_source_lang
        )
        if translated_text["error"] is not None:
            self.view.message(Condition.ERROR, "Проверьте соединение с интернетом")
        else:
            self.view.write_translate_in_browser(translated_text["translate"].text)
