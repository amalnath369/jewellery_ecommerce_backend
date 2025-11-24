from sqlmodel import Field,Relationship
from .base_model import BaseModel
from typing import Optional,List,TYPE_CHECKING
from uuid import UUID
from enum import Enum

if TYPE_CHECKING:
    from database.models.users_model import UserModel,ShippingAddressModel
    from database.models.product_models import ProductModel
    from database.models.payment_models import PaymentModel


class Status(str, Enum):
    ORDERED = 'ORDERED'
    CONFIRMED = 'CONFIRMED'
    PACKED = 'PACKED'
    SHIPPED ='SHIPPED'
    DELIVERD ='DELIVERED'
    RETURNED = 'RETURNED'
    REJECTED = 'REJECTED'


class OrderModel(BaseModel, table=True):
    __tablename__ = 'orders'

    user_id: UUID  = Field(default=None, foreign_key="users.id")
    product_id: UUID  = Field(default=None, foreign_key="products.id")
    address_id: UUID  = Field(default=None, foreign_key="shipping_addresses.id")
    status: Status = Field(default=Status.ORDERED, index=True)
    quantity: int = Field(default=1, index=True)


    user : "UserModel" = Relationship(back_populates="orders")
    product : "ProductModel" = Relationship(back_populates="orders")
    address : "ShippingAddressModel" = Relationship(back_populates="orders")

    payment : Optional["PaymentModel"] = Relationship(back_populates="order")
