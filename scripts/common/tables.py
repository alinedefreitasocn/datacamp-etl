# Import the objects needed
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Initialize the base and set inheritance
Base = declarative_base()

# map a Python class to a PostgreSQL table,
# declaring a table name and a primary key.
class PprRawAll(Base):
    # Set the table name
    __tablename__ = "ppr_raw_all"
    # Create a primary key integer column id
    id = Column(Integer, primary_key=True)
    # declare the rest of the columns,
    # according to this table definition
    date_of_sale = Column(String(55))
    address = Column(String(255))
    postal_code = Column(String(55))
    county = Column(String(55))
    price = Column(String(55))
    description = Column(String(55))
