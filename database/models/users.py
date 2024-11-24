from database.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSON
from typing import List


class User(Base):
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, nullable=False, index=True)
  email = Column(String, nullable=False, unique=True, index=True)
  phone = Column(String(10), nullable=True, unique=True)
  profile_pic = Column(String, nullable=True)
  role = Column(String, nullable=False)
  disabled = Column(Boolean(), default=False)
  hashed_password = Column(String, nullable=False)
  location = Column(String, nullable=True)
  devices: Mapped[List["Device"]] = relationship()
  

class Device(Base):
  id = Column(Integer, primary_key=True, index=True)
  device_name = Column(String, nullable=False)
  user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
  mac_id = Column(String, nullable=False)
  device_type: Mapped[List["DeviceType"]] = relationship()


class DeviceType(Base):
  id = Column(Integer, primary_key=True, index=True)
  user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
  device_id: Mapped[int] = mapped_column(ForeignKey("device.id"))
  type_name = Column(String, nullable=False)
  switches: Mapped[List["Switch"]] = relationship()

class Switch(Base):
  id = Column(Integer, primary_key=True, index=True)
  user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
  mac_id = Column(String, nullable=False)
  config = type_name = Column(JSON, nullable=False)
  type_id: Mapped[int] = mapped_column(ForeignKey("devicetype.id"))