from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, Float
from db.database import Base
from sqlalchemy import Column


class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)


class HotelChain(Base):
    __tablename__ = "hotel_chains"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    hotels = relationship("Hotel", back_populates="chain")


class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String)
    country = Column(String)
    address = Column(String)
    lat = Column(Float, nullable=True)
    lng = Column(Float, nullable=True)
    chain_id = Column(Integer, ForeignKey("hotel_chains.id"), nullable=True)

    chain = relationship("HotelChain", back_populates="hotels")
