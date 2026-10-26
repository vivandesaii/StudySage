from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class DocumentCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None


class DocumentRead(BaseModel):
    id: int
    title: str
    description: str | None = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
