from typing import Optional, List
from abc import ABC, abstractmethod
from domain.entities.cart import Cart, CartItem


class CartRepository(ABC):

    # ---- Cart-level operations ----
    
    @abstractmethod
    async def get_by_user(self, user_id: int) -> Optional[Cart]:
        pass

    @abstractmethod
    async def create_cart(self, user_id: int) -> Cart:
        pass

    @abstractmethod
    async def delete_cart(self, user_id: int) -> None:
        pass

    @abstractmethod
    async def list_all(self) -> List[Cart]:
        pass

    @abstractmethod
    async def save(self, cart : Cart) -> Cart:
        pass
    # ---- Item-level operations ----
    
    @abstractmethod
    async def add_item(self, user_id: int, item: CartItem) -> CartItem:
        pass

    @abstractmethod
    async def remove_item(self, user_id: int, product_id: str) -> None:
        pass

    @abstractmethod
    async def update_item(self, user_id: int, item: CartItem) -> CartItem:
        pass

    @abstractmethod
    async def clear_items(self, user_id: int) -> None:
        pass
