CREATE DATABASE bookstore;


CREATE TABLE IF NOT EXISTS author (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    fullname VARCHAR NOT NULL
)

CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY,
    title STRING,
    author_id INTEGER,
    FOREIGN KEY(author_id) REFERENCES author(id)
)