import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import api_router

app = FastAPI()

app.include_router(api_router, prefix="")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем запросы с вашего фронтенда
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешаем все заголовки
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, port=8080)
