from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends,APIRouter, Header
from sqlalchemy.orm import Session
from fastapi import status,HTTPException
from fastapi.security import OAuth2PasswordBearer 
from database.session import get_db
from auth import Hasher
from database.schemas.token import Token
from database.repository.login import get_user
from core.security import create_access_token
from jose import jwt, JWTError

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "mysecretkey"
ACCESS_TOKEN_EXPIRE_MINUTES = 5
REFRESH_TOKEN_EXPIRE_MINUTES = 10
ALGORITHM = "HS256"

def authenticate_user(email: str, password: str,db: Session):
    user = get_user(email=email,db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db: Session= Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password,db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme), db: Session= Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(email=username, db=db)
    if user is None:
        raise credentials_exception
    return user
