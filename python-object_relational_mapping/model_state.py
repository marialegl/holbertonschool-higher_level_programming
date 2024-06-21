#!/usr/bin/python3
"""
model_state module
Contains the definition of a class State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    class State that represents the state table
    """
    __tablename__ = 'states'
    ide = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
