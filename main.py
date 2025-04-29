from fastapi import FastAPI
from routes import auth_routes, protected_routes

app = FastAPI()


app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(protected_routes.router, prefix="/protected", tags=["Protected"])