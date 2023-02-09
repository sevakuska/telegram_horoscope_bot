import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from core.database.models import Base
from core.settings import database_settings


class _Database:
    def __init__(self, engine_type: str, database_name: str):
        self.engine_type = engine_type
        self.database_name = database_name
        self.engine = create_engine(f'{engine_type}:///{database_name}')
        self.sessionmaker = sessionmaker(bind=self.engine)

    def exists(self) -> bool:
        return os.path.exists(self.database_name)

    def create_database(self) -> None:
        Base.metadata.create_all(bind=self.engine)

    def get_session(self) -> Session:
        return self.sessionmaker()


database = _Database(
    database_settings.engine_type,
    database_settings.database_name
)
