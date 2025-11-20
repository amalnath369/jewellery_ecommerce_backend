
class InvalidAddressError(Exception):
    """Raised when an address is invalid."""
    pass

class InvalidPhoneError(Exception):
    """Raised when a phone number is invalid."""
    pass

class InvalidProfileError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    """Raised when trying to create a user that already exists."""
    pass

class UserNotFoundError(Exception):
    pass

class AddressNotFound(Exception):
    pass
