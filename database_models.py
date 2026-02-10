"""
models.py (SQLAlchemy ORM Model)

This file defines the database table structure using SQLALchemy ORM.
Each class represents a table, and each attribute represents a column

"""

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() # Creates a base class that all database models must inherit from. 

class Product(Base):
    """
    Product Table Model

    This class maps to a table named 'product' in the database.
    SQLAlchemy will automatically create this table based on the column definitions if migrations / create_all is run.


    """
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
