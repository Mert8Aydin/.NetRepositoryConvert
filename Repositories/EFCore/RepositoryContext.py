from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import declarative_base
from models import Book  # Kitap modelinizi içe aktarın
from config import BookConfig  # Konfigürasyonunuzu içe aktarın

Base = declarative_base()

class RepositoryContext:
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        self.Base = Base
        self.configure_models()

    def configure_models(self):
        # Kitap modelinin konfigürasyonunu uygulayın
        BookConfig(self.Base.metadata)
        
    def create_all(self):
        # Tüm veritabanı tablolarını oluşturun
        self.Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()

    def close(self):
        self.Session.remove()

# config.py içinde BookConfig'i şu şekilde tanımlayabilirsiniz:

class BookConfig:
    def __init__(self, metadata):
        # Burada Book modelinizin yapılandırmasını yapabilirsiniz
        # Örneğin:
        Book.__table_args__ = {'schema': 'your_schema'}
        metadata.create_all(self.engine)
