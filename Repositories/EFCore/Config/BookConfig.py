from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Float)

# Database URL
DATABASE_URL = "sqlite:///local.db"  

# Engine ve Session oluşturma
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def initialize_database():
    # Tabloları oluştur
    Base.metadata.create_all(engine)
    
    # Başlangıç verilerini ekle
    initial_books = [
        Book(id=1, title="Karagöz ve Hacivat", price=75),
        Book(id=2, title="Nutuk", price=275),
        Book(id=3, title="Kara Tren", price=375)
    ]
    
    # Verileri ekleyin
    with session.begin():
        session.add_all(initial_books)

if __name__ == "__main__":
    initialize_database()
