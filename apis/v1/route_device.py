from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from fastapi import Depends, Request
from apis.v1.route_login import get_current_user
from database.session import get_db
from database.models.users import User, Device, DeviceType, Switch
from database.schemas.users import ListDeviceResponse


router = APIRouter()


@router.get("/testing-device")
def dev(request: Request, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == 1).first()
    print(user.devices)
    return user


@router.get("/product-list/{user_id}", response_model=list[ListDeviceResponse])
def prod_list(user_id, db: Session = Depends(get_db)):
    devices = db.query(Device).filter(Device.user_id == user_id).all()
    return devices

@router.get("/switch-list/{device_type_id}")
def switch_list(device_type_id, db: Session = Depends(get_db)):
    switches = db.query(Switch).filter(Switch.type_id == device_type_id).all()
    return switches
