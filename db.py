from sqlalchemy import *
import config

config_data = config.load_config()
sql_config = config_data['sql']
url = '{}://{}:{}@{}:{}/{}'
url = url.format(sql_config['type'], sql_config['username'],
                 sql_config['password'], sql_config['host'],
                 sql_config['port'], sql_config['database'])
db = create_engine(url)
db.echo = sql_config['debug']
meta_data = MetaData(db)


def get_meta_data():
    return meta_data
