from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


# ====== Pydantic Schemas (what API receives/returns) ======
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    completed: bool = False


class TaskUpdate(BaseModel):
    # All optional for PATCH
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskPut(BaseModel):
    # For PUT (full update): require title, others optional
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    completed: bool = False


class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    # Pydantic v2: enable reading from ORM objects
    model_config = ConfigDict(from_attributes=True)