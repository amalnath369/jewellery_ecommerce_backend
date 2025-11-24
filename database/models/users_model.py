from .base_model import BaseModel
from sqlmodel import Field,Relationship
from typing import List,TYPE_CHECKING,Optional
from enum import Enum
from uuid import UUID

if TYPE_CHECKING:
    from database.models.product_models import ProductReviewModel
    from database.models.orders_model import OrderModel
    from database.models.cart_model import CartModel

class RoleEnum(str, Enum):
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'


class UserModel(BaseModel, table=True):
    __tablename__ = "users"

    name: str = Field(index=True)
    email: str = Field(index=True, unique=True)
    password: str = Field(max_length=128)
    phone: str = Field(index=True)
    role: RoleEnum = Field(default=RoleEnum.CUSTOMER)

    addresses : List["ShippingAddressModel"] = Relationship(back_populates="user")
    reviews : List["ProductReviewModel"] = Relationship(back_populates="user")
    orders : Optional[List["OrderModel"]] = Relationship(back_populates="user")
    carts : Optional[List["CartModel"]] = Relationship(back_populates="user")

class ShippingAddressModel(BaseModel, table=True):
    __tablename__ = "shipping_addresses"

    user_id: UUID = Field(default=None, foreign_key="users.id")
    street: str = Field(length=1024)
    city: str = Field(length=256, index=True)
    state: str = Field(length=256, index=True)
    zip_code: str = Field(length=20, index=True)
    country: str = Field(length=256)

    user : UserModel = Relationship(back_populates="addresses")
    orders : Optional[List["OrderModel"]] = Relationship(back_populates="address")