from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from src.config import config
from contextlib import contextmanager

config_data = config.load_config()
sql_config = config_data['sql']
url = '{}://{}:{}@{}:{}/{}'

url = url.format(sql_config['type'], sql_config['username'],
                 sql_config['password'], sql_config['host'],
                 sql_config['port'], sql_config['database'])
url = "postgresql+psycopg2://postgres:123456@192.168.210.84:5432/training"
engine = create_engine(url)
# engine = None

Base = declarative_base()
_session = scoped_session(sessionmaker(bind=engine, autoflush=True))
# _session = None

# def create_engine(_url):

#     global engine, _session
#     engine = create_engine(_url)
#     _session = scoped_session(sessionmaker(bind=engine, autoflush=True))


@contextmanager
def session(autocommit=False):
    """
    Function to manage session
    :param autocommit:
    :raise Exception:
    """
    if _session is None:
        raise Exception("Database engine not yet initialized. You should call \
                         awfm.db.initialize_engine first")

    session_context = _session()
    session_context.autoflush = True
    try:
        yield session_context
        if autocommit:
            session_context.commit()
    except:
        session_context.rollback()
        raise
    finally:
        session_context.expunge_all()
        session_context.close()
