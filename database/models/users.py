from database.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(Base):
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, nullable=False, index=True)
  email = Column(String, nullable=False, unique=True, index=True)
  phone = Column(String(10), nullable=False, unique=True)
  profile_pic = Column(String, nullable=True)
  role = Column(String, nullable=False)
  disabled = Column(Boolean(), default=False)
  hashed_password = Column(String, nullable=False)
  location = Column(String, nullable=True)