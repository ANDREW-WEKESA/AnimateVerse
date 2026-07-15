from fastapi import FastAPI
from app.routers.health import router as health_router

app = FastAPI(title="AnimateVerse API", version="1.0.0")
app.include_router(health_router)`r`nfrom app.routers.auth import router as auth_router`r`napp.include_router(auth_router)

@app.get("/")
def root():
    return {"app":"AnimateVerse","status":"running","version":"1.0.0"}
