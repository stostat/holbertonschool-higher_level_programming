#!/usr/bin/python3
"""Introduction to sqlalchemy"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class that creates the tabble states"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(140), nullable=False)
