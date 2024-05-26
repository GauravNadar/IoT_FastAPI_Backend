from pydantic import BaseModel
from pydantic import BaseModel,EmailStr, Field

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