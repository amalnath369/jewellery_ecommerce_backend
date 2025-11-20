from dataclasses import dataclass
from domain.entities.base import BaseEntity
from domain.exceptions.payment_exceptions import InvalidPaymentException
from enum import Enum
from domain.entities.orders import Order


class PaymentMethod(Enum):
    CREDIT_CARD = 'CREDIT_CARD'
    DEBIT_CARD = 'DEBIT_CARD'
    PAYPAL = 'PAYPAL'
    BANK_TRANSFER = 'BANK_TRANSFER'
    CASH_ON_DELIVERY = 'CASH_ON_DELIVERY'


class PaymentStatus(Enum):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    REFUNDED = 'REFUNDED'

@dataclass(kw_only=True)
class Payment(BaseEntity):
    order : 'Order'
    amount: float
    method: PaymentMethod
    status: PaymentStatus = PaymentStatus.PENDING

    def __post_init__(self):
        if self.amount < 0:
            raise InvalidPaymentException("Payment amount must be greater than zero.")
        
    def mark_payment(self, status : PaymentStatus) -> None:
        allowed_transitions = {
        PaymentStatus.PENDING: {PaymentStatus.COMPLETED, PaymentStatus.FAILED},
        PaymentStatus.COMPLETED: {PaymentStatus.REFUNDED},
        PaymentStatus.FAILED: set(),
        PaymentStatus.REFUNDED: set(),
    }

        if status not in allowed_transitions[self.status]:
            raise InvalidPaymentException(
                f"Cannot change payment state from {self.status} to {status}"
            )

        self.status = status