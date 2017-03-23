#!/usr/bin/python3
"""
Amenity Class:
    Inherits from BaseModel and Base, defines two new class attributes
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Represents Amenities available to users
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    """
    Initializes the class with args and kwargs
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

