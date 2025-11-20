from typing import Optional,List
from domain.entities.users import User,ShippingAddress
from abc import ABC, abstractmethod 



class UserRepository(ABC):


    @abstractmethod
    async def get_by_id(self, user_id : int)  -> Optional[User]:
        pass

    @abstractmethod
    async def get_by_email(self, email : str)  -> Optional[User]:
        pass

    @abstractmethod
    async def save(self, user : User) -> User:
        pass

    @abstractmethod
    async def delete(self, user : User) -> None:
        pass

    @abstractmethod
    async def list_all(self) -> List[User]:   
        pass


    @abstractmethod
    async def update(self, user : User) -> User:  
        pass



class AddressRepository(ABC):


    @abstractmethod
    async def get_by_id(self, address_id : int)  -> Optional[ShippingAddress]:
        pass

    @abstractmethod
    async def save(self, address : ShippingAddress) -> ShippingAddress:
        pass

    @abstractmethod
    async def delete(self, address : ShippingAddress) -> None:
        pass

    @abstractmethod
    async def list_by_user(self, user : User) -> List[ShippingAddress]:   
        pass


    @abstractmethod
    async def update(self, address : ShippingAddress) -> ShippingAddress:  
        pass
