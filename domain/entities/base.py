from dataclasses import dataclass, field
from datetime import datetime,UTC
from typing import Optional

@dataclass
class BaseEntity:
    id: Optional[int] = None
    created_at: datetime = field(default_factory=lambda :datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda : datetime.now(UTC))
    is_active: bool = True

    def mark_inactive(self):
        self.is_active = False
        self.updated_at = datetime.now(UTC)
