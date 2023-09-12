from db import BASE, engine
from database.models import Student, StudentGroup


def create_tables():
    print('Migration')
    BASE.metadata.create_all(engine, checkfirst=True)
