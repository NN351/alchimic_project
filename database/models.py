from db import BASE

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
    Date,
)

class StudentGroup(BASE):
    __tablename__ = 'student_group'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True
    )
    name = Column(String(100), nullable=False)

class Student(BASE):
    __tablename__ = 'student'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True
    )
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(60), nullable=False)
    email = Column(String(100), nullable=True)
    birthday = Column(Date, nullable=True)
    group = Column(Integer, ForeignKey('student_group.id'), nullable=False)


