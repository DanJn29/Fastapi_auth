from fastapi import APIRouter, HTTPException, Response
from models import UserLoginSchema
from security import security
from users import users

router = APIRouter()

@router.post("/login")
def login(creds: UserLoginSchema, response: Response):
    for user in users.values():
        if creds.username == user["username"] and creds.password == user["password"]:
            token = security.create_access_token(uid="12345", data={"role": user["role"]})
            return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")