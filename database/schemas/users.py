from pydantic import BaseModel
from pydantic import BaseModel,EmailStr, Field
from typing import List, Dict

class User(BaseModel):
    username: str = Field(..., min_length=4)
    email: EmailStr
    phone: str
    profile_pic: str
    location: str
    role: str
    password: str

class ShowUser(BaseModel):
    id: int
    email : EmailStr
    phone : str
    profile_pic: str
    location: str
    role: str

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True


class ChildSchema(BaseModel):
      id: int
      user_id: int
      device_id: int
      type_name: str


class ListDeviceResponse(BaseModel):
    id: int
    device_name: str
    user_id: int
    mac_id: str
    device_type: List[ChildSchema] = []

    class Config():
        orm_mode = True