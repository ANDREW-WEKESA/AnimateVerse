from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate,UserLogin
from app.crud.user import create_user,authenticate_user
from app.core.token import create_access_token
from app.db.session import get_db

router=APIRouter(prefix="/auth",tags=["Authentication"])

@router.post("/register")
def register(data:UserCreate,db:Session=Depends(get_db)):
    user=create_user(db,data.username,data.email,data.password)
    return {"id":user.id,"username":user.username,"email":user.email}

@router.post("/login")
def login(data:UserLogin,db:Session=Depends(get_db)):
    user=authenticate_user(db,data.email,data.password)
    if not user:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    token=create_access_token({"sub":user.email})
    return {"access_token":token,"token_type":"bearer"}
