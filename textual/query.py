from dotenv import load_dotenv, dotenv_values
from utils import get_engine


## Two ways load the environment variables in the root folder
# load_dotenv
config = dotenv_values(".env")

user = config["DB_USER"]
passwd = config["DB_PASS"]
host = config["DB_HOST"]
port = config["DB_PORT"]


engine = get_engine(user, passwd, host, port, "bookstore")

with engine.connect() as conn:

    query = """
    SELECT b.id, b.title, a.name, a.fullname
    FROM book b
    JOIN author a
    ON b.author_id = a.id
    """

    rs = conn.execute(query)

    for row in rs:
        print(row)

with engine.connect() as conn:

    query = """
    SELECT a.fullname, COUNT(b.title)
    FROM author a
    JOIN book b
    ON a.id = b.author_id
    GROUP BY a.fullname
    """

    rs = conn.execute(query)

    for row in rs:
        print(row)
