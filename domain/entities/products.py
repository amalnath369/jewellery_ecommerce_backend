from dataclasses import dataclass
from enum import Enum
from domain.entities.base import BaseEntity
from domain.entities.users import User
from domain.exceptions.product_exceptions import InvalidQuantityException,InvalidMoneyException
from typing import Optional
import uuid


class Category(Enum):
    RING = 'RING'
    NECKLACE = 'NECKLACE'
    EARRINGS = 'EARRINGS'
    BRACELET = 'BRACELET'
    ANKLET = 'ANKLET'


@dataclass(kw_only=True)
class Product(BaseEntity):
    name: str
    description: str
    category : Category
    
    _price: float    
    _quantity : int = 1
    _sku : Optional[str] = None

    brand: Optional[str] = None
    metal_type: Optional[str] = None
    metal_purity: Optional[str] = None
    weight: Optional[float] = None
    gemstone_type: Optional[str] = None
    gemstone_count: int = 0
    gemstone_weight: float = 0.0
    color: Optional[str] = None
    plating: Optional[str] = None
    style: Optional[str] = None
    occasion: Optional[str] = None
    gender: Optional[str] = None
    collection: Optional[str] = None
    certification: Optional[str] = None
    origin_country: Optional[str] = None
    care_instructions: Optional[str] = None


    def __post_init__(self):
        if self.price < 0:
            raise InvalidMoneyException("Price must be non-negative.")
        if self.quantity < 0:
            raise InvalidQuantityException("Quantity cannot be negative.")

        if not self.sku:
            self._sku = self._generate_sku()

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float):
        if new_price < 0 :
            raise InvalidMoneyException("Price must be non-negative.")
        self._price = new_price

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: int):
        if new_quantity < 0:
            raise InvalidQuantityException("Quantity cannot be negative.")
        self._quantity = new_quantity

    @property
    def sku(self) -> str:
        return self._sku


    def add_stock(self, count : int) -> None:
        if count <= 0:
            raise InvalidQuantityException('Quantity must be Greater than Zero!!!')
        else:
            self.quantity += count

    def remove_stock(self, count : int) -> None:
        if count <= 0:
            raise InvalidQuantityException('Quantity must be Greater than Zero!!!')
        
        if count > self.quantity:
            raise InvalidQuantityException('Not Enough Stock Available')
        
        self.quantity -= count


    def is_available(self) -> bool:
        return self.quantity > 0

    def _generate_sku(self) -> str:
        """Generate a SKU in the format: BRAND-CAT-XXXXXX"""
        brand_part = (self.brand or "GEN")[:3].upper()
        cat_part = self.category.value[:3].upper()
        unique_part = uuid.uuid4().hex[:6].upper()
        return f"{brand_part}-{cat_part}-{unique_part}"
    

    def update_price(self, new_price : float) -> None:
        if new_price <= 0:
            raise InvalidMoneyException("Price Must be Non Negative")      
        self.price = new_price




    

@dataclass(kw_only=True)
class ProductImage(BaseEntity):
    product_id: Product
    image_url: str


@dataclass(kw_only=True)
class ProductVideo(BaseEntity):
    product_id: Product
    video_url: Optional[str] = None


class ProductReviewRating(Enum):
    ONE_STAR = 1
    TWO_STAR = 2
    THREE_STAR = 3
    FOUR_STAR = 4
    FIVE_STAR = 5

@dataclass(kw_only=True)
class ProductReview(BaseEntity):
    product_id: Product
    user_id: User
    rating: ProductReviewRating
    review_text: Optional[str] = None



a = Product(
    name="Elegant Gold Ring",
    description="A beautiful 18k gold ring with intricate designs.",
    category=Category.RING,
    _price=299.99,
    _quantity=10,
    brand="GoldCraft"
)


