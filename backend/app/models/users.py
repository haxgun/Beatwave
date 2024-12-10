import uuid
from datetime import datetime

from pydantic import EmailStr
from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    access_token: str = Field(nullable=False)
    refresh_token: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class User(UserBase, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        nullable=False,
    )
