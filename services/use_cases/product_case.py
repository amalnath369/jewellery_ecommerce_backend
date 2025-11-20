from typing import List, Optional
from domain.entities.products import Product
from domain.repositories.product_repository import ProductRepository
from domain.exceptions.product_exceptions import OutofStockException




class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    
    async def add_product(self, product: Product) -> Product:
        return await self.product_repository.save(product)


    async def get_product(self, product_id: int) -> Optional[Product]:
        return await self.product_repository.get_by_id(product_id)


    async def update_product(self, product: Product) -> Product:
        return await self.product_repository.update(product)


    async def delete_product(self, product: Product) -> None:
        await self.product_repository.delete(product)


    async def list_all_products(self) -> List[Product]:
        return await self.product_repository.list_all()


    async def search_products(self, term: str) -> List[Product]:
        return await self.product_repository.search(term)


    async def reduce_stock(self, product_id: int, quantity: int) -> None:
        product = await self.get_product(product_id)
        if product is None:
            raise ValueError("Product not found")
        if product.quantity < quantity:
            raise OutofStockException("Not enough stock available")
        product.quantity -= quantity
        await self.update_product(product)