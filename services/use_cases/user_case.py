from typing import Optional, List
from domain.entities.users import User, ShippingAddress,Role
from domain.repositories.user_repository import UserRepository, AddressRepository   
from domain.exceptions.user_exceptions import UserAlreadyExistsError,UserNotFoundError,AddressNotFound
from domain.value_objects.phone import Phone


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo


    async def create_user(self, name: str, email: str, password: str, phone_num: str, role: Role = Role.CUSTOMER) -> User: 

        existing_user = await self.user_repo.get_by_email(email)
        if existing_user:
            raise UserAlreadyExistsError(f"User with email {email} already exists.")

        phone = Phone(number= phone_num)  

        user = User(
            _name=name,
            _email=email,
            _password=password,
            _phone=phone,
            _role=role
        )     

        saved_user = await self.user_repo.save(user)
        return saved_user
    
    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(f'No user with  id - {user_id} exists')
        return user
    
    async def get_user_by_email(self, email : str) -> Optional[User]:
        user = await self.user_repo.get_by_email(email=email)
        if not user:
            raise UserNotFoundError(f'No user with  email- {email} exists')
        return user

    async def list_all_users(self) -> List[User]:
         return await self.user_repo.list_all()
    

    async def update_user(
        self,
        user_id: int,
        name: Optional[str] = None,
        email: Optional[str] = None,
        phone_num: Optional[str] = None,
        role: Optional[Role] = None
    ) -> User:

        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(f"User with id {user_id} not found")

        if name:
            user.name = name

        if email:
            user.email = email

        if phone_num:
            user.phone = Phone(number=phone_num)

        if role:
            user.role = role

        updated_user = await self.user_repo.update(user)
        return updated_user
        
    
    async def delete_user(self, user_id: int) -> None:
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(f"User with id {user_id} not found")
        await self.user_repo.delete(user)

        

class AddressService:
    def __init__(self, address_repo: AddressRepository):
        self.address_repo = address_repo

    
    async def add_address(self, user: User, address: ShippingAddress) -> ShippingAddress:

        address.user_id = user
        saved_address = await self.address_repo.save(address)
        return saved_address
    

    async def list_addresses_by_user(self, user: User) -> List[ShippingAddress]:
        return await self.address_repo.list_by_user(user)
    


    async def get_by_id(self, address_id : int) -> Optional[ShippingAddress]:
        address = await self.address_repo.get_by_id(address_id)
        if not address:
            raise AddressNotFound(f"Address with id {address_id} not found")
        return address
    

    async def update_address(self, address_id: int, new_address: ShippingAddress) -> ShippingAddress:   
        address = await self.address_repo.get_by_id(address_id)
        if not address:
            raise AddressNotFound(f"Address with id {address_id} not found")

        address.address = new_address.address
        address.label = new_address.label
        address.is_default = new_address.is_default

        updated_address = await self.address_repo.update(address)
        return updated_address
    

    async def delete(self, address_id: int) -> None:
        address = await self.address_repo.get_by_id(address_id)
        if not address:
            raise AddressNotFound(f"Address with id {address_id} not found")
        await self.address_repo.delete(address)