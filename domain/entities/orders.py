from dataclasses import dataclass
from enum import Enum
from domain.exceptions.order_exceptions import InvalidOrderException,InvalidStatusTransitionException 
from domain.exceptions.product_exceptions import OutofStockException 
from domain.exceptions.user_exceptions import InvalidAddressError
from .base import BaseEntity
from .users import User,ShippingAddress
from .payments import Payment
from .products import Product


class Status(Enum):
    ORDERED = 'ORDERED'
    CONFIRMED = 'CONFIRMED'
    PACKED = 'PACKED'
    SHIPPED ='SHIPPED'
    DELIVERD ='DELIVERED'
    RETURNED = 'RETURNED'
    REJECTED = 'REJECTED'


@dataclass(kw_only=True)
class Order(BaseEntity):
    _user : User
    _product : Product
    _address : ShippingAddress
    _quantity : int = 1
    _status :Status = Status.ORDERED
    payment : Payment
    
    def __post_init__(self):
        if not self._product.is_available():
            raise OutofStockException("Product Not Available")
        
        if self._quantity <= 0:
            raise InvalidOrderException("Quantity must be greater than zero.")
        
        if self._quantity > self._product.quantity :
            raise OutofStockException('Not Available quanties as you entered')
        
        if not self._address:
            raise InvalidAddressError('Address is Required')
        
        
        
    @property
    def quantity(self) -> int:
        return self._quantity
    
    @property
    def price(self) -> float:
        return self._product.price * self._quantity
    
    
    def update_status(self, new_status: Status) -> None:
        valid_transitions = {
            Status.ORDERED: [Status.CONFIRMED, Status.REJECTED],
            Status.CONFIRMED: [Status.PACKED],
            Status.PACKED: [Status.SHIPPED],
            Status.SHIPPED: [Status.DELIVERD, Status.RETURNED],
        }
  
        if new_status not in valid_transitions.get(self._status, []):
            raise InvalidStatusTransitionException(f"Invalid status transition from {self._status} to {new_status}.")

        self._status = new_status

        
    
        
    


