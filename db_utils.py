# This script provides functionality to completely reset a database schema. 
# It's been developed for use in development environments where changes to the database schema 
# are frequent and require a clean slate for testing or development purposes.

from models.credentials import get_engine  # Importing the function to get the database engine
from models.entities import *  # Importing all entities defined in the daos.entities module
from sqlalchemy_utils import database_exists, create_database, drop_database  # Importing utility functions for database operations

def drop_n_create_db():
    """
    This function drops the existing database (if it exists) and creates a new database schema.
    It's useful for resetting the database state to a clean slate, especially during development
    and testing phases where schema changes are frequent.
    """
    engine = get_engine()  # Acquiring the database engine from the credentials module

    if database_exists(engine.url):  # Checking if the database already exists
        drop_database(engine.url)  # Dropping the existing database if it exists

    create_database(engine.url)  # Creating a new database
    Base.metadata.create_all(engine)  # Using SQLAlchemy's Base to create all defined tables and relationships in the new database

drop_n_create_db()