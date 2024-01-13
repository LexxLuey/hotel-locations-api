from typing import List
from db.models import Hotel, HotelChain
from schemas import *
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_hotel

router = APIRouter(prefix="/hotel", tags=["hotel"])


@router.post("/", response_model=HotelSchema)
def create_hotel(request: HotelCreate, db: Session = Depends(get_db)):
    return db_hotel.create_hotel(db, request)


@router.get("/", response_model=List[HotelSchema])
def read_hotels(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db_hotel.get_hotels(db, skip, limit)


@router.put("/{id}", response_model=HotelSchema)
def update_hotel(id: int, request: HotelUpdate, db: Session = Depends(get_db)):
    return db_hotel.update_hotel(db, id, request)


@router.get("/{hotel_id}", response_model=HotelSchema)
def read_hotel(hotel_id: int, db: Session = Depends(get_db)):
    return db_hotel.get_hotel(db, hotel_id)


@router.delete("/{id}")
def delete_hotel(id: int, db: Session = Depends(get_db)):
    return db_hotel.delete_hotel(db, id)
