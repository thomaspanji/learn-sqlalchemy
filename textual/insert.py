from dotenv import load_dotenv, dotenv_values
from utils import get_engine, insert_values
from sqlalchemy.sql import text

## Two ways load the environment variables in the root folder
# load_dotenv
config = dotenv_values(".env")

user = config["DB_USER"]
passwd = config["DB_PASS"]
host = config["DB_HOST"]
port = config["DB_PORT"]


engine = get_engine(user, passwd, host, port, "bookstore")

with engine.connect() as conn:

    authors = (
        {"id":1, "name":"Paryono", "fullname":"Stephen Paryono"},
        {"id":2, "name":"Daniel", "fullname":"Iphan Daniel"},
        {"id":3, "name":"Murphy", "fullname":"Eric Murphy"},
        {"id":4, "name":"Cheetos", "fullname":"Cheetah Cheetos"}
    )

    books = ( 
        { "id": 1, "title": "The Start", "author_id": 1 },
        { "id": 2, "title": "The End", "author_id": 1 },
        { "id": 3, "title": "The Content", "author_id": 2 },
    )

    insert_author = """
    INSERT INTO author(id, name, fullname) VALUES (:id, :name, :fullname)
    """

    insert_book = """
    INSERT INTO book(id, title, author_id) VALUES (:id, :title, :author_id)
    """

    statement = text(insert_author)

    for line in authors:
        conn.execute(statement, **line)

    statement = text(insert_book)

    for line in books:
        conn.execute(statement, **line)


# OR
# Using user-defined function from utils
# Example for authors
authors = (
    {"id":1, "name":"Paryono", "fullname":"Stephen Paryono"},
    {"id":2, "name":"Daniel", "fullname":"Iphan Daniel"},
    {"id":3, "name":"Murphy", "fullname":"Eric Murphy"},
    {"id":4, "name":"Cheetos", "fullname":"Cheetah Cheetos"}
)

insert_author = """
INSERT INTO author(id, name, fullname) VALUES (:id, :name, :fullname)
"""

insert_values(engine, insert_author, authors)