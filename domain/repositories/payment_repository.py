from typing import Optional,List
from domain.entities.payments import Payment
from abc import ABC, abstractmethod 


class PaymentRepository(ABC):
     
    @abstractmethod
    async def get_by_id(self, payment_id : int)  -> Optional[Payment]:
        pass    

    
    @abstractmethod
    async def save(self, payment : Payment) -> Payment: 
        pass    

    @abstractmethod
    async def update(self, payment : Payment) -> Payment:  
        pass

    @abstractmethod
    async def delete(self, payment : Payment) -> None:
        pass


    @abstractmethod
    async def list_all(self) -> List[Payment]:   
        pass


    @abstractmethod
    async def search(self, term : str) -> Optional[Payment]:
        pass

    @abstractmethod
    async def list_by_user(self, user_id : int) -> List[Payment]:   
        pass