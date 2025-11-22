from typing import List, Optional,Dict
from domain.entities.base import BaseEntity
from domain.entities.products import Product
from domain.entities.users import User
from domain.exceptions.product_exceptions import InvalidQuantityException
from domain.exceptions.cart_exceprtions import CartException
from dataclasses import dataclass

@dataclass
class CartItem:
    product_id : str
    quantity : int
    unit_price : float

    def __post_init__(self):
        if self.quantity < 1:
            raise InvalidQuantityException('Quantity must atleast one')

    @property
    def total_price(self) -> float:
        return self.unit_price * self.quantity
    

@dataclass(kw_only=True)
class Cart(BaseEntity):
    user : User
    items : Dict[str, CartItem]

    def add_item(self, product : Product, qty : int) -> None:
        if product.id in self.items:
            self.items[product.id].quantity += qty
        
        else:
            self.items[product.id]  = CartItem(
                product_id = product.id,
                quantity = qty,
                unit_price = product.price
            )
            
    def remove_item(self, product_id : str) -> None:
        if product_id in self.items:
            del self.items[product_id]
        else:
            raise CartException("Item not found in cart")

    
    def clear_cart(self) -> None:
        self.items.clear()

    
    @property
    def total_amount(self) -> float:
        return sum(item.total_price for item in self.items.values())