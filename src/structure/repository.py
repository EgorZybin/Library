from typing import List
from models.book import Book
from models.library import LibraryRepository


class FileRepository(LibraryRepository):
    """Класс для работы с файловым хранилищем книг."""

    def __init__(self, storage_file: str = "../db/library.json"):
        self.storage_file = storage_file

    def load_books(self) -> List[Book]:
        """Загружает книги из файла."""
        try:
            with open(self.storage_file, "r") as file:
                return [Book for line in file if line.strip()]
        except FileNotFoundError:
            return []

    def save_books(self, books: List[Book]) -> None:
        """Сохраняет книги в файл."""
        with open(self.storage_file, "w") as file:
            for book in books:
                file.write(str(book))
