from database.base_class import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer

class Token(Base):
  id = Column(Integer, primary_key=True, index=True)
  access_token = Column(String, nullable=False)
  refresh_token = Column(String, nullable=False)