from typing import Optional,List
from dataclasses import dataclass
from . base import BaseEntity
from domain.value_objects.address import Address
from domain.value_objects.phone import Phone
from enum import Enum
from domain.exceptions.user_exceptions import InvalidProfileError


class Role(Enum):
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'


@dataclass(kw_only=True)
class User(BaseEntity):
    _name : str
    _email : str
    _password : str
    _phone : Phone
    _role : Role = Role.CUSTOMER

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email
    
    @property
    def phone(self) -> Phone:
        return self._phone

    @property
    def role(self) -> Role:
        return self._role

    @name.setter
    def name(self, name: str):
        if not name:
            raise InvalidProfileError("Name is Required")
        if len(name) < 3:
            raise InvalidProfileError('Invalid Name')
        self._name = name

    @email.setter
    def email(self, email: str):
        self._email = email

    @phone.setter
    def phone(self, phone: Phone):
        self._phone = phone

    @role.setter
    def role(self, role: Role):
        self._role = role

@dataclass(kw_only=True)
class ShippingAddress(BaseEntity):
    user_id : User
    address : Address
    label : Optional[str] = None
    is_default : bool = False
    


