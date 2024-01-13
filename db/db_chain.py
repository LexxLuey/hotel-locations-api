from sqlalchemy.orm.session import Session
from db.models import HotelChain
from schemas import *
from fastapi import HTTPException, status


def create_chain(db: Session, request: HotelChainCreate):
    new_hotel_chain = HotelChain(**request.model_dump())
    db.add(new_hotel_chain)
    db.commit()
    db.refresh(new_hotel_chain)
    return new_hotel_chain


def get_chains(db: Session, skip: int, limit: int):
    chains = db.query(HotelChain).offset(skip).limit(limit).all()
    return chains


def delete_chain(db: Session, id: int):
    chain = db.query(HotelChain).filter(HotelChain.id == id).first()
    if not chain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hotel Chain with id {id} not found",
        )
    db.delete(chain)
    db.commit()
    return "ok"


def get_chain(db: Session, id: int):
    db_hotel_chain = db.query(HotelChain).filter(HotelChain.id == id).first()
    if db_hotel_chain is None:
        raise HTTPException(status_code=404, detail="Hotel chain not found")
    return db_hotel_chain


def update_chain(db: Session, id: int, request: HotelChainUpdate):
    chain = db.query(HotelChain).filter(HotelChain.id == id).first()
    if not chain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hotel chain with id {id} not found",
        )
    for field, value in request.model_dump(exclude_unset=True).items():
        setattr(chain, field, value)

    db.commit()
    db.refresh(chain)
    return chain
