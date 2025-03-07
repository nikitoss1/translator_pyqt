from googletrans import Translator


class ModelTranslate:

    def __init__(self):
        self.__translator = Translator()

    def translate_text(
        self, target_text: str, target_lang: str, source_lang: str = "auto"
    ) -> dict:
        try:
            translated_text = self.__translator.translate(
                target_text, dest=target_lang, src=source_lang
            )
            return {
                "translate": translated_text,
                "source_lang": translated_text.src,
                "target_lang": translated_text.dest,
            }
        except Exception as e:
            return {"message": "Произошла ошибка при переводе текста", "error": str(e)}

    def detected_language(self, text: str) -> str:
        detected = self.__translator.detect(text)
        return detected


if __name__ == '__main__':
    o = ModelTranslate()
    print(o.translate_text('Hello', 'ru')['translate'].text)