import logging
from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine import Engine
from sqlalchemy_utils import create_database, database_exists


logger = logging.getLogger(__name__)


DB_URL = 'postgresql://{user}:{password}@{host}:{port}/{db_name}'


def get_db_connection_str(user: str, password: str, host: str, port: str, db_name: str) -> str:
    return DB_URL.format(
        user=user, password=password, host=host, port=port, db_name=db_name,
    )


def get_engine() -> Engine:
    url = get_db_connection_str(
        user='admin',
        password='example',
        host='db',
        port='5432',
        db_name='my_database',
    )
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url)
    return engine


@lru_cache
def get_sessionmaker() -> sessionmaker:
    return sessionmaker(bind=get_engine(), autocommit=False, autoflush=False)


class DBSession:

    def __enter__(self) -> Session:
        sessionmaker = get_sessionmaker()
        self.session: Session = sessionmaker()        
        logger.info('connected successfully')
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        logger.info('connection closed')
        if self.session:
            self.session.close()


Base = declarative_base()


def create_all_tables() -> None:
    logger.info('all tables created')
    Base.metadata.create_all(get_engine())
