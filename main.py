"""
main.py

This is the entry point of the FastAPI application.
It handles:
- App creation
- Database initialization
- Sample data insertion
- API endpoints (CRUD operations)


"""

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session

# Create FASTAPI instance
app = FastAPI()

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods = ["*"]
)

# Create tables in the database if they don't exist
database_models.Base.metadata.create_all(bind=engine)

#First code of FASTAPI

@app.get("/")   
def greet():
    return "Hi"

# Sample data

products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),    
]

def get_db():
    db = session() # Creating the connection to db
    try:
        yield db # Using the connection
    finally:
        db.close() # Closing the connection


# DATABASE INITIALIZATION

def init_db():
    """
    Inserts sample data into the database if table is empty.

    """
    db = session()

    # Count rows in product table
    count = db.query(database_models.Product).count()

    if count == 0:
        for product in products:
            # Convert Pydantic model → dict → SQLAlchemy model
            db.add(database_models.Product(**product.model_dump())) # Passes the product list defined above to the models so that it is mapped with the database
            db.commit()

init_db()


# Making endpoints

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)): # Inject the connection also called Dependancy injection

    db_product = db.query(database_models.Product).all()

    return db_product

@app.get("/products/{id}") # makes the url dynamic so we can access all the product in the products field
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return "product not found" 


# To add product

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)): # We will get the data in the type of Product that is a class in models.py
    db.add(database_models.Product(**product.model_dump()))  
    db.commit()  
    return product 

# To update the product
@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "product updated"
    else:
        return "product not found"

#To delete a product
@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return "product not found"