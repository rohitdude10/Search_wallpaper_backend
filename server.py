from fastapi import FastAPI, Request
import constant
from pydantic import BaseModel
from auto_wallpaper_changer import start_process
from fastapi.middleware.cors import CORSMiddleware
from auto_wallpaper_changer import download_image_from_url , get_next_page_data, get_prev_page_data
from fastapi.responses import JSONResponse
from fastapi import status

from dotenv import load_dotenv

load_dotenv()


class Wallpaper(BaseModel):
    
    url: str
    

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get("/topics")
async def root():
    print("getting request")
    return {"topics":constant.TOPICS}


@app.get("/wallpapers/{theme}")
async def get_wallpaper(theme):
    print("getting request")
    data = start_process(theme)
    return {"theme":data}


@app.post("/set_wallpaper/")
async def set_wallpaper(request:Request):
    body = await request.json()
    print("data==>",body)
    download_image_from_url(body["data"]["url"], body["data"]["id"])
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Wallpaper successfully set"})


@app.post("/get_next_page")
async def get_next_page(request:Request):
    body = await request.json()
    print("data==>",body)
    data=get_next_page_data(body["next_page"])
    return {"theme":data}


@app.post("/get_prev_page")
async def get_prev_page(request:Request):
    body = await request.json()
    print("data==>",body)
    data=get_prev_page_data(body["prev_page"])
    return {"theme":data}
    
    