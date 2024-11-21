from library_models import Library


def main():
    """
        Главная функция программы.
    """
    library = Library()

    while True:
        print("\nДоступные команды:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите команду: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, year)
            print("Книга успешно добавлена.")
        elif choice == '2':
            book_id = int(input("Введите ID книги, которую нужно удалить: "))
            library.delete_book(book_id)
            print("Книга успешно удалена.")
        elif choice == '3':
            keyword = input("Введите название, автора или год для поиска: ")
            library.find_books(keyword)
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            book_id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input('Введите новый статус ("в наличии" или "выдана"): ')
            library.change_status(book_id, new_status)
            print("Статус книги успешно изменен.")
        elif choice == '6':
            break
        else:
            print("Неверная команда. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
