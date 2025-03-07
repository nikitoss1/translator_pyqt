import unittest
from model.user_translate import UserTranslate

class TestUserTranslate(unittest.TestCase):

    def setUp(self):
        self.translator = UserTranslate()

    
    def test_translate_text(self):
        result = self.translator.translate_text("Hello", target_lang='ru', source_lang='en')
        self.assertEqual(result['translate'].text, 'Привет')  # Теперь это строка


    def test_translate_text_without_source_lang(self):
        result = self.translator.translate_text("Hello", target_lang='ru')
        self.assertEqual(result['translate'].text, 'Привет')

    
    def test_translate_long_text(self):
        text = 'Hello. My name is Nikita. I\'m 22 y.o.'
        translate = 'Привет. Меня зовут Никита. Мне 22 года.'
        result = self.translator.translate_text(text, target_lang='ru')
        self.assertEqual(result['translate'].text, translate)


    def test_detected_lang(self):
        target_lang = 'en'
        text = 'Hello. My name is John!'
        result = self.translator.detected_language(text)
        self.assertEqual(target_lang, result.lang)

    
    def test_detected_lang_de(self):
        target_lang = 'de'
        text = 'Hallo, ich heiße John.!'
        result = self.translator.detected_language(text)
        self.assertEqual(target_lang, result.lang)