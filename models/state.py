#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
import models
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable = False)
    cities = relationship("City", cascade = "all, delete-orphan",
            backref = "state")

    @property
    def cities(self):
        """"returns the list of City instances """

        cities = models.storage.all(City)
        city_instances = []
        for city in cities.values():
            if city.state_id == self.id:
                city_instances.append(city)
        return city_instances
