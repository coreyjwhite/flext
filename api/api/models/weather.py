"""Weather database table mapper classes."""

from .base import BaseModel
from sqlalchemy import Column, DateTime, Float, Integer, String


class Forecast(BaseModel):
    """Hourly forecast data."""

    __tablename__ = "forecast"

    id = Column(Integer, primary_key=True)
    office = Column(String(3))
    lat = Column(Float)
    long = Column(Float)
    timestamp = Column(DateTime)
    start = Column(DateTime)
    end = Column(DateTime)
    temperature = Column(Integer)
    forecast = Column(String)
