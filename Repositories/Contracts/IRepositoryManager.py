from abc import ABC, abstractmethod
from typing import Protocol

class IBookRepository(Protocol):
    pass

class IRepositoryManager(ABC):
    @property
    @abstractmethod
    def book(self) -> IBookRepository:
        """Return an instance of IBookRepository."""
        pass

    @abstractmethod
    def save(self):
        """Save changes to the database."""
        pass
