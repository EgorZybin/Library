import os
import json
from models.book import Book


class Library:
    """
        Класс Library представляет модель библиотеки.
    """

    def __init__(self, filename: str = "../db/library.json") -> None:
        """
            Инициализация библиотеки.
        """
        self.filename: str = filename
        self.books = self.load_books()

    def load_books(self) -> list:
        """
            Функция загружает книги из файла.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return [Book(**data) for data in json.load(f)]
        return []

    def save_books(self) -> None:
        if not os.path.exists(os.path.dirname(self.filename)):
            os.makedirs(os.path.dirname(self.filename))
        with open(self.filename, 'w') as f:
            json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)

    def add_book(self) -> Book:
        """
            Функция добавляет книгу в библиотеку.
        """
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания: ")
        for book in self.books:
            if book.title == title and book.author == author and book.year == year:
                print("Книга уже есть в библиотеке.")
                return
            elif book.year < str(868) or book.year > str(2024):
                print("Год издания должен быть в диапазоне от 868 до 2024.")
                return

        new_id = len(self.books) + 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        print("Книга успешно добавлена.")

    def delete_book(self) -> None:
        """
            Функция удаляет книгу из библиотеки.
        """
        book_id = int(input("Введите ID книги, которую нужно удалить: "))
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.save_books()
                print("Книга успешно удалена.")
                return
        print(f'Книга с ID {book_id} не найдена.')

    def find_books(self,) -> None:
        """
            Функция ищет книги по заголовку, автору или году выпуска.
        """
        keyword = input("Введите название, автора или год для поиска: ")
        found_books = [book for book in self.books if
                       (keyword.lower() in book.title.lower()) or (keyword.lower() in book.author.lower()) or (
                               keyword == str(book.year))]
        if found_books:
            for book in found_books:
                print(f'{book.book_id}: {book.title} - {book.author} ({book.year}) [Статус: {book.status}]')
        else:
            print('Книги не найдены.')

    def display_books(self) -> None:
        """
            Функция отображает все книги в библиотеке.
        """
        if not self.books:
            print('Библиотека пуста.')
            return
        for book in self.books:
            print(f'{book.book_id}: {book.title} - {book.author} ({book.year}) [Статус: {book.status}]')

    def change_status(self) -> None:
        """
            Функция изменяет статус книги на указанный пользователем.
        """
        book_id = int(input("Введите ID книги для изменения статуса: "))
        for book in self.books:
            if book.book_id == book_id:
                new_status = input('Введите новый статус ("в наличии" или "выдана"): ')
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_books()
                    print('Статус книги успешно изменен.')
                    return
                else:
                    print('Неверный статус. Доступные статусы: "в наличии", "выдана".')
                    return
        print(f'Книга с ID {book_id} не найдена.')
