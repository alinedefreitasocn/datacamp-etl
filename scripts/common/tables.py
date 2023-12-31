# Import the objects needed
from sqlalchemy.orm import declarative_base, column_property
from sqlalchemy import Column, Integer, String, Date, cast

from base import Base

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
    # Create a unique transaction id
    transaction_id = column_property(
        date_of_sale + "_" + address + "_" + county + "_" + price
    )

class PprCleanAll(Base):
    __tablename__ = "ppr_clean_all"

    id = Column(Integer, primary_key=True)
    # Create a new column of type Date
    date_of_sale = Column(Date)
    address = Column(String(255))
    postal_code = Column(String(55))
    county = Column(String(55))
    price = Column(Integer)
    description = Column(String(255))
    # Create a unique transaction id
    # all non-string columns are casted as string
    transaction_id = column_property(
        cast(date_of_sale, String) + "_" + address + "_" + county + "_" + cast(price, String)
    )
