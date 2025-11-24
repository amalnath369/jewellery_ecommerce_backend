from typing import Optional,TYPE_CHECKING
from sqlmodel import Field,Relationship
from .base_model import BaseModel   
from uuid import UUID


if TYPE_CHECKING:
    from database.models.product_models import ProductModel
    from database.models.users_model import UserModel


class CartModel(BaseModel, table=True):
    __tablename__ = "carts"

    user_id: UUID = Field(default=None, foreign_key="users.id", index=True)

    items: Optional[list["CartItemModel"]] = Relationship(back_populates="cart", sa_relationship_kwargs={"cascade": "all, delete-orphan"})

    user : "UserModel" = Relationship(back_populates="carts")

class CartItemModel(BaseModel, table=True):
    __tablename__ = "cart_items"

    cart_id: UUID = Field(default=None, foreign_key="carts.id", index=True)
    product_id: UUID = Field(default=None, foreign_key="products.id", index=True)

    quantity: int = Field(default=1, index=True)
    unit_price: float = Field(index=True)

    # Relationship back to parent cart
    cart: "CartModel" = Relationship(back_populates="items")

    product: "ProductModel" = Relationship(back_populates="cart_items")