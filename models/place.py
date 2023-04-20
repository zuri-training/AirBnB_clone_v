#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models import storage
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Float, ForeignKey, Integer, String


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="all, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """FileStorage getter attribute"""
            revlist = []
            for review in list(storage.all(Review).values()):
                if review.place_id == self.id:
                    revlist.append(review)
            return revlist
