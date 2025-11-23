from .base_model import BaseModel
from sqlmodel import Field
from typing import Optional
from enum import Enum


class RoleEnum(Enum):
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'


class UserModel(BaseModel, table=True):
    __tablename__ = "users"

    name: str = Field(index=True)
    email: str = Field(index=True, unique=True)
    password: str = Field(hash_length=128)
    phone: str = Field(index=True)
    role: RoleEnum = Field(default=RoleEnum.CUSTOMER)


class ShippingAddressModel(BaseModel, table=True):
    __tablename__ = "shipping_addresses"

    user_id: Optional[str] = Field(default=None, foreign_key="users.id")
    street: str = Field(length=1024)
    city: str = Field(length=256, index=True)
    state: str = Field(length=256, index=True)
    zip_code: str = Field(length=20, index=True)
    country: str = Field(length=256)