from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
  username: str

  @field_validator('username')
  def username_validator(cls, value):
    if len(value) < 4:
      raise ValueError("Username at least 4 characters")
    return value


class SignUpData(BaseModel):
  password: str
  confirm_password: str

  @model_validator(mode='after')
  def password_validator(cls, values):
    if values.password != values.confirm_password:
      raise ValueError("Password doesn't match")
    return values
  

class Product(BaseModel):
  name: str
  price: float
  quantity: int

  @computed_field
  @property
  def total_price(self) -> float:
    return self.price * self.quantity