from domain.exceptions.user_exceptions import InvalidPhoneError
from dataclasses import dataclass


@dataclass
class Phone:
    number: str

    def __post_init__(self):
        if not self._is_valid_phone(self.number):
            raise InvalidPhoneError(f"Invalid phone number: {self.number}")

    def _is_valid_phone(self, number: str) -> bool:
        # Simple validation: check if the number consists of digits and has a reasonable length
        return number.isdigit() and  len(number) == 10