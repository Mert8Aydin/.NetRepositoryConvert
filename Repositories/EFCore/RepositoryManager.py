from sqlalchemy.orm import Session
from repositories.contracts import IBookRepository
from repositories.efcore import BookRepository  # KitapRepository'yi içe aktarın

class RepositoryManager:
    def __init__(self, context: Session):
        self._context = context
        self._book_repository = None

    @property
    def book(self) -> IBookRepository:
        if self._book_repository is None:
            self._book_repository = BookRepository(self._context)
        return self._book_repository

    def save(self):
        try:
            self._context.commit()
        except Exception as e:
            print(f"Error saving changes: {e}")
            self._context.rollback()
