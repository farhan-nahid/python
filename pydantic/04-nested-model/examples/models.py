from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
  street: str
  city: str
  postal_code: str


class User(BaseModel):
  id: int
  username: str
  address: Address


class Comment(BaseModel):
  id: int
  content: str
  replies: Optional[List['Comment']] = None



Comment.model_rebuild()