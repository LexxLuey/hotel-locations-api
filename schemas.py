from typing import List, Optional
from pydantic import BaseModel


class HotelChainBase(BaseModel):
    name: str


class HotelChainUpdate(BaseModel):
    name: Optional[str] = None


class HotelChainCreate(HotelChainBase):
    pass


class HotelBase(BaseModel):
    name: str
    city: str
    country: str
    address: str


class HotelUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    address: Optional[str] = None
    lat: Optional[float] = None  # Latitude
    lng: Optional[float] = None  # Longitude    
    chain_id: Optional[int] = None


class HotelCreate(HotelBase):
    chain_id: Optional[int] = None
    lat: Optional[float] = None  # Latitude
    lng: Optional[float] = None  # Longitude

class HotelSchema(HotelBase):
    id: int
    lat: Optional[float] = None  # Latitude
    lng: Optional[float] = None  # Longitude
    chain_id: Optional[int] = None
    chain: Optional[HotelChainBase] = None
    class Config:
        from_attributes = True


class HotelChainSchema(HotelChainBase):
    id: int
    hotels: List[HotelSchema] = []

    class Config:
        from_attributes = True


# Article inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []

    class Config:
        from_attributes = True


# User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config:
        from_attributes = True
