from sqlalchemy.orm import Session
from typing import List, Optional
from models import Book  
from repositories.contracts import IBookRepository, RepositoryBase  

class BookRepository(RepositoryBase[Book], IBookRepository):
    def __init__(self, context: Session):
        super().__init__(context)

    def create_one_book(self, book: Book):
        self.create(book)
        self._context.commit()

    def delete_one_book(self, book: Book):
        self.delete(book)
        self._context.commit()

    def get_all_books(self, track_changes: bool) -> List[Book]:
        return self.find_all(track_changes)

    def get_one_book_by_id(self, id: int, track_changes: bool) -> Optional[Book]:
        return self.find_by_condition(Book.id == id, track_changes).first()

    def update_one_book(self, book: Book):
        self.update(book)
        self._context.commit()
