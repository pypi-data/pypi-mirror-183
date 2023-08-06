import uvicorn
from fastapi import FastAPI
from api_utils.database import conn
from router import entities

app = FastAPI(title='Entities.ly',
              description='APIs for rr base entities Apis',
              version='0.1')
app.include_router(entities.router_entities)


def open_server(host: str = '127.0.0.1', port: int = 8000):
    uvicorn.run(app=app, host=host, port=port)


@app.on_event("startup")
async def startup():
    print("Connect to db instance...")


@app.on_event("shutdown")
async def shutdown():
    print("Closing db instance...")
    conn.close_connection()
