from typing import List
from db.models import Hotel, HotelChain
from schemas import (
    HotelChainUpdate,
    HotelCreate,
    HotelChainCreate,
    HotelUpdate,
    HotelChainSchema,
)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_chain

router = APIRouter(prefix="/hotel_chain", tags=["hotel_chain"])


@router.post("/", response_model=HotelChainSchema)
def create_hotel_chain(request: HotelChainCreate, db: Session = Depends(get_db)):
    return db_chain.create_chain(db, request)


@router.get("/", response_model=List[HotelChainSchema])
def read_hotel_chains(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db_chain.get_chains(db, skip, limit)


@router.get("/{hotel_chain_id}", response_model=HotelChainSchema)
def read_hotel_chain(hotel_chain_id: int, db: Session = Depends(get_db)):
    return db_chain.get_chain(db, hotel_chain_id)


@router.put("/{id}", response_model=HotelChainSchema)
def update_chain(id: int, request: HotelChainUpdate, db: Session = Depends(get_db)):
    return db_chain.update_chain(db, id, request)


@router.delete("/{id}")
def delete_chain(id: int, db: Session = Depends(get_db)):
    return db_chain.delete_chain(db, id)
