from fastapi import APIRouter, Depends, HTTPException
from security import security

router = APIRouter()

@router.get("/")
def protected(token: str = Depends(security.access_token_required)):
    return {"data": "PROTECTED INFO"}

@router.get("/admin")
def super_protected(token: str = Depends(security.access_token_required)):
    if token.role != "admin":
        raise HTTPException(status_code=401, detail="YOU ARE NOT ADMIN")
    return {"data": "SUPER PROTECTED INFO"}
