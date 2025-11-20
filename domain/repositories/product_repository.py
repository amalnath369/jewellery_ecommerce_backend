from typing import Optional,List
from domain.entities.products import Product
from abc import ABC, abstractmethod 




class ProductRepository(ABC):
    
    @abstractmethod
    async def get_by_id(self, product_id : int)  -> Optional[Product]:
        pass

    @abstractmethod
    async def list_all(self) -> List[Product]:   
        pass

    @abstractmethod
    async def search(self, term : str) -> Product:
        pass

    @abstractmethod
    async def list_by_category(self, category : str) -> List[Product]:   
        pass

    @abstractmethod
    async def save(self, product : Product) -> Product:
        pass

    @abstractmethod
    async def delete(self, product : Product) -> None:
        pass

    @abstractmethod
    async def update(self, product : Product) -> Product:  
        pass