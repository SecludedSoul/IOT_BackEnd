from fastapi import FastAPI
from config import engine
import router
import model 
from fastapi.middleware.cors import CORSMiddleware

model.Base.metadata.create_all(bind=engine)




app = FastAPI()

origins = [
    "https://iot-front-three.vercel.app",  #  Vercel deploy 
    "http://localhost:5173",  # ในเครื่อง
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # อนุญาตทุก HTTP methods
    allow_headers=["*"],  # อนุญาตทุก HTTP headers
)

@app.get('/')
async def root():
    return {"message": "This is an API for React CRUD By CowanSoodLorr 65070141. You can go to path /users to check API structure."}

app.include_router(router.router, prefix="/users" , tags=["users"])
