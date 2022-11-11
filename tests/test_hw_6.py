from unittest.mock import patch, Mock
from unittest import TestCase
import hw_6
import unittest


class TestFunctions(unittest.TestCase):

    @patch('builtins.input', return_value='10006')
    def test_people(self, mock_input):
        result = hw_6.people()
        self.assertEqual('Владелец: Аристарх Павлов', result)

    @patch('builtins.input', return_value='11-2')
    def test_shelf(self, mock_input):
        result = hw_6.shelf()
        self.assertEqual('Документ находится на полке № 1', result)

    @patch('builtins.input', return_value='3, id, 222, Абырвалг')
    def test_add(self, mock_input):
        result = hw_6.add()
        self.assertEqual('Документ номер 222 успешно добавлен на полку 3!', result)

    @patch('builtins.input', return_value='222')
    def test_delete_doc(self, mock_input):
        result = hw_6.delete_doc()
        self.assertEqual('Вы удалили документ "222" из каталога и полки архива', result)

    def test_list(self):
        result = hw_6.list_()
        self.assertEqual('passport "2207 876234" "Василий Гупкин",invoice "11-2" "Геннадий Покемонов",'
                         'insurance "10006" "Аристарх Павлов"', result)




