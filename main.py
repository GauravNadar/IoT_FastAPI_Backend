from fastapi import FastAPI
from database.session import engine
from database.base import Base
from apis.base import api_router
from core.config import settings
import uvicorn
from contextlib import asynccontextmanager
from paho.mqtt import client as mqtt_client

broker = '13.60.190.6'
port = 1883
client_id = f'python-mqtt-123456'

app_connections = {}

def create_tables():         
	Base.metadata.create_all(bind=engine)
     
def include_router(app):   
	app.include_router(api_router)
	
def connect_mqtt_client():
    def on_connect(client, userdata, flags, rc, properties):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id=client_id, callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)
    client.username_pw_set("adminuser", "password@123")
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect MQTT server
    #app_connections["MQTT_CONN_CLIENT"] = connect_mqtt_client
    print("STARTED IOT APP")
    app.extra["MQTT_CONN_CLIENT"] = connect_mqtt_client()
    app.extra["MQTT_CONN_CLIENT"].loop_start()
    yield
    # Close MQTT server connection
    #app_connections.clear()
    print("STOPPED IOT APP")
    app.extra["MQTT_CONN_CLIENT"].loop_stop()
    app.extra["MQTT_CONN_CLIENT"].disconnect()
    app.extra.clear()
        

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION, lifespan=lifespan)
    create_tables()
    include_router(app)
    return app


app = start_application()

if __name__ == '__main__':
	uvicorn.run(app, host="0.0.0.0", port=8000)
