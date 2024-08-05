from abc import ABC, abstractmethod
from typing import List, Optional
from models import Book  


class IBookRepository(ABC):
    @abstractmethod
    def get_all_books(self, track_changes: bool) -> List[Book]:
        pass

    @abstractmethod
    def get_one_book_by_id(self, id: int, track_changes: bool) -> Optional[Book]:
        pass

    @abstractmethod
    def create_one_book(self, book: Book):
        pass

    @abstractmethod
    def update_one_book(self, book: Book):
        pass

    @abstractmethod
    def delete_one_book(self, book: Book):
        pass
