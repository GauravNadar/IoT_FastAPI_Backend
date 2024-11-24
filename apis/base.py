from fastapi import APIRouter

from apis.v1 import route_user
from apis.v1 import route_login
from apis.v1 import route_mqtt
from apis.v1 import route_device


api_router = APIRouter()
api_router.include_router(route_user.router,prefix="",tags=["users"])
api_router.include_router(route_login.router,prefix="",tags=["login"])
api_router.include_router(route_mqtt.router,prefix="",tags=["mqtt"])
api_router.include_router(route_device.router,prefix="",tags=["device"])