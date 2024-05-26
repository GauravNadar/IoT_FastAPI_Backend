from fastapi import FastAPI
from database.session import engine
from database.base import Base
from apis.base import api_router
from core.config import settings
import uvicorn

def create_tables():         
	Base.metadata.create_all(bind=engine)
     
def include_router(app):   
	app.include_router(api_router)
        

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()

if __name__ == '__main__':
	uvicorn.run(app, host="0.0.0.0", port=8000)
