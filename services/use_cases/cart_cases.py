from typing import List, Optional
from domain.entities.products import Product    
from domain.entities.orders import Order, Status
from domain.entities.users import User
from domain.exceptions.product_exceptions import InvalidQuantityException
from domain.exceptions.cart_exceprtions import CartException

from domain.entities.cart import Cart
from domain.repositories.cart_repository import CartRepository



class CartService:
    def __init__(self, cart_repo : CartRepository):
        self.cart_repository = cart_repo

    # --------------- Cart Level Operations ------------

    async def get_cart_by_user(self, user_id : int) -> Optional[Cart]:
        cart = await self.cart_repository.get_by_user(user_id)
        if cart is None:
            cart = await self.cart_repository.create_cart(user_id)
        return cart
        
    async def clear_cart(self, user_id: int) -> None: 
        await self.cart_repository.clear_items(user_id) 
    
    async def delete_cart(self, user_id: int) -> None: 
        await self.cart_repository.delete_cart(user_id)
        

    
    # ------------------Cart Item Level Operation---------------------


    async def add_cart(self, user_id : int, product : Product, qty : int = 1) -> Cart:
        cart = await self.get_cart_by_user(user_id)
        cart.add_item(product=product,qty=qty)
        await self.cart_repository.save(cart)
        return cart
    

    async def remove_cart(self, user_id : int, product : Product, qty : int = 1) -> None:
        cart = await self.get_cart_by_user(user_id)
        cart.remove_item(product.id)
        await self.cart_repository.save(cart)

    async def update_cart_item(self, user_id : int, product : Product, qty : int) -> Cart:
        if qty < 1:
            raise InvalidQuantityException("Quantity must be at least one.")
        
        cart = await self.get_cart_by_user(user_id)
        if product.id in cart.items:
            cart.items[product.id].quantity = qty
            await self.cart_repository.save(cart)
            return cart
        else:
            raise CartException("Item not found in cart.")

    async def get_total_amount(self, user_id: int) -> float: 
        cart = await self.get_cart_by_user(user_id) 
        return cart.total_amount
