from fastapi import FastAPI, HTTPException, Depends
from authx import AuthX, AuthXConfig
from pydantic import BaseModel


app = FastAPI()

config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["headers"]
security = AuthX(config=config)


users = {
    "user1":{
        "username": "user10",
        "password": "password1",
        "role": "user",
    },
    "user2":{
        "username": "user11",
        "password": "password2",
        "role": "admin",
    },
}

class UserLoginSchema(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(creds: UserLoginSchema):
    for user in users.values():
        if creds.username == user["username"] and creds.password == user["password"]:
            token = security.create_access_token(uid="12345", data={"role": user["role"]})
            print(f"Generated token: {token}")
            return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/")
def protected(token: str = Depends(security.access_token_required)):
    return {"data": "PROTECTED INFO"}

@app.get("/admin")
def super_protected(token: str = Depends(security.access_token_required)):
    # token is already payload,no need to decode
    if token.role != "user":
        return {"data": "SUPER PROTECTED INFO"}
    raise HTTPException(status_code=401, detail="YOU ARE NOT ADMIN")

