from typing import Optional,TYPE_CHECKING
from enum import Enum   
from uuid import UUID
from sqlmodel import Field,Relationship
from .base_model import BaseModel



if TYPE_CHECKING:
    from database.models.orders_model import OrderModel



class PaymentMethod(str, Enum):
    CREDIT_CARD = 'CREDIT_CARD'
    DEBIT_CARD = 'DEBIT_CARD'
    PAYPAL = 'PAYPAL'
    BANK_TRANSFER = 'BANK_TRANSFER'
    CASH_ON_DELIVERY = 'CASH_ON_DELIVERY'


class PaymentStatus(str,Enum):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    REFUNDED = 'REFUNDED'


class PaymentModel(BaseModel, table=True):
    __tablename__ = "payments"

    order_id: UUID = Field(default=None, foreign_key="orders.id", index=True)
    amount: float = Field(index=True)
    method: PaymentMethod = Field(sa_column_kwargs={"type_": "VARCHAR(50)"})
    status: PaymentStatus = Field(default=PaymentStatus.PENDING, sa_column_kwargs={"type_": "VARCHAR(50)"})


    order : "OrderModel" = Relationship(back_populates="payment")