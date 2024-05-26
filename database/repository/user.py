from sqlalchemy.orm import Session
import sys
sys.path.append("..")
from database.schemas.users import User as UserCreate
from database.models.users import User
from auth import Hasher


def create_new_user(user:UserCreate,db:Session):
    user = User(
        username = user.username,
        email = user.email,
        phone = user.phone,
        profile_pic = user.profile_pic,
        location = user.location,
        role = user.role,
        hashed_password=Hasher.get_password_hash(user.password)
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user