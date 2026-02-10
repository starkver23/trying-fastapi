"""
database.py

This file is responsible for setting up the database connection using SQLALchemy.
It creates the engine and session that will be used throughout the application to interact with PostgreSQL

Engine here helps to communicate with the database
Session is the workplace to add, remove, update, query and commit the changes in the data


"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""

Database URL
Format: "postgresql+driver://username:password@host/database_name"
In this case:
    - DBMS: PostgreSQL
    - Driver: psycopg
    - Username: aryanverma
    - Host: localhost
    - Database Name: telusko

Psycopg converts python commands to SQL queries


"""

db_url = "postgresql+psycopg://aryanverma@localhost/telusko" # has admin name and password for database since we are using postgresql we write postgres and it's password

engine = create_engine(db_url) #pass the dbms which we are working with 
session = sessionmaker(autocommit=False, autoflush=False, bind=engine) # engine helps to connect to the database

"""

autocommit means the changes made in the database. Since, it is false we need to call commit() whenever adding data to the database
autoflush prevents automatic sync to the DB while we are still editing
bind is used to connect sessions to the database gateway

"""


