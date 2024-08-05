from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic
from sqlalchemy.orm import Session

T = TypeVar('T')

class IRepositoryBase(ABC, Generic[T]):
    @abstractmethod
    def find_all(self, track_changes: bool) -> List[T]:
        pass

    @abstractmethod
    def find_by_condition(self, condition, track_changes: bool) -> List[T]:
        pass

    @abstractmethod
    def create(self, entity: T):
        pass

    @abstractmethod
    def update(self, entity: T):
        pass

    @abstractmethod
    def delete(self, entity: T):
        pass
