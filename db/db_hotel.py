from exceptions import StoryException
from sqlalchemy.orm.session import Session
from db.models import Hotel
from schemas import *
from fastapi import HTTPException, status


def create_hotel(db: Session, request: HotelCreate):
    new_hotel = Hotel(**request.model_dump())
    db.add(new_hotel)
    db.commit()
    db.refresh(new_hotel)
    return new_hotel


def update_hotel(db: Session, id: int, request: HotelUpdate):
    hotel = db.query(Hotel).filter(Hotel.id == id).first()
    if not hotel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hotel with id {id} not found",
        )
    for field, value in request.model_dump(exclude_unset=True).items():
        setattr(hotel, field, value)

    db.commit()
    db.refresh(hotel)
    return hotel


def get_hotel(db: Session, id: int):
    hotel = db.query(Hotel).filter(Hotel.id == id).first()
    if not hotel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"hotel with id {id} not found",
        )
    return hotel


def get_hotels(db: Session, skip: int, limit: int):
    hotels = db.query(Hotel).offset(skip).limit(limit).all()
    return hotels


def delete_hotel(db: Session, id: int):
    hotel = db.query(Hotel).filter(Hotel.id == id).first()
    if not hotel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hotel with id {id} not found",
        )
    db.delete(hotel)
    db.commit()
    return "ok"

