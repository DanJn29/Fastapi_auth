from fastapi import FastAPI
import uvicorn
from routes import auth_routes, protected_routes

app = FastAPI()


app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(protected_routes.router, prefix="/protected", tags=["Protected"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)