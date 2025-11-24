from sqlmodel import Field,Relationship
from .base_model import BaseModel
from typing import Optional,List,TYPE_CHECKING
from enum import Enum
from uuid import UUID

if TYPE_CHECKING:
    from database.models.users_model import UserModel
    from database.models.cart_model import CartItemModel



class Category(str, Enum):
    RING = 'RING'
    NECKLACE = 'NECKLACE'
    EARRINGS = 'EARRINGS'
    BRACELET = 'BRACELET'
    ANKLET = 'ANKLET'


class ProductModel(BaseModel, table=True):
    __tablename__ = "products"

    name: str = Field(index=True)
    description: Optional[str] = Field(default=None, index=True)
    category: Category = Field(sa_column_kwargs={"type_": "VARCHAR(50)"})

    price: float = Field(index=True)
    quantity: int = Field(default=1, index=True)
    sku: Optional[str] = Field(default=None, index=True, unique=True)

    brand : Optional[str] = Field(default=None, index=True)
    metal_type : Optional[str] = Field(default=None, index=True)
    metal_purity : Optional[str] = Field(default=None, index=True)
    weight : Optional[float] = Field(default=None, index=True)
    gemstone_type : Optional[str] = Field(default=None, index=True)
    gemstone_count : int = Field(default=0, index=True)
    gemstone_weight : float = Field(default=0.0, index=True)
    color : Optional[str] = Field(default=None, index=True)
    plating: Optional[str] = Field(default=None, index=True)
    style : Optional[str] = Field(default=None, index=True)
    occasion : Optional[str] = Field(default=None, index=True)
    gender : Optional[str] = Field(default=None, index=True)

    images : List["ProductImageModel"] = Relationship(back_populates="product")
    videos : Optional[List["ProductVideoModel"]] = Relationship(back_populates="product")
    reviews : Optional[List["ProductReviewModel"]] = Relationship(back_populates="product")

    cart_items : Optional[List["CartItemModel"]] = Relationship(back_populates="product")




class ProductImageModel(BaseModel, table=True):
    __tablename__ = "product_images"

    product_id: UUID = Field(default=None, foreign_key="products.id")
    image_url: str = Field(index=True)

    product : ProductModel = Relationship(back_populates="images")


class ProductVideoModel(BaseModel, table=True):
    __tablename__ = "product_videos"

    product_id: UUID = Field(default=None, foreign_key="products.id")
    video_url: str = Field(index=True)

    product : Optional[ProductModel] = Relationship(back_populates="videos")

class ProductReviewRating(int,Enum):
    ONE_STAR = 1
    TWO_STAR = 2
    THREE_STAR = 3
    FOUR_STAR = 4
    FIVE_STAR = 5

class ProductReviewModel(BaseModel, table=True):
    __tablename__ = "product_reviews"

    product_id: UUID = Field(default=None, foreign_key="products.id")
    user_id: UUID = Field(default=None, foreign_key="users.id")
    rating: ProductReviewRating = Field(index=True)
    comment: Optional[str] = Field(default=None, index=True)

    product : Optional[ProductModel] = Relationship(back_populates="reviews")
    user : Optional["UserModel"] = Relationship(back_populates="reviews")