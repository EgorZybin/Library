import unittest
from unittest.mock import patch

from library.models import Library, Book


class TestLibrary(unittest.TestCase):

    def setUp(self):
        # Создание экземпляра библиотеки для тестирования
        self.library = Library()
        self.library.books = [
            Book(id=1, title="Война и мир", author="Лев Толстой", year=1867, status="в наличии"),
            Book(id=2, title="Анна Каренина", author="Лев Толстой", year=1873, status="выдана"),
            Book(id=3, title="Мёртвые души", author="Николай Гоголь", year=1842, status="в наличии"),
        ]

    @patch('builtins.print')
    def test_find_books_by_title(self, mock_print):
        self.library.find_books("Война и мир")
        mock_print.assert_called_with('1: Война и мир - Лев Толстой (1867) [Статус: в наличии]')

    @patch('builtins.print')
    def test_find_books_by_author(self, mock_print):
        self.library.find_books("Лев Толстой")
        mock_print.assert_called_with('2: Анна Каренина - Лев Толстой (1873) [Статус: выдана]')

    @patch('builtins.print')
    def test_find_books_by_year(self, mock_print):
        self.library.find_books("1842")
        mock_print.assert_called_with('3: Мёртвые души - Николай Гоголь (1842) [Статус: в наличии]')

    @patch('builtins.print')
    def test_find_books_not_found(self, mock_print):
        self.library.find_books("Nonexistent Book")
        mock_print.assert_called_with('Книги не найдены.')

    @patch('builtins.print')
    def test_display_books(self, mock_print):
        self.library.display_books()
        self.assertEqual(mock_print.call_count, 3)
        mock_print.assert_any_call('1: Война и мир - Лев Толстой (1867) [Статус: в наличии]')
        mock_print.assert_any_call('2: Анна Каренина - Лев Толстой (1873) [Статус: выдана]')
        mock_print.assert_any_call('3: Мёртвые души - Николай Гоголь (1842) [Статус: в наличии]')

    @patch('builtins.print')
    def test_display_books_empty(self, mock_print):
        self.library.books = []
        self.library.display_books()
        mock_print.assert_called_once_with('Библиотека пуста.')

    @patch('builtins.print')
    def test_change_status_valid(self, mock_print):
        self.library.change_status(1, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")
        self.library.change_status(1, "в наличии")
        self.assertEqual(self.library.books[0].status, "в наличии")

    @patch('builtins.print')
    def test_change_status_invalid(self, mock_print):
        self.library.change_status(1, "недоступно")
        mock_print.assert_called_once_with('Неверный статус. Доступные статусы: "в наличии", "выдана".')

    @patch('builtins.print')
    def test_change_status_book_not_found(self, mock_print):
        self.library.change_status(999, "в наличии")
        mock_print.assert_called_once_with('Книга с ID 999 не найдена.')


if __name__ == '__main__':
    unittest.main()
