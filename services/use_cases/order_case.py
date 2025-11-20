from typing import List, Optional
from domain.entities.products import Product    
from domain.entities.orders import Order, Status
from domain.entities.users import User, ShippingAddress
from domain.repositories.order_repository import OrderRepository
from domain.exceptions.order_exceptions import OrderNotFoundException, InvalidOrderException


class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    async def create_order(self, user: User, product: Product, address: ShippingAddress, quantity: int) -> Order:
        order = Order(_user=user, _product=product, _address=address, _quantity=quantity)
        saved_order = await self.order_repository.save(order)
        return saved_order

    async def get_order(self, order_id: int) -> Order:
        order = await self.order_repository.get_by_id(order_id)
        if not order:
            raise OrderNotFoundException(f"Order with id {order_id} not found.")
        return order

    async def update_order_status(self, order_id: int, new_status: Status) -> Order:
        order = await self.get_order(order_id)
        order.update_status(new_status)
        updated_order = await self.order_repository.update(order)
        return updated_order

    async def delete_order(self, order_id: int) -> None:
        order = await self.get_order(order_id)
        await self.order_repository.delete(order)

    async def list_orders_by_user(self, user_id: int) -> List[Order]:
        orders = await self.order_repository.list_by_user(user_id)
        return orders
    
    async def list_all_orders(self) -> List[Order]:
        orders = await self.order_repository.list_all()
        return orders
    
    async def search_order_by_status(self,status: str) -> List[Order]:
        orders = await self.order_repository.search_by_status(status)
        return orders
    
    async def list_orders_by_date_range(self, start_date: str, end_date: str) -> List[Order]:
        orders = await self.order_repository.list_by_date_range(start_date, end_date)
        return orders

    async def list_orders_by_product(self, product_id: int) -> List[Order]:
        orders = await self.order_repository.list_by_product(product_id)
        return orders
    