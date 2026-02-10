"""
models.py

This file defines the data structure or schema for the application.
We use pydantic's BaseModel to validate the type of data. 
Validate here means that the data is correct and follows our rules and regulations

"""


from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

"""
Product Model

The above class represents the structure of the product object.
It ensures that all the data follows the correct format and data tupes when creating or updating products

"""