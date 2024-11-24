from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from fastapi import Depends, Request, Body
from apis.v1.route_login import get_current_user
from database.schemas.users import User, ShowUser
from database.session import get_db
from typing import Annotated

router = APIRouter()

# CONNECT_TOPIC = "HOME/C8:2E:18:67:95:A8/POST"
# CONFIG_TOPIC = "HOME/C8:2E:18:67:95:A8/CONFIG"
TOPIC = "test/mqtt/3"

def subscribe(client, topic):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def publish(client, msg, topic):
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


@router.post("/connect-device", status_code=status.HTTP_201_CREATED)
def connect_device(request: Request, db: Session = Depends(get_db)):
    # user = create_new_user(user=user,db=db)

    client = request.app.extra["MQTT_CONN_CLIENT"]
    subscribe(client, TOPIC)
    return {}

@router.post("/send-command", status_code=status.HTTP_201_CREATED)
def publish_mqtt(request: Request, body: Annotated[dict, Body()], db: Session = Depends(get_db)):
    #sample_msg = {"home":{"light1":"ON","light2":"OFF","fan":"ON","socket":"OFF","fan_speed":"1"}}
    msg = str(body)
    client = request.app.extra["MQTT_CONN_CLIENT"]
    publish(client, msg, TOPIC)
    return {"MSG": "DONE"}