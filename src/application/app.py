from models.library import Library


class LibraryApp:

    def __init__(self, library: Library):
        self.library = library

    def main(self):
        """
        Главная функция программы.
        """
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
                if not choice:
                    raise ValueError("Ввод не может быть пустым.")

                match choice:

                    case '1':
                        self.library.add_book()
                    case '2':
                        self.library.delete_book()
                    case '3':
                        self.library.find_books()
                    case '4':
                        self.library.display_books()
                    case '5':
                        self.library.change_status()
                    case '6':
                        break
                    case _:
                        print("Неверная команда. Пожалуйста, попробуйте снова.")
            except ValueError as err:
                print(f"Неправильный ввод. Ошибка: {err}. Пожалуйста, попробуйте снова.")
