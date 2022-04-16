from utils import get_engine
from dotenv import load_dotenv, dotenv_values
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


## Two ways to load the environment variables in the root folder
# load_dotenv
config = dotenv_values(".env")

user = config["DB_USER"]
passwd = config["DB_PASS"]
host = config["DB_HOST"]
port = config["DB_PORT"]

metadata = MetaData()

authors = Table(
    'author', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String, nullable=False)
)

books = Table(
    'book', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('author_id', Integer, ForeignKey('author.id')),
)

# engine = create_engine('sqlite:///bookstore.db')
engine = get_engine(user, passwd, host, port, "bookstore")

# generate table in database
metadata.create_all(engine)

