
from structure.repository import FileRepository
from models.library import Library
from application.app import LibraryApp

if __name__ == "__main__":
    repository = FileRepository("library.txt")
    library = Library(repository)
    app = LibraryApp(library)
    app.main()
