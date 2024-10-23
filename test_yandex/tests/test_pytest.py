from unittest import TestCase

from test_yandex.main import create_folder

class Test(TestCase):
    def test_status_code1(self):
        code = 201
        result = create_folder('Фото', token='ваш токен')
        self.assertEqual(code, result)

    def test_status_code2(self):
        code = 409
        result = create_folder('Фото', token='ваш токен')
        self.assertEqual(code, result)

    def test_status_code3(self):
        code = 401
        result = create_folder('Фото', token='')
        self.assertEqual(code, result)

