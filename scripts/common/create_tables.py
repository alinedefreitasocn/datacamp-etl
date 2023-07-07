# import base and engine from base.py
from base import Base, engine
# Import the PprRawAll table from tables.py
from tables import PprRawAll

# Create the table in the database
if __name__ == "__main__":
    # Base.metadata.create_all() is the method
    # used to create all tables that don't
    # yet exist in the database.
    # engine needs to be passed as argument to
    # create_all() to establish connection.
    Base.metadata.create_all(engine)
