class InvalidQuantityException(Exception):
    """Raises when invalid product quantity is added"""
    pass


class InvalidMoneyException(Exception):
    """Raises when invalid Money is added"""
    pass


class OutofStockException(Exception):
    pass