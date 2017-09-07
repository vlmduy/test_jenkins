"""
db.py: Manage DB Connection
Copyright 2017-2018 LinhHo Training.
"""

from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from src.config import config

config_data = config.load_config()
sql_config = config_data['sql']
url = '{}://{}:{}@{}:{}/{}'

# url = url.format(sql_config['type'], sql_config['username'],
#                  sql_config['password'], sql_config['host'],
#                  sql_config['port'], sql_config['database'])
# url = "postgresql+psycopg2://postgres:123456@192.168.210.84:5432/training"
url = 'mysql+pymysql://root:Innovatube731442@35.187.101.71:3306/linh_clone'
engine = create_engine(url)
# engine = None

Base = declarative_base()
_session = scoped_session(sessionmaker(bind=engine, autoflush=True))
# _session = None

# def create_engine(_url):
#     """
#     Init database engine connection
#     :param connection_string:
#     :return: connection engine object
#     """
#     global engine, _session
#     engine = create_engine(_url)
#     _session = scoped_session(sessionmaker(bind=engine, autoflush=True))
#     # install listener to refresh stale connections
#     @event.listens_for(engine, "engine_connect")
#     def ping_connection(connection, branch):
#         if branch:
#             # "branch" refers to a sub-connection of a connection,
#             # we don't want to bother pinging on these.
#             return

#         # turn off "close with result".  This flag is only used with
#         # "connectionless" execution, otherwise will be False in any case
#         save_should_close_with_result = connection.should_close_with_result
#         connection.should_close_with_result = False

#         try:
#             # run a SELECT 1.   use a core select() so that
#             # the SELECT of a scalar value without a table is
#             # appropriately formatted for the backend
#             connection.scalar(select([1]))
#         except exc.DBAPIError as err:
#             # catch SQLAlchemy's DBAPIError, which is a wrapper
#             # for the DBAPI's exception.  It includes a .connection_invalidated
#             # attribute which specifies if this connection is a "disconnect"
#             # condition, which is based on inspection of the original exception
#             # by the dialect in use.
#             if err.connection_invalidated:
#                 # run the same SELECT again - the connection will re-validate
#                 # itself and establish a new connection.  The disconnect detection
#                 # here also causes the whole connection pool to be invalidated
#                 # so that all stale connections are discarded.
#                 connection.scalar(select([1]))
#             else:
#                 raise
#         finally:
#             # restore "close with result"
#             connection.should_close_with_result = save_should_close_with_result

#     return engine

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
