import re
from dataclasses import dataclass
from domain.exceptions.user_exceptions import InvalidAddressError



@dataclass
class Address:
    street: str
    city: str
    state: str
    postal_code: int
    country: str = 'INDIA'    
    address_line_2: str = ""
    landmark: str = ""
    latitude: float = None
    longitude: float = None

    def __post_init__(self):
        if not self._validate_basic_fields():
            raise InvalidAddressError("Street, city,Pin code  and country are required.")
        if not self._is_valid_indian_pin(self.postal_code):
            raise InvalidAddressError(f"Invalid Indian PIN code: {self.postal_code}")
        
    def _validate_basic_fields(self) -> bool:
        return all([self.street, self.city, self.country,self.state,self.postal_code])

    def _is_valid_indian_pin(pin_code: str) -> bool:
        pattern = r'^[1-9][0-9]{5}$'
        return bool(re.match(pattern, pin_code))
    
    def __str__(self):
        parts = [self.street, self.address_line_2, self.city, self.state, self.postal_code, self.country]
        return ", ".join(filter(None, parts))
    
    