from typing import Optional,List
from domain.entities.orders import Order
from abc import ABC, abstractmethod



class OrderRepository(ABC):

    @abstractmethod
    async def get_by_id(self, order_id : int)  -> Optional[Order]:
        pass

    @abstractmethod
    async def save(self, order : Order) -> Order: 
        pass

    @abstractmethod
    async def delete(self, order : Order) -> None:
        pass

    @abstractmethod
    async def list_by_user(self, user_id : int) -> List[Order]:   
        pass
    
    @abstractmethod
    async def list_all(self) -> List[Order]:   
        pass

    @abstractmethod
    async def search_by_status(self, status : str) -> List[Order]:   
        pass

    @abstractmethod
    async def list_by_date_range(self, start_date : str, end_date : str) -> List[Order]:   
        pass

    @abstractmethod
    async def list_by_product(self, product_id : int) -> List[Order]:   
        pass

    @abstractmethod
    async def update(self, order : Order) -> Order:  
        pass