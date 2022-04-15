from sqlalchemy import create_engine, inspect
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.sql import text


def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url)
    return engine


def insert_values(engine, insert_statement, data):
    with engine.connect() as conn:
        statement = text(insert_statement)

        for line in data:
            conn.execute(statement, **line)


def check_table_columns(engine, table):
    inspector = inspect(engine)
    return inspector.get_columns(table)