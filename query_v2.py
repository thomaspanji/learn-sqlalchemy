from dotenv import load_dotenv, dotenv_values
from utils import get_engine
from sqlalchemy.sql import select
from model import authors, books

## Two ways load the environment variables in the root folder
# load_dotenv
config = dotenv_values(".env")

user = config["DB_USER"]
passwd = config["DB_PASS"]
host = config["DB_HOST"]
port = config["DB_PORT"]


engine = get_engine(user, passwd, host, port, "bookstore")

# Query using sqlalchemy select
with engine.connect() as conn:
    
    s = select(authors)
    rs = conn.execute(s)

    # Print as tuple
    for row in rs:
        print(row)

    # or
    for row in rs:
#         print("name: ", row.name, "; fullname: ", row.fullname)

# Selecting specific columns
with engine.connect() as conn:
    
    s = select(authors.c.name, authors.c.fullname)
    rs = conn.execute(s)

    # Print as tuple
    for row in rs:
        print(row)

    # Output
    # ('Paryono', 'Stephen Paryono')
    # ('Daniel', 'Iphan Daniel')
    # ('Murphy', 'Eric Murphy')
    # ('Cheetos', 'Cheetah Cheetos')

# Select with where clause
# Joining two tables
with engine.connect() as conn:
    
    s = select(books, authors).where(books.c.author_id == authors.c.id)

    for row in conn.execute(s):
        print(row)
    
    # Output
    # (1, 'The Start', 1, 1, 'Paryono', 'Stephen Paryono')
    # (2, 'The End', 1, 1, 'Paryono', 'Stephen Paryono')
    # (3, 'The Content', 2, 2, 'Daniel', 'Iphan Daniel')

# Select specific columns from two tables
with engine.connect() as conn:
    
    s = select(books.c.title, authors.c.name, authors.c.fullname).where(books.c.author_id == authors.c.id)

    for row in conn.execute(s):
        print(row)
    
    # Output
    # ('The Start', 'Paryono', 'Stephen Paryono')
    # ('The End', 'Paryono', 'Stephen Paryono')
    # ('The Content', 'Daniel', 'Iphan Daniel')