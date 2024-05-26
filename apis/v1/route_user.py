from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from fastapi import Depends
from apis.v1.route_login import get_current_user
from database.schemas.users import User, ShowUser
from database.session import get_db
from database.repository.user import create_new_user

router = APIRouter()


@router.post("/register", response_model = ShowUser, status_code=status.HTTP_201_CREATED)
def register_user(user : User,db: Session = Depends(get_db)):
    user = create_new_user(user=user,db=db)
    return user

@router.get("/testing")
def safe_view(db: Session = Depends(get_db), current_user: User=Depends(get_current_user)):
    return {"message": "success"}