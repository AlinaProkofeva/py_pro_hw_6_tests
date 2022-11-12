from unittest.mock import patch, Mock
import unittest
from parameterized import parameterized

from hw_6 import *
from tests.fixtures import *


class TestFunctions(unittest.TestCase):

    @parameterized.expand(FIXTURES_PEOPLE)
    @patch('builtins.input')
    def test_people(self, mock_input, exp_res, inp):
        '''поиск владельца по номеру документа'''
        inp.return_value = mock_input
        result = people()
        self.assertEqual(exp_res, result)

    @parameterized.expand(FIXTURES_SHELF)
    @patch('builtins.input')
    def test_shelf(self, mock_input, exp_res, inp):
        '''поиск полки по номеру документа'''
        inp.return_value = mock_input
        result = shelf()
        self.assertEqual(exp_res, result)

    @parameterized.expand(FIXTURES_ADD)
    @patch('builtins.input')
    def test_add(self, mock_input, exp_res, inp):
        '''добавление документа'''
        inp.return_value = mock_input
        result = add()
        self.assertEqual(exp_res, result)
    #
    @parameterized.expand(FIXTURES_DEL)
    @patch('builtins.input')
    def test_delete_doc(self, mock_input, exp_res, inp):
        '''удаление документа'''
        inp.return_value = mock_input
        result = delete_doc()
        self.assertEqual(exp_res, result)
    #
    def test_list(self):
        '''просмотр всех документов'''
        result = list_()
        self.assertEqual('passport "2207 876234" "Василий Гупкин",invoice "11-2" "Геннадий Покемонов",'
                         'insurance "10006" "Аристарх Павлов"', result)




