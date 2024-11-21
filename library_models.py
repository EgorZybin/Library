import json
import os


class Book:
    """
        Класс Book представляет модель книги.
    """
    def __init__(self, id, title, author, year, status="в наличии"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }


class Library:
    """
        Класс Library представляет модель библиотеки.
    """
    def __init__(self, filename='library.json'):
        """
            Инициализация библиотеки.
        """
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        """
            Функция загружает книги из файла.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return [Book(**data) for data in json.load(f)]
        return []

    def save_books(self):
        """
            Функция сохраняет книги в файл.
        """
        with open(self.filename, 'w') as f:
            json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        """
            Функция добавляет книгу в библиотеку.
        """
        new_id = len(self.books) + 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self.save_books()

    def delete_book(self, book_id):
        """
            Функция удаляет книгу из библиотеки.
        """
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                return
        print(f'Книга с ID {book_id} не найдена.')

    def find_books(self, keyword):
        """
            Функция ищет книги по заголовку, автору или году выпуска.
        """
        found_books = [book for book in self.books if (keyword.lower() in book.title.lower()) or (keyword.lower() in book.author.lower()) or (keyword == str(book.year))]
        if found_books:
            for book in found_books:
                print(f'{book.id}: {book.title} - {book.author} ({book.year}) [Статус: {book.status}]')
        else:
            print('Книги не найдены.')

    def display_books(self):
        """
            Функция отображает все книги в библиотеке.
        """
        if not self.books:
            print('Библиотека пуста.')
            return
        for book in self.books:
            print(f'{book.id}: {book.title} - {book.author} ({book.year}) [Статус: {book.status}]')

    def change_status(self, book_id, new_status):
        """
            Функция изменяет статус книги на указанный пользователем.
        """
        for book in self.books:
            if book.id == book_id:
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_books()
                    return
                else:
                    print('Неверный статус. Доступные статусы: "в наличии", "выдана".')
                    return
        print(f'Книга с ID {book_id} не найдена.')