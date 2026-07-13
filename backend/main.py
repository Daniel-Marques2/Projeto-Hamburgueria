from fastapi import FastAPI

app = FastAPI()

from backend.routes.auth_routes import auth_router
from backend.routes.order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)


#uvicorn backend.main:app --reload