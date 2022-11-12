import requests
import unittest
from parameterized import parameterized

from hw_6 import TOKEN_ya, func_create_folder_ya
from tests.fixtures import *


class TestFunction(unittest.TestCase):

    @parameterized.expand(FIXTURES_YA)
    def test_create_folder(self, name, exp_code):
        '''тестируем статус-код при создании папки'''
        result = func_create_folder_ya(TOKEN_ya, name)
        self.assertEqual(exp_code, result)

        '''чистим диск от тестовых папок'''
        if exp_code == 201:
            url = 'https://cloud-api.yandex.net/v1/disk/resources'
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'OAuth {TOKEN_ya}'
            }
            create_folder_params = {
                'path': f"disk:/{name}"
            }
            response = requests.delete(url, params=create_folder_params, headers=headers)

    @parameterized.expand(FIXTURES_YA_FAIL)
    @unittest.expectedFailure
    def test_create_folder_failure(self, name):
        '''проверяем на предполагаемые ошибки'''
        result = func_create_folder_ya(TOKEN_ya, name)
        self.assertEqual(201, result)