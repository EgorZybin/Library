from models.library import Library


def main():
    """
        Главная функция программы.
    """
    library = Library()

    while True:
        try:
            print("""\nДоступные команды:
            1. Добавить книгу
            2. Удалить книгу
            3. Искать книгу
            4. Отобразить все книги
            5. Изменить статус книги    
            6. Выйти""")

            choice = input("Выберите команду: ")

            match choice:

                case '1':
                    library.add_book()
                case '2':
                    library.delete_book()
                case '3':
                    library.find_books()
                case '4':
                    library.display_books()
                case '5':
                    library.change_status()
                case '6':
                    break
                case _:
                    print("Неверная команда. Пожалуйста, попробуйте снова.")
        except ValueError as err:
            print(f"Неправильный ввод. Ошибка: {err}. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
