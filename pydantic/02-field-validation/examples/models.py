from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
  user_id: int
  items: List[str]
  quantities: Dict[str, int]


class Product(BaseModel):
  name: str
  price: float
  description: Optional[str] = None