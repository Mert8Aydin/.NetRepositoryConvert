from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import SQLAlchemyError

class RepositoryBase(IRepositoryBase[T], Generic[T]):
    def __init__(self, context: Session):
        self._context = context

    def find_all(self, track_changes: bool) -> List[T]:
        query = self._context.query(T)
        if not track_changes:
            query = query.options(joinedload('*'))
        return query.all()

    def find_by_condition(self, condition, track_changes: bool) -> List[T]:
        query = self._context.query(T).filter(condition)
        if not track_changes:
            query = query.options(joinedload('*'))
        return query.all()

    def create(self, entity: T):
        try:
            self._context.add(entity)
            self._context.commit()
        except SQLAlchemyError as e:
            self._context.rollback()
            raise

    def update(self, entity: T):
        try:
            self._context.merge(entity)
            self._context.commit()
        except SQLAlchemyError as e:
            self._context.rollback()
            raise

    def delete(self, entity: T):
        try:
            self._context.delete(entity)
            self._context.commit()
        except SQLAlchemyError as e:
            self._context.rollback()
            raise
