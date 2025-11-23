import uuid
from sqlmodel import SQLModel,Field
from datetime import datetime
from typing import Optional
from uuid import UUID



class BaseModel(SQLModel):
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})
    is_active: bool = Field(default=True)