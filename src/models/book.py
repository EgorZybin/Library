from dataclasses import dataclass


@dataclass
class Book:
    """Класс, представляющий книгу в библиотеке."""
    book_id: int  # Уникальный идентификатор книги
    title: str  # Название книги
    author: str  # Автор книги
    year: int  # Год издания книги
    status: str = "в наличии"  # Статус книги (по умолчанию "в наличии")

    def to_dict(self) -> dict:
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }
